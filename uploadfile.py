from flask import Flask, request
from flask import render_template
import boto3


app = Flask(__name__)


@app.route('/')
def renderUploadPage():
    return  render_template('UploadFile.html')



@app.route('/upload', methods = ['GET','POST'])
def uploadfile():
    s3 = boto3.resource('s3')
    f = request.files['file']
    s3.Bucket('firstfileuploadbkt').put_object(Key= f.filename , Body = request.files['file'])
    return "File saved to S3"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')  
