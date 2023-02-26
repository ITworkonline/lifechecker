from flask import Flask, request
from datetime import datetime
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
        return create_habit(request.get_json(force=True))

"""
Concrete list of habits method
"""
def list_habits():
    return {"habits_list":list(habit_dict.values())}

"""
Concrete create new habit
"""
@app.route('/addhabits', methods=['GET', 'POST'])
def create_habit(new_habit):
    habit_name = new_habit['name']
    habit_dict[habit_name] = new_habit
    return new_habit

"""
API call based on GET, PUT, DELETE
GET: Get habit's attributes
PUT: Update the habit by name
DELETE: Delete the habit by name
"""
@app.route('/habitslist/<habit_name>', methods=['GET', 'PUT', 'DELETE'])
def programming_language_route(habit_name):
   if request.method == 'GET':
       return get_habit_attributes(habit_name)
   elif request.method == "PUT":
       return update_habit(habit_name, request.get_json(force=True))
   elif request.method == "DELETE":
       return delete_programming_language(habit_name)

"""
Concrete get attributes by habit name
"""
def get_habit_attributes(habit_name):
   return habit_dict[habit_name]

"""
Concrete update habit attributes by its name
"""
def update_habit(habit_name, new_habit_attributes):
   habit = habit_dict[habit_name]
   habit.update(new_habit_attributes)
   return habit

"""
Concrete delete habit by its name
"""
def delete_programming_language(habit_name):
   deleting_habit = habit_dict[habit_name]
   del habit_dict[habit_name]
   return deleting_habit