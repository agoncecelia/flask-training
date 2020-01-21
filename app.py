from flask import Flask, request, jsonify, json
from flask_pymongo import PyMongo
from bson import json_util

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/issues"
mongo = PyMongo(app)

@app.route('/issue', methods=['POST'])
def create():
    result = mongo.db.issues.insert_one(request.get_json()).inserted_id
    print(result)
    return jsonify({'success': True})

@app.route('/issue', methods=['GET'])
def find():
    result = list(mongo.db.issues.find())
    print(result)
    return json.dumps(result, default=json_util.default)
