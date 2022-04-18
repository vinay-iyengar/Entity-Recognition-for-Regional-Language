# Entity-Recognition-for-Regional-Language
The main objective is to develop a system, where in we can classify the entites in the sentence or input that is given to the system.The entities are to be classified according to their part of speech.

## Install

This project requires Python 2.7 and the following libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [gensim](https://pypi.org/project/gensim/)
- [Tensorflow](https://www.tensorflow.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [wamp server](http://www.wampserver.com/en/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included.

## Run

#### 1.Preprocessing
For the preprocessing part you need to run the entity.py code and the output is saved in the ./output/kannada_tags.txt file.The input is given from the ./data/kannda_testing.txt

You need to run the code in Python 2.7 version only.

```
python entity.py

```
#### 2.Accuracy
For the accuarcy part in a terminal or command window, navigate to the top-level project directory and run one of the following commands:

```
jupyter notebook feature-extractor.ipynb

```

```
jupyter notebook pos-tagger.ipynb

```
This will open the Jupyter Notebook software and project file in your browser.

Or you can run above files manually in jupyter notebook

First you need to execute the feature-extractor.ipynb file after that pos-tagger.ipynb

#### 1.UI Design

For the UI design part you need to load the file using wamp server.You need to run the following command in the web browser by mentioning the file name

```
localhost/UI Design/index.php
```

```
localhost/UI Design/entity_tags.html

```
## Result

| Data | Accuracy |
| --- | --- |
| Trained data | 89.202 |
| Test data | 81.954 |



