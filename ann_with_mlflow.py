# -*- coding: utf-8 -*-
"""ANN with MLflow.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_z4YEtn1rFDPA9FDlxczXCLRP5GBV3Ew
"""

import pandas as pd
import numpy as np

data= pd.read_csv('/content/diabetes[1].csv')
data

from sklearn.model_selection import train_test_split

X=data.to_numpy()[:,0:8]
y=data.to_numpy()[:,8]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
print (f'Shape of Train Data : {X_train.shape}')
print (f'Shape of Test Data : {X_test.shape}')

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model=Sequential([Dense(24,input_dim=(8),activation='relu'),Dense(12,activation='relu'),Dense(1,activation='sigmoid')])

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
model.summary()

from __future__ import barry_as_FLUFL
history=model.fit(X_train,y_train,epochs=100,batch_size=32,verbose=1)

scores=model.evaluate(X_test,y_test)
print (f'{model.metrics_names[1]} : {round(scores[1]*100, 2)} %')

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
y_pred=model.predict(X_test)

MSE=mean_squared_error(y_test,y_pred)
MAE=mean_absolute_error(y_test,y_pred)
R2=r2_score(y_test,y_pred)

import math
RMSE = math.sqrt(MSE)

print(MSE)
print(MAE)
print(R2)
print(RMSE)

!pip install -q mlflow databricks-sdk

import mlflow
mlflow.login()

tracking_uri="databricks"
MlflowClient=mlflow.client.MlflowClient
client = MlflowClient(tracking_uri=tracking_uri)

experiment_description=("This is ANN model trained on diabetes data")

experiment_tag= {
    "project_name": "diabetes",
    "dept": "Medical",
    "team" : "MED-ml",
    "Project_quarter":"Q3-2023",
    "mlflow.note.content": experiment_description
}

diabetes_experiment=client.create_experiment(name="/Users/idreeslang007@gmail.com/Diabetes_Models", tags=experiment_tag)

Diabetes_experiment=mlflow.set_experiment(experiment_name="/Users/idreeslang007@gmail.com/Diabetes_Models")
run_name ="diabetes_model"
artifact_path="/Users/idreeslang007@gmail.com/Diabetes_Models"

metrics={"MSE":MSE,"MAE":MAE,"R2":R2,"RMSE":RMSE}

for i in range(20):
  with mlflow.start_run():
    mlflow.log_metrics(metrics)
    mlflow.sklearn.log_model(sk_model=run_name, input_example=X_test, artifact_path=artifact_path)
#adding text to check the commits    
