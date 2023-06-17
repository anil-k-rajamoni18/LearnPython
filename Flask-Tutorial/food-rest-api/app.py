from flask import Flask,request
from db.MongoUtils import MongoDBConnection


mycoll =  MongoDBConnection('rocketRecipeDB','food-items','mongodb://localhost:27017/').create_connection()

app = Flask(__name__)


env = {
    'name' : 'rocket recipe microservice',
    'version': 'V1.0'
}

@app.route('/')
def greet():
    return f"{env['name']} is UP & RUNNING with version : {env['version']}"

@app.route('/api/food/<int:id>',methods = ['GET'])
def get_food_item(id):
    if mycoll is not None:
        data = mycoll.find()
        return data


@app.route('/api/foods/',methods = ['GET'])
def get_food_items():
    pass


@app.route('/api/food/',methods = ['POST'])
def save_food_item():
    if mycoll is not None:
        data = request.json
        response = mycoll.insert_one(data)
        return f' data inserted successfully {response.acknowledged} {response.inserted_id}'
    return f'Service is not avaiable....'

@app.route('/api/foods/',methods = ['POST'])
def save_food_items():
    pass

@app.route('/api/food/<int:id>',methods = ['PUT'])
def update_food_item():
    pass


@app.route('/api/food/<int:id>',methods = ['DELETE'])
def delete_food_item():
    pass


if __name__ == '__main__':
    # create db connection..
    app.run(debug=True)