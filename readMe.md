#RUN APP

$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
. venv/bin/activate
pip install Flask
pip install -q -U keras-tuner
pip install pandas
pip install sklearn
pip install tensorflow
pip install lime
pip install 


##Run in debug mode
export FLASK_DEBUG=1
flask run  --debugger
#in docker
docker run -i -t -p 5000:5000 --name python-server -v ~/Desktop/www:/app/www python:latest
flask run --host=0.0.0.0
####in app.py
 app.config['TEMPLATES_AUTO_RELOAD'] = True 
