from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# your program here
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:power@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# your program here

class Person(db.Model):
    __tablename__='persons' #to specify name of table
    id=db.Column(db.Integer,primary_key=True) #it automatically sets auto increment o this
    name=db.Column(db.String(),nullable=False)

    #this helps when accessing the object from another file
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'
@app.route('/')
def index():
    person=Person.query.first()
    return "Hello "+person.name

db.create_all()
#always include this at the bottom of your code
if __name__ == '__main__':
   app.run(host="0.0.0.0",debug=True)