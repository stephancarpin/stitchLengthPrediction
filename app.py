
from unittest import case
from flask import Flask, render_template, request, url_for, flash, redirect
import numpy as np
from regression import *
import math 
import os
#os.remove("./assets/images/lime_report.jpg")


app = Flask(__name__,static_folder='assets')
app.config["CACHE_TYPE"] = "null"
app.config['TESTING']    = True
app.testing = True
app.config['SECRET_KEY'] = 'b1808f24613321f9007f0e8b31759bc269e8fc6a6a2fb51d'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True




# csv_data= pd.read_csv('./data/dataset_pre_processed.csv',header=0)


# headers = csv_data.columns[0:16]

##Run Training


input_array = []
@app.route('/', methods=('GET', 'POST') )
def index():
    if request.method == 'POST':
        shade_encoded = 0

        


        yarn_count = 590.5/float(request.form['yarn_count'])
        density    = float(request.form['density-data'])
        width      = float(request.form['width-data'])
        #Encoding for shade label encoded
        shade      = request.form['shade-data']
        if(shade == 'white'):
            shade_encoded = 5
        if(shade == 'light'):
            shade_encoded = 3
        if(shade == 'medium'):
            shade_encoded = 4
        if(shade == 'dark'):
            shade_encoded = 1
        if(shade == 'extra_dark'):
            shade_encoded = 2
        if(shade == 'black'):
            shade_encoded = 0


        
       
        diameter   = float(request.form['diameter-data'])
        gauge      = float(request.form['gauge-data'])
        feeders    = float(request.form['feeders-data'])
        needles    = float(request.form['needles-data'])
        rpm        = float(request.form['rpm-data'])
        shrinkage_length = float(request.form['shrinkage_length-data'])
        shrinkage_width  = float(request.form['shrinkage_width-data'])

        #create array from input flask
        input_array   = [yarn_count, density, width,shade_encoded, diameter, gauge, needles, feeders, rpm, shrinkage_length,shrinkage_width]
      
        input_array_to_numpy               = np.array(input_array)
        input_array_to_numpy_float         = input_array_to_numpy.astype(np.float64)
        input_array_to_numpy_float_reshape = np.reshape(input_array_to_numpy_float,[1,11])
        print(input_array_to_numpy_float_reshape)


        columns_input = ['count', 'density', 'width','shade', 'diameter', 'gauge', 'needles', 'feeders', 'rpm', 'shrinkage_length', 'shrinkage_width']
        df=pd.DataFrame(data = input_array_to_numpy_float_reshape,columns=columns_input)
        

        scale_input_arr          = scaler.transform(df)
        print('------------ scale input----------')
        print(scale_input_arr)

# 
        #Output from prediction function
        stitch_length = float(predict(scale_input_arr))
        tightness_factor= math.sqrt(yarn_count)/(stitch_length*10)
        #Pass model
        
        return render_template('index.html', prediction_output = '%.4f'%(stitch_length * 100),
                                             tightness_factor  = round(tightness_factor,2),
                                             LFA  = int(stitch_length * needles * 2))

    return render_template('index.html', prediction_output="")


