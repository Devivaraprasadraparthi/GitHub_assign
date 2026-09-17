from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os

# MongoDB Connection
client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
db = client["todo_db"]
todos_collection = db["todos"]



@app.route('/todo')
def todo_page():
    return render_template('todo.html')


@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    if request.is_json:
        data = request.get_json()
        item_name = data.get('itemName')
        item_description = data.get('itemDescription')
    else:
        item_name = request.form.get('itemName')
        item_description = request.form.get('itemDescription')

    if not item_name or not item_description:
        return jsonify({"error": "itemName and itemDescription are required"}), 400

    new_item = {
        "itemName": item_name,
        "itemDescription": item_description
    }
    result = todos_collection.insert_one(new_item)

    return jsonify({
        "message": "Item stored successfully",
        "id": str(result.inserted_id)
    }), 201