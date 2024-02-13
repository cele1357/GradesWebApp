from flask import Flask, render_template, json, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.sqlite"
db = SQLAlchemy(app)

class Student(db.Model): #db is a table
    #attributes
    id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String, unique=False, nullable=False)
    Grade = db.Column(db.String, unique=False, nullable=False)
    #constructor, dont need bc Student inherits from a parent class which already has a constructor
    # def __init__(self, Name, Grade):
    #     self.Name = Name
    #     self.Grade = Grade
    def __repr__(self):
        return 'Student(' + self.Name + ',' + self.Grade + ')'

with app.app_context():
        db.create_all()

if __name__ =="__grades__":
    app.run()

@app.route('/')
def index():
    return render_template('grades.html')


@app.route('/grades', methods = ['GET'])
def get_Grades():
    #this is a list of student objects [Student(hguyh,98), Student(hgj,099)]
    student_list = Student.query.all()
    dictionary = {}
    for i in student_list:
        dictionary.update({i.Name : i.Grade})    

    return dictionary


@app.route('/grades', methods = ['POST'])
def create_New(): #add data
    #gets the input, get the values of the keys to put in variables
    request_json = request.get_json()
    studentName = request_json['name']
    studentGrade = request_json['grade']

    new = Student(Name=studentName, Grade=studentGrade)
    db.session.add(new) 
    db.session.commit()
    return request_json
       
@app.route('/grades/<name>', methods = ['GET'])
def get_Grade(name):  
    Stu = Student.query.filter_by(Name=name).first()
    dictionary = {}
    dictionary.update({Stu.Name : Stu.Grade})    

    return dictionary


@app.route('/grades/<name>', methods = ['PUT'])
def edit_Grade(name):
    request_json = request.get_json()
    #studentName = request_json['name']
    studentGrade = request_json['grade']

    Stu = Student.query.filter_by(Name=name).first()

    Stu.Grade = studentGrade
    db.session.commit()
    
    dictionary = {}
    dictionary.update({Stu.Name : Stu.Grade})    

    return dictionary
    
@app.route('/grades/<name>', methods = ['DELETE'])
def delete_Grade(name):
    
    studentName = name

    Stu = Student.query.filter_by(Name=studentName).first()

    db.session.delete(Stu)
    db.session.commit()
    return get_Grades()   