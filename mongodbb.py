import pymongo
import random

uid=0
def find():
    uidd=int(input("enter the id you want to find:"))
    finded_val=row.find_one({'_id':uidd})
    print(finded_val)

def insert():
    uid=random.randint(0,100000)
    uname=input("Enter your name: ")
    uemail=input("Enter your email: ")
    public_key=input("Enter your public key: ")
    encrypt_private=input("Enter emcrpyt_private: ")
    hash_master=input("Enter your hash_master: ")
    uval={'_id':uid,'name':uname,'email':uemail,'public_key':public_key,'encrypt_private_key':encrypt_private,'hash_master_key':hash_master}
    row.insert_one(uval)

def delete():
    uidd=int(input("enter the id you want to delete: "))
    hash_master=input("Enter your hash_master to delete: ")
    row.delete_one({'_id':uidd,'hash_master_key':hash_master})

def update():
    uidd=int(input("enter the id you want to update:"))
    newname=input("")
    newemail=""
    newhash=input("Enter new hash:")
    nprivate=input("Enter new private key:")
    row.update_one({"_id":uidd},{"$set":{"name":newname,"email":newemail,"hash_master_key":newhash}})
    
if __name__== "__main__":
    client= pymongo.MongoClient("mongodb://localhost:27017/")
    db= client['userdata']
    row=db['datad']
    #uid=input("Enter your value: ")

    no=input("Enter the command:")
    if(no=="1"):
        insert()
    elif(no=="2"):
        find()
    elif(no=="3"):
        delete()
    elif(no=="4"):
        update()
    else:
        print("error 404")
