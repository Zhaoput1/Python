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
from operator import add


# In[2]:


File = 'Books_5.json'
df = spark.read.json(File)


# In[3]:


df_full = df.drop('asin').drop('helpful').drop('reviewTime').                drop('reviewerID').drop('reviewerName').drop('summary').drop('unixReviewTime')


# In[4]:


# df_big, df_small = df_full.randomSplit([.9999, .0001])


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


df_train, df_test = tfifd.randomSplit([.7, .3])


# In[11]:


from pyspark.ml.classification import LinearSVC


lsvc = LinearSVC(maxIter=100, regParam=0.1)

model = lsvc.fit(df_train)
predictions = model.transform(df_test)


# In[12]:


result = predictions.select('label','prediction').collect()
y = []
y_pred = []

for i in result:
    y.append(i[0])
    y_pred.append(i[1])


# In[13]:


from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
conf = confusion_matrix(y, y_pred)
print('confusion matrix is ')
print(conf)
print('accuracy is:')
print(accuracy_score(y, y_pred))
print('f1 score is:')
print(f1_score(y, y_pred))


# In[ ]:




