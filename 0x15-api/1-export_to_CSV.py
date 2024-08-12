#!/usr/bin/python3
"""using this REST API,
for a given employee ID,
returns information about his/her
TODOlist progress.
"""
from csv import DictWriter, QUOTE_ALL
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
    list_task = []
    for task in tasks:
        new_task = {"username": "{}".format(employee_name)}
        new_task = {**new_task, **task}
        new_task.pop("id")
        list_task.append(new_task)

    with open('{}.csv'.format(sys.argv[1]), 'w', newline='') as f:
        headers = ["userId", "username", "completed", "title"]
        writer = DictWriter(f, fieldnames=headers, quoting=QUOTE_ALL)
        writer.writerows(list_task)
