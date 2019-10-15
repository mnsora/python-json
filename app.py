from flask import Flask, render_template, request
import json
import os

UPLOAD_FOLDER = './files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/db/uploadjson')
def uploadjson():
    alldatas = get_all_data()
    return render_template('upload.html',alldatas=alldatas)

@app.route('/upload', methods=['POST'])
def upload():  

     # as usual, use request to get the uploaded file, 'file' is because the input name="file"
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # open the file, using the filename, and load it as json
    data = json.load(open('./files/'+file.filename))
    # return json as string
    return json.dumps(data)

if __name__ == '__main__':
   app.run()
