# SO*Cluster* - Towards Intent-based Clustering of Stack Overflow Questions using Graph-Based Approach

## What is SO*Cluster*?
1. SO*Cluster* is a tool based on Sentence-BERT vectorizer for creating *Intent*-clusters using a graph-based clustering algorithm.
2. The current version clusters StackOverflow questions which do not contain any image, code-snippet or table involved.
3. Support for image/code-snippet containing StackOverflow questions can be added to SO*Cluster* in the future.

## Features of SO*Cluster* :
1. SO*Cluster* uses *intent* as a key concept to cluster the StackOverflow questions.
2. It uses a graph-based clustering algortihm. (State-of-the art clustering methods are often based on graphical representations of the relationships among data points [<a href="https://ojs.aaai.org/index.php/AAAI/article/view/10302/10161">see here</a>])
3. It evaluates the clusters on three evaluation metrics - *Silhouette coefficient, Calinkski-Harabasz Index & Davies-Bouldin Index*, as well as prints the spread of the clusters over different sizes.

## Uses of SO*Cluster* :
There are many unanswered questions on StackOverflow. Main reasons behind more than 50% of these are *Failing to attract an expert member; Too short, hard to follow; and Duplicate question*.

Developers can use SO*Cluster* to cluster the StackOverflow questions - including both answered and unanswered ones.

These *Intent*-based clusters can be leveraged to answer unanswered questions using other answered questions in the same cluster.

Also, SO*Cluster* evaluates these clusters to tell how *good* the selected StackOveflow dataset is for our intended goal of Automatic Question Answering.

## Working of SO*Cluster* :
SO*Cluster* can be divided into three main steps as shown:

![Arch diagram Horizontal](https://user-images.githubusercontent.com/46972481/117248272-53706b00-ae5d-11eb-9ef6-252dbbf36304.png)

1. **Dataset Generation and Pre-processing** :-
    1. Data Dump - We downloaded SO post data from Stack-Exchange data dump archives [<a href="https://archive.org/download/stackexchange">link</a>]
    2. Pre-processing - We filtered and pre-processed the database and ignored questions that contained *images, code-snippets, tables, etc*.
    3. Feature Vectorization - We used *Sentence*-BERT to generate 768-dimensional feature vectors.
2. **Graph Construction** :-
    1. Similarity Index - SO*Cluster* uses cosine similarity as its metric to calculate the similairty between two vectors.
    2. Graph generation - It creates a weighted undirected graph using the feature vectors obtained as nodes and cosine similarity between them as the edge weights.
3. **Clustering** :-
    In this step, SO*Cluster* uses a graph-based clustering algorithm which takes the weighted undirecteed graph as input and provides a set of clusters as output.
    It uses threshold similarity as a parameter to invalidate those edges whose weight is less than the given threshold similarity.
<img width=500 alt="Clustering Algorithm" src="https://user-images.githubusercontent.com/46972481/117269210-b79f2900-ae75-11eb-8dde-cec7cdf1ba12.JPG">


## Example Clusters generated through SO*Cluster* :
- ![image](https://user-images.githubusercontent.com/46972481/117282080-fa66fe00-ae81-11eb-8633-91de69eab375.png)
- ![image](https://user-images.githubusercontent.com/46972481/117282266-2b473300-ae82-11eb-9015-f5450a6e95a0.png)
- ![image](https://user-images.githubusercontent.com/46972481/117282307-37cb8b80-ae82-11eb-9a1d-c056ae0c2ff6.png)

Here each image represents questions clustered by SO*Cluster* in the same cluster. Notice the similarity in the *intents* of the questions clustered together...

## Important files in SO*Cluster* Repository :
Inside the data directory, "database_script.sql" file contains the code to handle the StackOverflow data dump and create well-organized SQL tables.

Inside the *clustering* directory, "graph_clustering.py" script contains the source code of SO*Cluster* tool.

The *result_script.sh* file is a bash script that can be used to reproduce the experiment done in the paper.


## Steps to use SO*Cluster* :
1. Download this repository in your local machine.
2. Unzip the folder and extract it to a location of your choice on your PC.
3. Also, download the StackOverflow data dump [<a href="https://archive.org/download/stackexchange">link</a>] (only *Posts* zip file) from Stack Exchange archives in your PC and extract it.
4. Inside the SOCluster repository, go to *data/database_script.sql* file. There, provide the local path to the *Posts.xml* data dump file at appropriate location (in the end).
5. Run the *database_script.sql* file.
6. Now, go to *clustering/graph_clustering.py* file and provide your MySQL user credentials (username and password) at required place.
7. Run the *graph_clustering.py* file using the command `python3 graph_clustering.py -n NUMBER_OF_QUES -t THRESHOLD_SIMILARITY --tag-list="[TAG1,TAG2,..]"`.
   A sample command would be `python3 graph_clustering.py -n 10000 -t 0.65 --tag-list="[javascript,python]"`.
8. The clusters will be printed on your screen.
9. You can also run the *result_script.sh* bash file to repeat the experiment done in the paper.

## Walkthrough :
You can find the walkthrough of the tool <a href="https://youtu.be/uyn8ie4h3NY">here</a>

## How to contribute to SO*Cluster* :
We will be very happy to receive any kind of contributions. Incase of a bug or an enhancement idea or a feature improvement idea, please open an issue or a pull request. Incase of any queries or if you would like to give any suggestions, please feel free to contact Abhishek Kumar (cs17b002@iittp.ac.in), Deep Ghadiyali (cs17b011@iittp.ac.in) or Sridhar Chimalakonda (ch@iittp.ac.in) of RISHA Lab, IIT Tirupati, India.

