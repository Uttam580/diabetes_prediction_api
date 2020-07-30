

![GitHub repo size](https://img.shields.io/github/repo-size/Uttam580/diabetes_prediction_api?style=plastic)
![GitHub language count](https://img.shields.io/github/languages/count/Uttam580/diabetes_prediction_api?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/Uttam580/diabetes_prediction_api?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/Uttam580/diabetes_prediction_api?color=red&style=plastic)


Medium Blog: 

<a href ="https://medium.com/@uttam94/diabetes-prediction-c6b3dca0a2b5"> <img src="https://github.com/Uttam580/Uttam580/blob/master/img/medium.png" width=60 height=30>

# Diabetes_prediction

In this project, the objective is to predict whether the person has Diabetes or not based on various features like Glucose level, Insulin, Age, BMI. We will use the Pima Indians dataset from the UCI Machine learning repository.

**quick demo**

![demo_gif](https://github.com/Uttam580/diabetes_prediction_api/blob/master/demo.gif)

we can predict diabetes from two ways.

1. User will fill the data after that prediction will be displayed over UI.

2. User can upload csv file with required features and then get downloadable predicted csv  file.

   Below is screenshot for sample csv, while bulk prediction same features column sequence needs to be maintained in uploading file.

   <img src = "https://miro.medium.com/max/855/1*_JQuyFFixYC5f5w2RiJX0g.png">


**Description of variables in the dataset:**

```Pregnancies:``` Number of times pregnant

```Glucose:``` Plasma glucose concentration a 2 hours in an oral glucose tolerance test

```BloodPressure:``` Diastolic blood pressure (mm Hg)

```SkinThickness:```Triceps skin fold thickness (mm)

```Insulin:``` 2-Hour serum insulin (mu U/ml)

```BMI:``` Body mass index (weight in kg/(height in m)²)

```DiabetesPedigreeFunction:``` Diabetes pedigree function

```Age:``` Age (years)

```Outcome:``` Class variable (0 or 1)

**Diabetes-Prediction directory tree**

```
├─ app.py
├─ demo.gif
├─ downloads
│  └─ prediction.csv
├─ LICENSE
├─ models
│  ├─ model.py
│  ├─ my_model.pkl
│  ├─ predict.py
│  └─ transformer.pkl
├─ procfile
├─ README.md
├─ requirements.txt
├─ src
│  └─ diabetes.csv
├─ static
│  └─ css
│     ├─ grid.css
│     ├─ images
│     │  └─ dia.jpeg
│     └─ style.css
├─ templates
│  └─ index.html
└─ uploads
   └─ test.csv

```

```app.py``` : Front and back end portion of the web application

```downloads``` : conatains predcited csv file(based on uploaded file)

```models```  : contains model for prediction

```requirements.txt``` : required library 

```src```  : conatins raw data file 

```static``` : contains static file (css, img) for UI

```templates``` : contains templates for UI

```uploads``` : uploded csv file will store  here  after that it will used for prediction(added test file for sample)


## Installation

* Clone this repository and unzip it.

* create new env with python 3 and activate it .

* Install the required packages using pip install -r requirements.txt

* Execute the command: python app.py

* Open ```http://127.0.0.1:5000/``` in your browser.

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) 

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
