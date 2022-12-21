import sys
sys.path.append('c:/users/user/appdata/local/programs/python/python38-32/lib/site-packages')
import flask
# import requests
from flask import Flask
from flask import request 
app = Flask(__name__)
import Mode
# import main


#to display the connection status
@app.route('/', methods=['GET'])
def handle_call():
    return "Successfully Connected"

#the get method. when we call this, it just return the text "Hey!! I'm the fact you got!!!"
@app.route('/gettext/<mode>&<img>', methods=['GET'])
def get_fact(mode, img):
    newtext=Mode.testing(mode, img)
    return newtext

# extract_img= request.args.get(mode)
#the post method. when we call this with a string containing a name, it will return the name with the text "I got your name"
@app.route('/getname/<name>', methods=['POST'])
def extract_name(name):
    return "I got your name "+name;

#this commands the script to run in the given port
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)