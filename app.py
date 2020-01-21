from flask import Flask, request, jsonify, json
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
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

@app.route('/issue/<id>', methods=["DELETE"])
def delete(id):
    print(id)
    result = mongo.db.issues.delete_one({"_id": ObjectId(id)})

    response = {}
    if result.deleted_count > 0:
        response["success"] = True
        return jsonify(response)
    return jsonify({"success": False, "message": "Not found", "status": 404})


@app.route('/issue/<id>',methods=["PUT"])
def update(id):
#    db.sample.update({"_id":"1002"},{"$set":{"city":"Visakhapatnam"}})
    result = mongo.db.issues.update_one({"_id":ObjectId(id)},{"$set":{"resolved":True}})
    print(result)
    return jsonify({'success': True})