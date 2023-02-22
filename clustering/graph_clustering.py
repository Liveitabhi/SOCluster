import utility
import config
from question import Question
from sklearn.metrics.pairwise import cosine_similarity as cs
from sentence_transformers import SentenceTransformer
import sys
import time

from transformers import AutoTokenizer, AutoModel
import torch

# Argument list
argumentList = sys.argv[1:]

# Setting Config Parameters
config_params = config.getConfig(argumentList)
if not bool(config_params):
    print("Configuration not found...")
    sys.exit()
locals().update(config_params)

# Getting Question From MySQL Database
# Change this part if you want to import questions from file or other database

# username and password credential for connecting to MySQL database
username = "root"
password = "user@123"

result, row_headers = utility.getInputQuestionSQL(username,password,tag_list,number_of_samples)

q_arr = list()
c_arr = list()

# Extracting questions from the result
for x in result:
    q_x= Question(x,row_headers)
    q, c = q_x.getText()
    q_arr.append(q)
    c_arr.append(c)

print('Number of questions: ', len(q_arr))
# Vectorization of question
start = time.time()
model = SentenceTransformer(transformer_model)
embedding = model.encode(q_arr)
end = time.time()
print("Model + Embedding Time : ",end-start)

# Code for using CodeBERT for code
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")
code_embeddings = []
for i, code in enumerate(c_arr):
    print('Processing code: ', i+1, '/', len(c_arr))
    code_tokens = tokenizer(code, truncation=True, max_length=512)
    # tokens = [tokenizer.cls_token] + code_tokens + [tokenizer.eos_token]
    # token_ids = tokenizer.convert_tokens_to_ids(tokens)
    context_embeddings=model(torch.tensor(code_tokens['input_ids'])[None,:])[0]
    context_embeddings = torch.mean(context_embeddings, dim=1)
    code_embeddings.append(context_embeddings.detach().numpy())

code_embeddings = [torch.tensor(x) for x in code_embeddings]
code_embeddings = torch.stack(code_embeddings).squeeze(1)

# Concat
embedding = torch.tensor(embedding)
embedding = torch.cat((embedding, code_embeddings), dim=1)

# Printing Information regarding Clustering
utility.printInitialInfo(len(embedding),threshold,tag_list,transformer_model,len(embedding[0]))

# Pairwise Cosine Similarity Index Matrix
start = time.time()
similarity_index = cs(embedding)
end = time.time()
print("Cosine Similarity Index Matrix Calculation Time : ",end-start)

# Cluster Generation
start = time.time()
clusters, labels = utility.getClusters(similarity_index,len(embedding),threshold)
end = time.time()
print("Cluster Generation Time : ",end-start)
print("--------------------------------------------------------------------------------------------------")

# Printing Cluster Information
utility.printCluster(clusters,q_arr,details=enable_question_print,print_min_size=print_min_size)

# Printing Evaluation Score
utility.printScores(embedding,labels)
