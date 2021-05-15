import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
import pyspark
from pyspark.sql import SparkSession
import time
print("-- REGRESOR --")


iris_data = datasets.load_iris()
df_iris = pd.DataFrame(iris_data.data,columns=iris_data.feature_names)
df_iris['target'] = pd.Series(iris_data.target)
print(df_iris.head())
etiquetas = df_iris['target'].unique()
print(etiquetas)


#Create PySpark SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("REGRESOR") \
    .getOrCreate()
#Create PySpark DataFrame from Pandas
sparkDF=spark.createDataFrame(df_iris)
sparkDF.printSchema()
sparkDF.show()


from pyspark.ml import Pipeline
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
