from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.oracle import BLOB,DATE


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, autoincrement=True)
    username = db.Column(db.String(50),unique=True, nullable=False,primary_key=True)
    password = db.Column(db.String(15),nullable=False)
    type = db.Column(db.String(15),nullable=False)

    def __init__(self,username,password,type):
        self.username=username
        self.password=password
        self.type=type
class Admin(db.Model):
    __tablename__ = 'Admin'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    admin_id=db.column(db.Integer)
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)

    def __init__(self,usr_name,fname,lname,phone,mail,admin_id):
        self.usr_name=usr_name
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.mail=mail
        self.admin_id=admin_id 
        
class Authority(db.Model):
    __tablename__ = 'Authority'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    mail = db.Column(db.String(50))
    job = db.Column(db.String(50))
    proof=db.Column(db.BLOB)
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)
    

    def __init__(self,usr_name,fname,lname,phone,mail,job,proof):
        self.usr_name=usr_name
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.mail=mail
        self.job=job
        self.proof=proof    

class Ordinary(db.Model):
    __tablename__ = 'Ordinary'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    phone = db.Column(db.Integer)
    mail = db.Column(db.String(20))
    state = db.Column(db.String(20))
    city = db.Column(db.String(20))
    proof=db.Column(db.BLOB)
    address=db.Column(db.String(50))
    zip = db.Column(db.Integer)
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)
    

    def __init__(self,usr_name,fname,lname,phone,mail,state,city,address,zip,proof):
        self.usr_name=usr_name
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.mail=mail
        self.job=job
        self.proof=proof    
        self.state=state
        self.city=city
        self.zip=zip


class Other(db.Model):
    __tablename__ = 'Other'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    admin_approval = db.Column(db.String(5))
    admin_id =  db.Column(db.Integer)
    no_of_video_upload = db.Column(db.Integer)
    no_of_video_request = db.Column(db.Integer)
    third_party_issue_id = db.Column(db.Integer)
    third_party_pending_order = db.Column(db.String(10))
    Third_party_response = db.Column(db.String(20))  #video not available or available
    date= db.Column(DATE)
    start_time = db.Column(db.Integer)
    end_time = db.Column(db.Integer)
    live_recording_no=db.Column(db.Integer)
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)
    

    def __init__(self,admin_approval,admin_id,no_of_video_upload,no_of_video_request,third_party_issue_id,third_party_pending_order,Third_party_response,date,start_time,end_time,usr_name):
        self.admin_approval=admin_approval
        self.admin_id=admin_id
        self.no_of_video_request=no_of_video_upload
        self.third_party_issue_id=third_party_issue_id
        self.third_party_pending_order=third_party_pending_order
        self.Third_party_response=Third_party_response
        self.date=date    
        self.start_time=start_time
        self.end_time=end_time
        self.live_recording_no=live_recording_no
        self.usr_name=usr_name

class Third(db.Model):
    __tablename__ = 'Third'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    dept = db.Column(db.String(50))
    name = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    Third_party_id = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    usr_name = db.Column(db.String, db.ForeignKey('User.username'),nullable=False)

    def __init__(self,usr_name,dept,name,mail,third_party_id,phone):
        self.usr_name=usr_name
        self.dept=dept
        self.name=name
        self.phone=phone
        self.mail=mail
        self.third_party_id=third_party_id
        








    

@app.route('/thirdparty')
def  dashboard():
    n=8
    return render_template('thirddashboard.html',n=n)





if(__name__ == "__main__"):
    db.create_all()
    app.run(debug=True)
    
