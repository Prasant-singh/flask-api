from flask import Flask, redirect, render_template, request
from werkzeug.utils import secure_filename
import os
import cv2

app = Flask(__name__)

upload_folder = os.path.join('static', 'uploads')
app.config['UPLOAD'] = upload_folder

if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

@app.route("/", methods=['GET', 'POST'])
def upload_file():  
    if request.method == "POST":
        file = request.files['img']
        if file.filename == '':
            return redirect(request.url)
            
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD'], filename)
        file.save(filepath)

        img = cv2.imread(filepath)
        if img is not None:
            (h, w) = img.shape[:2]
            center = (w // 2, h // 2)  
            rotate = cv2.getRotationMatrix2D(center, 90, 1.0) 
            rotated_img = cv2.warpAffine(img, rotate, (w, h)) 
            
            rotated_filename = 'rotated_' + filename
            rotated_filepath = os.path.join(app.config['UPLOAD'], rotated_filename)
            cv2.imwrite(rotated_filepath, rotated_img)
            
            return render_template("index.html", img=rotated_filepath)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)