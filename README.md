# SO*Cluster* - Towards Intent-based Clustering of Stack Overflow Questions using Graph-Based Approach

## What is SO*Cluster*?
1. SO*Cluster* is a tool based on Sentence-BERT vectorizer for creating *Intent*-clusters using a graph-based clustering algorithm.
2. The current version clusters StackOverflow questions which do not contain any image, code-snippet or table involved.
3. Support for image/code-snippet containing StackOverflow questions can be added to SO*Cluster* in the future.

## Features of SO*Cluster*:
1. SO*Cluster* uses *intent* as a key concept to cluster the StackOverflow questions.
2. It uses a graph-based clustering algortihm. (State-of-the art clustering methods are often based on graphical representations of the relationships among data points [<a href="https://ojs.aaai.org/index.php/AAAI/article/view/10302/10161">here</a>])
3. It evaluates the clusters on three evaluation metrics - *Silhouette coefficient, Calinkski-Harabasz Index & Davies-Bouldin Index* as well as prints the spread of the clusters over different sizes.

## Uses of SO*Cluster*:
There are many unanswered questions on StackOverflow. Main reasons behind more than 50% of these are *Failing to attract an expert member; Too short, hard to follow; and Duplicate question*.

Developers can use SO*Cluster* to cluster the StackOverflow questions - including both answered and unanswered ones.

These *Intent*-based clusters can be leveraged to answer unanswered questions using other answered questions in the same cluster.

Also, SO*Cluster* evaluates these clusters which can tell how *good* the selected StackOveflow dataset is for our intended goal of Automatic Question Answering.

## Working of SO*Cluster*:
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

## Example Cluster:
<figure>
<img width=500 alt="Explanation" src="https://user-images.githubusercontent.com/35232831/117125604-616bb080-adb7-11eb-9048-c006557ab804.png">
<figcaption>
Part of the generated output for Quick Sort program. [A] is the expanded view of the first collapsible block and hence includes lower level information as well. [B] is the sliding-window interface for loops. [C] represent the high level information for the first recursive call. [H] shows the value returned by the function shown in [A]. [D] shows the arrows using which we can navigate through iterations of the loop.[E] highlights the line number of the corresponding line of code. [F] contains the line of code. [G] highlights our natural language description for the change in variables due to [F]. [I] shows the name of the file.
</figcaption>
</figure>

## What's inside SO*Cluster* Repository:


## Steps to use SO*Cluster*:
1. 

## Walkthrough:
You can find the walkthrough of the tool <a href="https://youtu.be/">here</a>

## How to contribute to SO*Cluster*:
We will be very happy to receive any kind of contributions. Incase of a bug or an enhancement idea or a feature improvement idea, please open an issue or a pull request. Incase of any queries or if you would like to give any suggestions, please feel free to contact Abhishek Kumar (cs17b002@iittp.ac.in), Deep Ghadiyali (cs17b011@iittp.ac.in) or Sridhar Chimalakonda (ch@iittp.ac.in) of RISHA Lab, IIT Tirupati, India.

