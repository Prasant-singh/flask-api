from flask import Flask,redirect,render_template,request,flash,url_for
from werkzeug.utils import secure_filename
import os

app=Flask(__name__)
app.secret_key = 'your_super_secret_key_here'
upload_floder=os.path.join('static','uploads')
app.config["UPLOAD"]=upload_floder


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/",methods=["POST"])
def upload_video():
    if request.method=="POST":
        file=request.files['file']
        if file.filename=="":
            flash("No file uploaded")
            return redirect(request.url)
        
        else:
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD"], filename))
            flash("Video successffully uploaded")

            return render_template("index.html",filename=filename)
        

@app.route('/display/<filename>')
def display_video(filename):

	return redirect(url_for('static', filename='uploads/' + filename), code=301)


















if __name__=="__main__":
    app.run(debug=True)