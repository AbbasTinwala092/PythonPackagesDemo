from flask import Flask
myApp = Flask(__name__)

@myApp.route('/')
def display():
    return "Hello World"

@myApp.route('/ContactUs')
def contactus():
    return "Hello to ContactUs"

#@myApp.route('/Admin')

if __name__ == '__main__':
    myApp.run(debug = True)




