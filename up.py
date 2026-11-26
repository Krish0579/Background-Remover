from flask import Flask,render_template,request,send_file
#flask - turns python file to web server
#render_template - shows your html page on the screen
#request - catches the images the user uploads from html
#send_file: Sends the finished image back to the user
import subprocess
import sys
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('web.html')
@app.route('/upload',methods=['POST'])
def upload():
    request.files['image'].save('img.png')
    #saves uploaded image as png
    subprocess.run([sys.executable,'app.py'], check=True )
    #returns app.py directly
    return send_file('output1.png',as_attachment=True)
app.run(debug=True)