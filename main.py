from flask import Flask,render_template,request
from speech_recognisation import assistant
import pytesseract
import os


app=Flask(__name__,static_folder="history")
APP_ROOT=os.path.dirname(os.path.abspath(__file__))


@app.route('/',methods=['GET'])
def homepage():
    return render_template('upload.html')
@app.route('/complete',methods=['POST'])

def upload():
    if request.method == 'POST':
        upload.voice_text=request.form['voices']
        upload.gender=request.form['voices']
        tar=os.path.join(APP_ROOT,'history/')
        print(tar)
        if not os.path.isdir(tar):
            os.mkdir(tar)
        for file in request.files.getlist('file'):
            filename=file.filename
            destination="/".join([tar,filename])
            file.save(destination)
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        upload.text = pytesseract.image_to_string(destination)
        print(upload.text)
        return render_template("complete.html",img_name=filename,message=upload.text)
    else:
        return "Something Went Wrong"

@app.route('/speak',methods=['POST'])
def speak():
    if request.method=='POST':
        texts=upload.text
        texxt_to_speak=upload.voice_text
        assistant(texts,texxt_to_speak)
        return render_template('complete.html')


if __name__=='__main__':
    app.run(debug=True)