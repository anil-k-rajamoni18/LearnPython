from flask import Flask

#create app object
app = Flask(__name__)


@app.route("/")
def greet():
    return 'Hey Hi Am learning Flask...'

@app.route("/info")
def person_info():
    data = {"id" : 101 ,"name" : "Fenil" ,"course" : "Python" , "fee" : 800,"isCompleted": False}
    return data

if __name__ == '__main__':
    app.run(debug= True)