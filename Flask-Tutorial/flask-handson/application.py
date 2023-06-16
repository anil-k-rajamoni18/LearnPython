from flask import Flask , render_template

# create a flask app object 

app = Flask(__name__)



students = [{
    'name': "fenil",
    'course': 'python',
    'level': 3,
    'isStudent':True,
    'skills' : ['python','IOT']
},
{
    'name': "sowmya",
    'course': 'python',
    'level': 3,
    'isStudent':True,
    'skills' : ['python','java','c']
},
]

# creates routes with decorates.
@app.route('/')
def home():
    return render_template('home.html',data = 'Hello Welcome to my Web-APP')

@app.route('/students')
def students_data():
    #return {'data': students}
    return render_template('students.html',students = students)

@app.route('/students/<name>')
def get_student(name):
    print(name)

    for student in students:
        if name in student['name']:
            return student    
    else:
        return {'data': f'student with name {name} not found..'}
 


if __name__ == '__main__':
    app.run(debug=True)