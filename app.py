
from flask import Flask, render_template, request, url_for, flash, redirect
import numpy as np
from regression import *
import math 







app = Flask(__name__,static_folder='assets')
app.config["CACHE_TYPE"] = "null"
app.config['TESTING']    = True
app.testing = True
app.config['SECRET_KEY'] = 'b1808f24613321f9007f0e8b31759bc269e8fc6a6a2fb51d'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

select_model = Training()


# csv_data= pd.read_csv('./data/dataset_pre_processed.csv',header=0)


# headers = csv_data.columns[0:16]

##Run Training


input_array = []
@app.route('/', methods=('GET', 'POST') )
def index():
    if request.method == 'POST':

        yarn_count = float(request.form['yarn_count'])
        density    = float(request.form['density-data'])
        width      = float(request.form['width-data'])
        shade      = request.form['shade-data']
        white      = 0
        light      = 1
        medium     = 0
        dark       = 0
        extra_dark = 0
        black      = 0
        diameter   = float(request.form['diameter-data'])
        gauge      = float(request.form['gauge-data'])
        feeders    = float(request.form['feeders-data'])
        needles    = float(request.form['needles-data'])
        rpm        = float(request.form['rpm-data'])
        shrinkage_length = float(request.form['shrinkage_length-data'])
        shrinkage_width  = float(request.form['shrinkage_width-data'])
        input_array = [yarn_count, density, width,white, light, medium, dark, extra_dark, black, diameter, gauge, needles, feeders, rpm, shrinkage_length,shrinkage_width]
        print('-----from frontend------')
        new_ar = np.array(input_array)
        new_ar = new_ar.astype(np.float64)
        arr_2d       = np.reshape(new_ar,[1,16])
        print(arr_2d)
        stitch_length = float(predict(select_model,arr_2d))
        


        #Pass model
        
        return render_template('index.html', prediction_output = stitch_length,
                                             tightness_factor = math.sqrt(yarn_count)/(stitch_length*10))

    return render_template('index.html', prediction_output="")
