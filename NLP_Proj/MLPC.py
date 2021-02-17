#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import re
import numpy as np
from numpy import dot
from numpy.linalg import norm
from pyspark import SparkContext
from pyspark.sql.functions import *
from pyspark.sql.types import *
import numpy as np
from pyspark.ml.linalg import SparseVector, DenseVector
from pyspark.ml.linalg import Vectors, VectorUDT
from pyspark.sql.session import SparkSession
from pyspark.sql import SQLContext


# In[2]:


sc = SparkContext(appName="Proj")
spark = SparkSession(sc)


# In[3]:



df = spark.read.json(sys.argv[1])


# In[4]:


df_full = df.drop('asin').drop('helpful').drop('reviewTime').                drop('reviewerID').drop('reviewerName').drop('summary').drop('unixReviewTime')



# In[5]:


pn_udf = udf(lambda x: 1 if x >=4 else 0, IntegerType() ) #1 for positive 0 for negative
df_full_l = df_full.withColumn('label',pn_udf('overall')).drop('overall')


# In[6]:


from pyspark.ml.feature import HashingTF,IDF,Tokenizer
dim = 20000
tokenizer = Tokenizer(inputCol = 'reviewText', outputCol = 'words')
wordsData = tokenizer.transform(df_full_l)


# In[7]:


hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=dim)
featurizedData = hashingTF.transform(wordsData)


# In[8]:


idf = IDF(inputCol="rawFeatures", outputCol="features")
idfModel = idf.fit(featurizedData)


# In[9]:


rescaledData = idfModel.transform(featurizedData)
tfifd = rescaledData.select("label", "features")


# In[10]:


df_train, df_test = tfifd.randomSplit([.6, .4])


# In[11]:


from pyspark.ml.classification import MultilayerPerceptronClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator


# In[12]:


layers = [dim, 128, 128, 2]
trainer = MultilayerPerceptronClassifier(maxIter=100, layers=layers, blockSize=128, seed=256)


# In[ ]:


model = trainer.fit(df_train)
predictions = model.transform(df_test)


# In[ ]:


result = predictions.select('label','prediction').collect()
y = []
y_pred = []

for i in result:
    y.append(i[0])
    y_pred.append(i[1])


# In[ ]:


from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
conf = confusion_matrix(y, y_pred)
print('confusion matrix is ')
print(conf)
print('accuracy is:')
print(accuracy_score(y, y_pred))
print('f1 score is:')
print(f1_score(y, y_pred))


# In[ ]:




