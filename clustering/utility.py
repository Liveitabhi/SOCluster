import mysql.connector as sqlc
from sklearn.metrics import davies_bouldin_score, calinski_harabasz_score, silhouette_score
import umap
import hdbscan
from scipy.spatial.distance import euclidean
from DBCV import DBCV

# Input Question from MySQL Database
def getInputQuestionSQL(username,password,tag_list,number_of_samples,host="localhost"):
    mydb = sqlc.connect(
        host=host,
        user=username,
        password=password
    )
    connection = mydb.cursor()

    connection.execute("USE stackoverflow")

    sql_tag_list = ["INSTR(Tags,'<" + x + ">') > 0" for x in tag_list]
    final_tag_condition = " || ".join(sql_tag_list)

    sql = "SELECT * FROM Posts WHERE PostTypeId=1 AND (" + str(final_tag_condition) + ") AND Body NOT LIKE '%<img>%' LIMIT " + str(number_of_samples)

    connection.execute(sql)

    row_headers = [x[0] for x in connection.description]
    result = connection.fetchall()

    return result, row_headers

# Printing Information regarding Clustering 
def printInitialInfo(nos,threshold,tag_list,transformer_model,vlen):

    print("----------------------------------------------------------------------------------")
    print("Number of Samples : ",nos)
    print("Threshold : ",threshold)
    print("Tag List : ",tag_list)
    print("Model : ",transformer_model)
    print("----------------------------------------------------------------------------------")

    # Dimensions of embeded vector
    print("Embeded Vector Dimension Info:")
    print("Length of an array: ", nos)
    print('Sample vector - length', vlen)
    print("----------------------------------------------------------------------------------")

# BFS for generation Clusters
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


# generating clusters using UMAP + HDBSCAN
def generate_clusters(message_embeddings,
                      n_neighbors,
                      n_components, 
                      min_cluster_size,
                      random_state = 42):
    """
    Generate HDBSCAN cluster object after reducing embedding dimensionality with UMAP
    """
    
    umap_embeddings = (umap.UMAP(n_neighbors=n_neighbors, 
                                n_components=n_components, 
                                metric='cosine', 
                                random_state=random_state,min_dist=0.0)
                            .fit_transform(message_embeddings))

    clusters = hdbscan.HDBSCAN(min_cluster_size = min_cluster_size,
                               min_samples=1,
                               metric='euclidean', 
                               cluster_selection_method='eom').fit(umap_embeddings)

    return clusters,umap_embeddings

# Utility to generate Clusters using multiple BFS call
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

# Printing Cluster Information
def printCluster(clusters,q_arr,details=False,print_min_size=2):
    
    cluster_size_dict = dict({})
    for cluster in clusters:
        length = len(cluster)
        if length in cluster_size_dict:
            cluster_size_dict[length] += 1
        else:
            cluster_size_dict[length] = 1
        if details:
            if(len(cluster) >= print_min_size):
                print("\n<========================================   CLUSTER START   ==========================================================>\n")
                for node in cluster:
                    print(node, " : ",q_arr[node])
                    print("--------------------------------------------------------------------------------------------------")
                print("\n<========================================   CLUSTER END   =========================================================>\n")
    
    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
    ("--------------------------------------------------------------------------------------------------")
    print("Total Clusters : ", len(clusters))
    print("--------------------------------------------------------------------------------------------------")

    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")

    for key in cluster_size_dict:
        print(key, " : ",cluster_size_dict[key])
        print("--------------------------------------------------------------------------------------------------")

    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")

# Printing Evaluation Score
def printScores(embedding,labels):
    try:
        score = silhouette_score(embedding, labels, metric='euclidean')
        print("Evaluation Score SH (higher better): ", score)
    except:
        print("Evaluation Score SH (higher better): NA")
    try:
        score = calinski_harabasz_score(embedding, labels)
        print("Evaluation Score CH (higher better): ", score)
    except:
        print("Evaluation Score CH (higher better): NA")
    try:
        score = davies_bouldin_score(embedding, labels)
        print("Evaluation Score DB (lower better): ", score)
    except:
        print("Evaluation Score DB (lower better): NA")
    # Tried to use DBCV metric for evaluating Density based clustering but its too slow for large number of questions
    # try:
    #     score = DBCV(embedding,labels,euclidean)
    #     print("Evaluation Score DBCV (higher better): ", score)
    # except:
    #     print("Evaluation Score DBCV (higher better): NA")

