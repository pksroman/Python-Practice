from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return("Hello")

@app.route('/factorial//<int:num>')
def factorial(num):
    fac = 1
 
    for i in range(1, num + 1):
	    fac = fac * i

    factorial = fac

    result = {
                "number" : num,
                "Factorial" : factorial
        }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)