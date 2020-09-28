from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'

@app.route('/')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully to pigeonvideo!'
		
if __name__ == '__main__':
   app.run(debug = False)
   app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER