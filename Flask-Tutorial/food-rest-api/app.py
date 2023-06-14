from flask import Flask 


app = Flask(__name__)


@app.route('/api/food/<int:id>',methods = ['GET'])
def get_food_item():
    pass


@app.route('/api/food/',methods = ['POST'])
def save_food_item():
    pass



@app.route('/api/food/<int:id>',methods = ['PUT'])
def update_food_item():
    pass


@app.route('/api/food/<int:id>',methods = ['DELETE'])
def delete_food_item():
    pass


if __name__ == '__main__':
    # create db connection..
    app.run()