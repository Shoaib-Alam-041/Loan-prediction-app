# -*- coding: utf-8 -*-
"""Loan Status Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CU7D29KDVPqlwUoNoHjFH4w_MSUApRzw
"""

import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

data=pd.read_csv("/content/data.csv")

# checking the type of data
type(data)

# Printing the first 5 Rows
data.head()

# Number of rows and columns
data.shape

# Statistical measures
data.describe()

# Numbers of Empty values
data.isnull().sum()

# dropping null values
data = data.dropna()

data.isnull().sum()

# Label encoding
data.replace({"Loan_Status": {"N":0,"Y":1}},inplace=True)

data.head()

# dependents column values
data.Dependents.value_counts()

# replace the '3+' to 4
data = data.replace(to_replace="3+",value=4)

data.Dependents.value_counts()

"""# **Data Visualization**

---
"""

# Relationship between education and loan_status
sns.countplot(x='Education',hue='Loan_Status',data=data)

# Relationship between marital status and loan_status
sns.countplot(x='Married',hue='Loan_Status',data=data)

# Relationship between Self_Employed  and loan_status
sns.countplot(x='Self_Employed',hue='Loan_Status',data=data)

"""# **Encoding**

---


"""

data.replace({'Married':{'Yes':1,'No':0},'Gender':{'Male':1, "Female":0},'Self_Employed':{'Yes':1,'No':0},'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},
              'Education':{'Graduate':1,"Not Graduate":0}},inplace=True)

data.sample()

# seprating data into x and y
X = data.drop(columns=["Loan_ID","Loan_Status"],axis=1)
Y = data["Loan_Status"]

print(X)
print(Y)

"""**Train Test Split**

---


"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.1, stratify=Y,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

"""**Training the Model (Support Vector Machines)**

---


"""

classifier = svm.SVC(kernel='linear')

# training the svm
classifier.fit(X_train,Y_train)

"""**Model Evaluation**

---


"""

# accuracy score on training data
x_train_prediction = classifier.predict(X_train)
training_data_accuracy= accuracy_score(x_train_prediction,Y_train)

print(f"Accuracy on training data : {training_data_accuracy}")

# accuracy score on training data
x_test_prediction = classifier.predict(X_test)
testing_data_accuracy= accuracy_score(x_test_prediction,Y_test)

print(f"Accuracy on testing data : {testing_data_accuracy}")

"""**Predictive System**"""

input_data = (1,0,0,1,0,4583,1508.0,128.0,360.0,1,2)

# Convert the input data to a DataFrame
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = classifier.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
  print('Loan Approval Prediction : No')
else:
  print('Loan Approval Prediction : Yes')