#!/usr/bin/python3
"""using this REST API,
for a given employee ID,
returns information about his/her
TODOlist progress.
"""
import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    todo_url = 'https://jsonplaceholder.typicode.com/todos'\
        + "?userId={}".format(id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    user_response = requests.get(user_url)
    employee_name = user_response.json()["username"]
    tasks = requests.get(todo_url).json()
    list_tasks = []
    for task in tasks:
        new_dict = {"task": task["title"],
                    "completed": task["completed"],
                    "username": employee_name
                    }
        list_tasks.append(new_dict)

    task_dic = {id: list_tasks}
    with open("{}.json".format(id), 'w') as f:
        json.dump(task_dic, f)
