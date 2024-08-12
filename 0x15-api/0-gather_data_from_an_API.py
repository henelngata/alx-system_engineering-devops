#!/usr/bin/python3
"""using this REST API,
for a given employee ID,
returns information about his/her
TODOlist progress.
"""
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    todo_url = 'https://jsonplaceholder.typicode.com/todos'\
        + "?userId={}".format(id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    user_response = requests.get(user_url)
    employee_name = user_response.json()["name"]
    tasks = requests.get(todo_url).json()
    number_of_tasks = len(tasks)
    total = 0

    for task in tasks:
        if task["completed"] is True:
            total = total + 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, total, number_of_tasks)
          )

    for task in tasks:
        if task["completed"] is True:
            task_title = task["title"]
            print("\t {}".format(task_title))
