
from doctest import master
from flask import Flask, request, render_template
import pymongo
import random

app = Flask(__name__)

nam3=[]
#uidd=0
@app.route('/', methods =["GET", "POST"])
def gfg():
 if request.method == "POST":
  fullname=request.form.get("nam")
  email=request.form.get("eml")
  public_key1=request.form.get("pk")
  encrypt_private_key=request.form.get("epk")
  masterkeyhash=request.form.get("mk")
    #-----------------------------------------
  insert(fullname,email,public_key1,encrypt_private_key,masterkeyhash)
 return render_template("userdatafiles/index.html")
#--------------------------------------------
def insert(fullname,email,public_key1,encrypt_private_key,masterkeyhash):
    uid=random.randint(0,100000)
    uname=fullname
    uemail=email
    public_key=public_key1
    encrypt_private=encrypt_private_key
    hash_master=masterkeyhash
    uval={'_id':uid,'name':uname,'email':uemail,'public_key':public_key,'encrypt_private_key':encrypt_private,'hash_master_key':hash_master}
    row.insert_one(uval)
    #-------------------------------------------
    return render_template("userdatafiles/index.html")

#--------------------------------------------------------
@app.route('/dele', methods =["GET", "POST"])
def delpage():
    if request.method == "POST":
     uidd=request.form.get("uid")
     hash_master=request.form.get("mk")
     delete(uidd,hash_master)
    return render_template('userdatafiles/dele.html')

def delete(uidd,hash_master):
    uidd1=0
    hash_master1=""

    uidd1=int(uidd)
    hash_master1=hash_master

    print(type(uidd1))
    print(type(hash_master1))

    row.delete_one({'_id':uidd1,'hash_master_key':hash_master1})

@app.route('/update', methods =["GET", "POST"])
def updatepage():
    if request.method == "POST":
     uidd=request.form.get('uid')
     fullname=request.form.get("nam")
     email=request.form.get("eml")
     masterkeyhash=request.form.get("mk")
     update(uidd,fullname,email,masterkeyhash)
    return render_template('userdatafiles/update.html')
def update(uidd,fullname,email,masterkeyhash):
    uidd1=int(uidd)
    newname=fullname
    newemail=email
    newhash=masterkeyhash
    row.update_one({"_id":uidd1},{"$set":{"name":newname,"email":newemail,"hash_master_key":newhash}})

if __name__=='__main__':
 client= pymongo.MongoClient("mongodb://localhost:27017/")
 db= client['userdata']
 row=db['datad']
 app.run(use_reloader = True,debug=True)
 
