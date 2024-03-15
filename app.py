from flask import *  ##$$ Flask is the prototype used to create instances of web application
import os
from werkzeug.utils import secure_filename ##Pass it a filename and it will return a secure version of it 
import label_image                ## This filename can then safely be stored on a regular file system and passed to os. path.

def load_image(image):
    text = label_image.main(image)
    return text

app = Flask(__name__)
@app.route('/')

@app.route('/first')
def first():
    return render_template('first.html')

    
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)
        # Make prediction
        result = load_image(file_path)
        result = result.title()
        d = {"brownspot":" → You are Normal",
	    'Normal':" → You are Normal",
        "Severe":" → Affected ",
        "Stage1":" → Condition at stage 1",
        "Stage2":" → Condition at stage 2"}
        result = result+d[result]
        #result2 = result+d[result]
        #result = [result]
        #result3 = d[result]        
        print(result)
        #print(result3)
        os.remove(file_path)
        return result
        #return result3
    return None

if __name__ == '__main__':
    app.run()