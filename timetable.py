from flask import Flask, request, jsonify ,Response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from flask import *
import json

#Init timetable
timetable = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
timetable.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir,'db.sqlite')
timetable.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# Init db 
db = SQLAlchemy(timetable)
# Init ma
ma = Marshmallow(timetable)


# timetable class/model
class Week(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    A = db.Column(db.String(100),unique=True)
    B = db.Column(db.String(100),unique=True)
    C = db.Column(db.String(100),unique=True)
    D = db.Column(db.String(100),unique=True)
    E = db.Column(db.String(100),unique=True)
    F = db.Column(db.String(100),unique=True)
    G = db.Column(db.String(100),unique=True)


    def __init__(self,A,B,C,D,E,F,G):
        self.A= A
        self.B= B
        self.C= C
        self.D= D
        self.E= E
        self.F= F
        self.G= G
        self.Monday={self.A:'8-9',self.F:'9-10',self.D:'10:15-11:15',self.B:'11:15-12:15'}
        self.Tuesday={self.B:'8-9',self.G:'9-10',self.E:'10:15-11:15',self.C:'11:15-12:15'}
        self.Wednesday={self.C:'8-9',self.A:'9-10',self.F:'10:15-11:15',self.D:'11:15-12:15'}
        self.Thursday={self.D:'8-9',self.B:'9-10',self.G:'10:15-11:15',self.E:'11:15-12:15'}
        self.Friday={self.E:'8-9',self.C:'9-10',self.A:'10:15-11:15',self.F:'11:15-12:15'}

    def __iter__(self) :
        yield 5
        for i in [self.Monday,self.Tuesday,self.Wednesday,self.Thursday,self.Friday] :
            yield i 
    
    def __len__(self) :
        return 5
    

#week schema
class WeekSchema(ma.Schema):
    class Meta:
        fields=('A', 'B', 'C', 'D', 'E', 'F', 'G')

#init schema
week_schema = WeekSchema(many=True)      
# Enter the Slots
@timetable.route('/subject', methods=['POST'])
def add_subject():
    A= request.json['A']
    B= request.json['B']
    C= request.json['C']
    D= request.json['D']
    E= request.json['E']
    F= request.json['F']
    G= request.json['G']

    global subject 
    subject= Week(A,B,C,D,E,F,G)
    try :
        db.session.add(subject)
        db.session.commit()
        return jsonify(dict3)
        #return week_schema.jsonify(subject)
    except :
        dict3 = ParseClass(subject)
        return jsonify(dict3)
        #return jsonify({'error':'UniqueIDError'})

def ParseClass(W) :
    ans = {}
    A_ = [W.Monday,W.Tuesday,W.Wednesday,W.Thursday,W.Friday    ]
    for i in range(len(A_)) :
        ans[i] = A_[i]
    return ans 

#Get All time
@timetable.route('/subject', methods=['GET'])
def get_subjects():
    global subject
    ob=subject
    assert type(ob) == Week
    dict3 = ParseClass(ob)

    dict1={'Mon':ob.Monday,'Tue':ob.Tuesday,'Wed':ob.Wednesday,'Thu':ob.Thursday,'Fri':ob.Friday}
    dict2 = {'a':'b','c':'d','e':'f'}
    return jsonify(dict3)

if __name__ == "__main__":
    timetable.run(debug=True)

