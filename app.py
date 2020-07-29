import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template,send_from_directory
import pickle
import time
import os.path
from os import path
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)


# imporing model and scalar object 
MODEL= 'my_model.pkl'
model = pickle.load(open(f'./models/{MODEL}','rb'))
SCALAR= 'transformer.pkl'
sc = pickle.load(open(f'./models/{SCALAR}','rb'))
UPLOAD_FOLDER = 'uploads'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict( sc.transform(final_features))

    if prediction == 1:
        pred = "You have Diabetes, please consult a Doctor."
    elif prediction == 0:
        pred = "You don't have Diabetes."
    output = pred

    return render_template('index.html', prediction_text='{}'.format(output))

@app.route('/download',methods=['POST','GET'])
def upload():
    try:
        if request.method == 'POST':
        # Get the file from post request
            f = request.files['file']

            # Save the file to ./uploads
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
            f.save(file_path)
            test_df = pd.read_csv(file_path)
            pred= model.predict(sc.transform(test_df))
            test_df['pred']= pred
            #checking for previous prediction file
            if path.exists('./downloads/prediction.csv'):
                os.remove('./downloads/prediction.csv')
                print('previous prediction file removed from path')
            else:
                pass
            test_df.to_csv('./downloads/prediction.csv')

            return send_from_directory('./downloads/','prediction.csv',as_attachment=True,  cache_timeout=0)
    finally:
        upload_file = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        time.sleep(2)
        os.remove(upload_file)
        print('clean up done')

if __name__ == "__main__":
    app.run(debug=True)
