import utility
import config
from question import Question
from sklearn.metrics.pairwise import cosine_similarity as cs
from sentence_transformers import SentenceTransformer
import sys
import time

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
username = 'username'
password = 'password'

result, row_headers = utility.getInputQuestionSQL(username,password)

q_arr = list()

# Extracting questions from the result
for x in result:
    q_x = Question(x,row_headers)
    q_arr.append(q_x.getText())

# Vectorization of question
start = time.time()
model = SentenceTransformer(transformer_model)
embedding = model.encode(q_arr)
end = time.time()
print("Model + Embedding Time : ",end-start)

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

# Printing Cluster Information
utility.printCluster(clusters,details=enable_question_print)

# Printing Evaluation Score
utility.printScores(embedding,labels)