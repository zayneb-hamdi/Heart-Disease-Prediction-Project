import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from flask import Flask,render_template,request
from pymongo import mongo_client

app=Flask(__name__)
client = mongo_client.MongoClient("mongodb://localhost:27017/")
db=client["prediction_db"]
cases=db["cases"]






heart_data=pd.read_csv('heart_disease_data.csv')
"""heart_data.head()
heart_data.tail()
heart_data.shape
heart_data.info()
heart_data.isnull().sum()
heart_data.describe()
heart_data['target'].value_counts()"""

x=heart_data.drop('target',axis=1)
y=heart_data['target']
#print(x)
#print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)
#print(x.shape,x_train.shape,x_test.shape)
model=LogisticRegression()
model.fit(x_train,y_train)
x_train_prediction=model.predict(x_train)
training_data_accuracy=accuracy_score(x_train_prediction,y_train)
print("accuracy on training data: ",training_data_accuracy)
x_test_prediction=model.predict(x_test)
test_data_accuracy=accuracy_score(x_test_prediction,y_test)
print("accuracy on test data",test_data_accuracy)
#***************************************************************************************************************************************


@app.route("/")
def home():
  return render_template("index.html")

@app.route("/formulaire.html")
def formulaire():
  return render_template("formulaire.html")

@app.route("/submit",methods=["POST"])
def submit():
  age = int(request.form['age'])
  sex = int(request.form['sex'])
  cp = int(request.form['cp'])
  trestbps = int(request.form['trestbps'])
  chol = int(request.form['chol'])
  fbs = int(request.form['fbs'])
  restecg = int(request.form['restecg'])
  thalach = int(request.form['thalach'])
  exang = int(request.form['exang'])
  oldpeak = float(request.form['oldpeak'])
  slope = int(request.form['slope'])
  ca = int(request.form['ca'])
  thal = int(request.form['thal'])
  input_data = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
  input_data_as_numpy_array=np.asarray(input_data)
  input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
  prediction=model.predict(input_data_reshaped)
  print(prediction)
  if(prediction[0]==0):
    result='Good heart !'
  else:
    result='heart disease risk please check with doctor!'
  
  object ={
    "age":age,
    "sex":sex,
    "cp":cp,
    "trestbps":trestbps,
    "chol":chol,
    "fbs":fbs,
    "restecg":restecg,
    "thalach":thalach,
    "exang":exang,
    "oldpeak":oldpeak,
    "slope":slope,
    "ca":ca,
    "thal":thalach,
    "result":result,
  }
  cases.insert_one(object)
  return render_template("result.html",resultat=result)
  
  
















#*******************************************
if __name__=="__main__":
  app.run(debug=True)