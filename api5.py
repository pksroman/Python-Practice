from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return("Hello")

@app.route('/leap_year//<int:year>')
def prime(year):
    if(year%4==0 and (year%100!=0 or year%400==0)):
	    result = {
                "year" : year,
                "leap year" : "True"
                }
    else:
	    
        result = {
                "year" : year,
                "leap year" : "False"
                }
        

    

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)