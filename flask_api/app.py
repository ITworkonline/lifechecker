from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

"""
Constant: Mock habits data
Length of data: 3
Attributes: id, name, createTime, frequency, threshold, completed
"""
habit_dict = {
    1: {"id": 1, "name": "Work out", "createTime": datetime.now(), "frequency": "weekly", "threshold":80, "completed":True},
    2: {"id": 2, "name": "Reading books", "createTime": datetime.now(), "frequency": "monthly", "threshold":50, "completed":True},
    3: {"id": 3, "name": "Sports", "createTime": datetime.now(), "frequency": "monthly", "threshold":20, "completed":False},
}

"""
About page: test the endpoint
"""
@app.route('/about')
def about_route():
    response_body = {
        "name": "Jie",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }
    return response_body

"""
API call based on GET or POST
GET: List of habits
POST: Create new habit
"""
@app.route('/habitslist', methods=['GET', 'POST'])
def habits_route():
    if request.method == 'GET':
        return list_habits()
    elif request.method == "POST":
        return add_habit(request.get_json(force=True))

"""
Concrete list of habits method
"""
def list_habits():
    return {"habits_list":list(habit_dict.values())}

"""
Concrete add new habit
"""
def add_habit(request_data):
    habit_id = max(habit_dict.keys()) + 1
    new_habit = {
        "id": habit_id,
        "name": request_data['name'],
        "createTime": datetime.now(),
        "frequency": request_data['frequency'],
        "threshold": request_data['threshold'],
        "completed": False
    }
    habit_dict[habit_id] = new_habit
    return jsonify(new_habit)

"""
Concrete update the habit based on id
"""
@app.route('/habitslist/<int:habit_id>', methods=['GET','PUT', 'DELETE'])
def habit_id_route(habit_id):
    if request.method == 'GET':
        return get_habit_attributes_by_id(habit_id)
    elif request.method == "PUT":
        return update_habit_by_id(habit_id, request.get_json(force=True))
    elif request.method == "DELETE":
        return delete_habit_by_id(habit_id)

"""
Concrete get attributes by habit id
"""
def get_habit_attributes_by_id(habit_id):
    if habit_id not in habit_dict:
        return jsonify({"message": "Habit not found"}), 404
    return habit_dict[habit_id]

"""
Concrete update habit attributes by its id
"""
def update_habit_by_id(habit_id, new_habit_attributes):
    if habit_id not in habit_dict:
        return jsonify({"message": "Habit not found"}), 404
    habit = habit_dict[habit_id]
    habit.update(new_habit_attributes)
    return jsonify(habit)

"""
Concrete delete habit by its id
"""
def delete_habit_by_id(habit_id):
    if habit_id not in habit_dict:
        return jsonify({"message": "Habit not found"}), 404
    deleting_habit = habit_dict[habit_id]
    del habit_dict[habit_id]
    return deleting_habit
