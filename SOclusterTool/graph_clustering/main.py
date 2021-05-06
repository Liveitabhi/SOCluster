import mysql.connector as sqlc
import json
import re
from io import StringIO
from html.parser import HTMLParser
from sklearn.metrics.pairwise import cosine_similarity as cs
from sentence_transformers import SentenceTransformer
from sklearn.metrics import davies_bouldin_score, calinski_harabasz_score, silhouette_score
import sys
import getopt
import time

number_of_samples = 1000
tag_list = ['javascript', 'python']
max_body_length = 200
threshold = 0.5
print_min_size = 2
enable_question_print = True
transformer_model = 'distilbert-base-nli-stsb-mean-tokens'

# Argument list
argumentList = sys.argv[1:]

# n: number of samples, t: threshold, m: model, p: print min size
options = "n:t:m:p:"

# nos: number os samples, tag-list: tag list, max-body: max body length, model: model, print: enable question print, print-min-size: print min size
long_options = ["nos", "tag-list =", "max-body",
                "th", "model", "print", "print-min-size"]


try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)

    # checking each argument
    for (currentArgument, currentValue) in arguments:
        if currentArgument.strip() in ("-n", "--nos"):
            number_of_samples = int(currentValue)
        elif currentArgument.strip() in ("-t", "--th"):
            threshold = float(currentValue)
        elif currentArgument.strip() in ("-m", "--model"):
            transformer_model = currentValue
        elif currentArgument.strip() in ("-p", "--print-min-size"):
            print_min_size = int(currentValue)
        elif currentArgument.strip() == "--tag-list":
            tag_list = list(map(str, currentValue.strip('[]').split(',')))
        elif currentArgument.strip() == "--print":
            enable_question_print = bool(currentValue)
        elif currentArgument.strip() == "--print-min-size":
            print_min_size = int(currentValue)
except getopt.error as err:
	# output error, and return with an error code
	print (str(err))

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


class Question:
    def __init__(self, row_headers, obj):
        self.question = dict(zip(row_headers, obj))
        # print(json.dumps(self.question,default=json_util.default,indent=4))
        self.setText()

    def setText(self):
        html = self.question["Body"]
        s = MLStripper()
        s.feed(html)
        text = s.get_data()
        # partial_html = re.sub(r"<(/)?br(/)?>", "\n", html)
        # text = re.sub(r"<[^>]*>", " ", partial_html)
        # print("html : ",html)
        # print("text : ",text)
        self.question_text = text

    def getText(self):
        return self.question_text

def getClusters(mat, nos,th):
    visited = [False] * nos
    labels = [0] * nos
    cluster_index = 1
    cluster_set = list()
    for i in range(0, nos):
        if visited[i] == False:
            cluster = bfs(i, mat,visited,th,nos)
            for ele in cluster:
                labels[ele] = cluster_index
            cluster_index += 1
            cluster_set.append(cluster)
    return cluster_set, labels

def bfs(node, mat,visited,threshold,nos):
    cluster = [node]
    visited[node] = True
    index = 0
    while index < len(cluster):
        curr_node = cluster[index]
        for i in range(0, nos):
            if(i == curr_node):
                continue
            else:
                if visited[i] == False and mat[curr_node][i] >= threshold:
                    visited[i] = True
                    cluster.append(i)
        index += 1
    return cluster

mydb = sqlc.connect(
    host="localhost",
    user="stackadmin",
    password="ADT@cs17b"
)
connection = mydb.cursor()

connection.execute("USE stackoverflow")

sql_tag_list = ["INSTR(Tags,'<" + x + ">') > 0" for x in tag_list]
final_tag_condition = " || ".join(sql_tag_list)
# print(final_tag_condition)

sql = "SELECT * FROM Posts WHERE PostTypeId=1 AND (" + str(final_tag_condition) + ") AND LENGTH(Body) <= " + str(max_body_length) + " LIMIT " + str(number_of_samples)

connection.execute(sql)

row_headers = [x[0] for x in connection.description]
result = connection.fetchall()

q_arr = list()

# Extracting questions from the result
for x in result:
    q_x = Question(row_headers, x)
    q_arr.append(q_x.getText())

# Vectorization of question
start = time.time()
model = SentenceTransformer(transformer_model)
embedding = model.encode(q_arr)
end = time.time()
print("MODEL + EMBEDDING : ",end-start)

print("----------------------------------------------------------------------------------")
print("Number of Samples : ",len(embedding))
print("Threshold : ",threshold)
print("Tag List : ",tag_list)
print("Model : ",transformer_model)
print("----------------------------------------------------------------------------------")

# Dimensions of embeded vector
print("Length of an array: ", len(embedding))
print('Sample vector - length', len(embedding[0]))

print("----------------------------------------------------------------------------------")
# Graph generation
start = time.time()
similarity_index = cs(embedding)
end = time.time()
print("CS TIME : ",end-start)

#print("--------------------------------------------------------------------------------------------------")
#print(similarity_index)

start = time.time()

clusters, labels = getClusters(similarity_index,len(embedding),threshold)

end = time.time()

print("BFS TIME : ",end-start)

cluster_size_dict = dict({})

if enable_question_print == True:
    for cluster in clusters:
        length = len(cluster)
        if length in cluster_size_dict:
            cluster_size_dict[length] += 1
        else:
            cluster_size_dict[length] = 1
        if(len(cluster) >= print_min_size):
            for node in cluster:
                print(node, " : ",q_arr[node])
                print(
                    "--------------------------------------------------------------------------------------------------")
            print("\n<==================================================================================================>\n")
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")

("--------------------------------------------------------------------------------------------------")
print("Total Clusters : ", len(clusters))
print("--------------------------------------------------------------------------------------------------")

print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")

for key in cluster_size_dict:
    print(key, " : ",cluster_size_dict[key])
    print("--------------------------------------------------------------------------------------------------")

try:
    score = silhouette_score(embedding, labels, metric='euclidean')
    print("Evaluation Score SH (higher better 0.55): ", score)
except:
    print("Evaluation Score SH (higher better 0.55): NA")
try:
    score = calinski_harabasz_score(embedding, labels)
    print("Evaluation Score CH (higher better 561.62): ", score)
except:
    print("Evaluation Score CH (higher better 561.62): NA")
try:
    score = davies_bouldin_score(embedding, labels)
    print("Evaluation Score DB (lower better 0.6619): ", score)
except:
    print("Evaluation Score DB (lower better 0.6619): NA")