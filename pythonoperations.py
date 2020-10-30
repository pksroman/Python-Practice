from flask import Flask, jsonify, request
app = Flask(__name__)

database = [ 
    {"name" : "prabhakar",
    "reg_no" : "0",
   "branch"  : "mechanical",
    "college" : "dr.ait"},

    {"name" : "manosh",
    "reg_no" : "1",
    "branch" : "mechanical",
    "college" : "east point"},

    {"name" : "chandan",
    "reg_no" : "2",
    "branch" : "mechanical",
    "college" : "cambridge"}, 

    {"name" : "akshay",
    "reg_no" : "3",
    "branch" : "information science",
    "college" : "east point"}
    ]

@app.route("/", methods = ["GET"])
def hello():
    return jsonify("hello")

@app.route("/database", methods = ['GET'])
def get():
    return jsonify({"database" : database})


@app.route("/database", methods = ["POST"])
def create():
    data = {"name" : "charan",
    "reg_no" : "4",
    "branch" : "civil",
    "college" : "bit"}
    database.append(data)
    return jsonify({"created": data})

@app.route("/database/<int:reg_no>", methods = ["PUT"])
def data_update(reg_no):
    database[reg_no]["college"] = "BIT"
    database[reg_no]["name"] =  "charan r gowda"
    return jsonify({"data": database[reg_no]})

@app.route("/database/<int:reg_no>", methods = ["DELETE"])
def delete(reg_no):
    database.remove(database[reg_no])
    return jsonify({"result" : True})

@app.route("/database/<int:reg_no>/update", methods = ["PATCH"])
def update(reg_no):
    database[reg_no]["name"] = "pks"
    return jsonify({"data": database[reg_no]})


if __name__ == "__main__":
    app.run(debug=True)

