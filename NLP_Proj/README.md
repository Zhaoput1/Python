## 777 Term Project
Part 1: Large Dataset(Amazon book reviews data 2014 9GB) binary classification with Pyspark ml lib.\
Part 2: Multi-classification problem with Pyspark Pipeline and BERT\
By Zhaopu Teng
(I have a report file, in which will explain what I did in this project.)

## Describe here your project


For the part 1, I get the dataset from https://www.kaggle.com/jmourad100/amazon-product-reviews-data-5core-2014?select=Books_5.json.\
In this dataset, we have reviews and score from 1 to 5. I define the score of 4, 5 is positive, and define them as class 1, while for score 1, 2, 3 is negative, and
I define them as class 0. Then I use three algorithm to simulate the model, Logistic Regression, SVM, and Multilayer Perceptron Classifier.

For the part 2, I use a sparknlp api to achieve the BERT model used on spark. Special environment is needed. We define the model and stages ourselves and go through
a Pyspark Pipeline. It is a very time consuming work and totally new knowledge, I can only implement it on medium dataset. Also it is somehow not compatible with 
Google clusters. To be continue, I can work on how to implement this algorithm on large dataset.


# Submit your python scripts .py 

If your assignment has 3 tasks you need to commit the 3 scripts only and overwrite them. You can then delete the script number 4 ( main_task4.py 
)

If your assignment has 4 tasks then you can use all of them. 

# Other Documents. 

Since the MLPC only can be run on the Google cloud, so I get a output screenshot to show the reslut.


# How to run  




```python

For LogisticRegression.py, just submit and run will be OK.

```



```python

For SVM.py, just submit and run will be OK.

```



```python

For MLPC.py, it is not possible to run it on labtop. It takes more than 12 hours to run it on Google Cloud. You can shrink the dataset to test it.

```


```python

For bbc_BERT.py, a particular environment is needed. In my case, I use it on Colab with pyspark==2.4.7, spark-nlp==2.5.0. Using a different version of the two
packages may cause errors.

```


```python

For ag_BERT.py, a particular environment is needed. In my case, I use it on Colab with pyspark==2.4.7, spark-nlp==2.6.4. Using a different version of the two
packages may cause errors.

```


```python

For LR_Compare.ipynb, it is to compare with the result given by af_BERT.py.

```








