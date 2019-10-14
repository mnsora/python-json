from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # as usual, use request to get the uploaded file, 'file' is because the input name="file"
    file = request.files['file']
    # open the file, using the filename, and load it as json
    data = json.load(open(file.filename))
    # return json as string
    return json.dumps(data)

if __name__ == '__main__':
   app.run()