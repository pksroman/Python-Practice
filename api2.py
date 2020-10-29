from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return("Hello")

@app.route('//<int:num>')
def even_or_odd(num):
    if num%2 == 0:
        
        result = {
                "number" : num,
                "even or odd" : 'even'
        }
        
    else:
        
        result = {
                "number" : num,
                "even or odd" : 'odd'
        }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
        

