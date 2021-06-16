import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pyspark
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

import time
print("-- REGRESOR --")




from sklearn.datasets import load_boston
X, y = load_boston(return_X_y=True)
print("tipo de X = ",type(X))
print("tipo de y = ",type(y))

#Create PySpark SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("REGRESOR") \
    .getOrCreate()
#Create PySpark DataFrame from Pandas

sparkDF=spark.createDataFrame(pd.DataFrame(X))
sparkDF.printSchema()
sparkDF.show()

sparkDF=spark.createDataFrame(pd.DataFrame(y))
sparkDF.printSchema()
sparkDF.show()

