from flask import Flask, render_template, request, url_for, flash, redirect




app = Flask(__name__,static_folder='assets')
app.config["CACHE_TYPE"] = "null"
app.config['TESTING']    = True
app.testing = True
app.config['SECRET_KEY'] = 'b1808f24613321f9007f0e8b31759bc269e8fc6a6a2fb51d'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
