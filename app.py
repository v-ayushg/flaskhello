from flask import Flask, jsonify, request 

app = Flask(__name__) 


 
@app.route('/')
def hello():
    return "I am Flask hello world, try /hello"


@app.route('/django')
def django():
    return "I am not django"

@app.route('/pankaj')
def pankaj():
    return "I am Pankaj."
	

@app.route('/hello', methods=['GET']) 
def helloworld(): 
	if(request.method == 'GET'): 
		data = {"data": "Hello World"} 
		return jsonify(data) 


if __name__ == '__main__': 
	app.run(debug=True) 
