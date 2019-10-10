# ANS.analogy
using AI to answer the Analogy question
----
## Description
We all are gone through several questions of Analogies like Man is to Woman, as king is to queen and many more questions like this.
![alt text](https://github.com/udaram/ANS.analogy/blob/master/gif/Word-Vectors.png)<br>
After answering several such types of question we get bored and now we want that our computer to automatically answer these questions for the provided question and its options.<br>
Here is an Application created using python GUI framework Tkinter which is able to answer such types of questions.
Which uses the simple concept of Word embeddings and Cosine Similarity. Word Embeddings are the numeric vector representation of a word, a vector associated with a word is sufficient enough to represent that word in every context. and cosine Similarity is the measure of similarity between two non-zero vectors.
Here, I'm using glove word embedding and the concept of cosine similarity to make such types of analogies.

## Dataset
* Glove6B dataset [Link](https://drive.google.com/open?id=1GI5sWeCxgJEgToeVmakL69oDlXowXGU4)
----
## Requirements
* Python 3.5
* Numpy
* Tkinter 

*Test model*
--------------------------
```
$ python3 gui.py

this gui is made using python Tkinter package 
```
*Test Results*
--------------
Here, some glimpses of Best results which i have got during testing.<br>
![alt text](https://github.com/udaram/ANS.analogy/blob/master/gif/1.gif)
![alt text](https://github.com/udaram/ANS.analogy/blob/master/gif/2.gif)
![alt text](https://github.com/udaram/ANS.analogy/blob/master/gif/3.gif)
