#!/usr/bin/env python
# coding: utf-8

# In[10]:


from flask import Flask, request, render_template


# In[11]:


app = Flask(__name__)


# In[12]:


from werkzeug.utils import secure_filename
import speech_recognition as sr

@app.route("/",methods = ["Get","Post"])
def index():
    if request.method == "POST":
        # READ THE FILE
        file = request.files["file"]
        print("file received")
        filename = secure_filename(file.filename) # file name
        print(filename)
        file.save("static/"+filename) # save under this directory
        
        a = sr.AudioFile("static/"+filename)
        with a as source:
            a = sr.Recognizer().record(a)
        s = sr.Recognizer().recognize_google(a)
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="2"))


# In[ ]:


if __name__ == '__main__':
    app.run()


# In[ ]:




