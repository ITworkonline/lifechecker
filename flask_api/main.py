from flask import Flask, request
from datetime import datetime

import requests
app = Flask(__name__)

"""
Constant: Mock habits data
Length of data: 3
Attributes: name, createTime, frequency, threshold, completed
"""
habit_dict = {
   "Work out" : {"name": "Work out", "createTime": datetime.now(), "frequency": "weekly", "threshold":80, "completed":True},
   "Reading books" : {"name": "Reading books", "createTime": datetime.now(), "frequency": "monthly", "threshold":50, "completed":True},
   "Sports" : {"name": "Sports", "createTime": datetime.now(), "frequency": "monthly", "threshold":20, "completed":False},
}

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
        return create_habit(request.get_json(force=True))

"""
Concrete list of habits method
"""
def list_habits():
    return {"habits_list":list(habit_dict.values())}

"""
Concrete creat new habit
"""
def create_habit(new_habit):
    habit_name = new_habit['name']
    habit_dict[habit_name] = new_habit
    return new_habit


