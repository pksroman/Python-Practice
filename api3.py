from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return("Hello")

@app.route('/armstrong//<int:num>')
def armstrong(num):
    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        
        result = {
                "number" : num,
                "Armstrong" : 'True'
        }
    else:
        
        result = {
                "number" : num,
                "armstrong" : 'False'
        }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)