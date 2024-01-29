#!/usr/bin/python3
"""Gathers data from an api"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])

    # Fetching employee information
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        employee_id)

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        user_data = user_response.json()
        todo_data = todo_response.json()

        if not user_data or not todo_data:
            print(
                "User or TODO data not found for employee ID: {}".format(
                    employee_id
                )
            )
            exit(1)

        # Extracting relevant information
        employee_name = user_data.get('name')
        total_tasks = len(todo_data)
        completed_tasks = sum(task.get('completed') for task in todo_data)
        completed_task_titles = [
            task.get('title') for task in todo_data if task.get('completed')]

        # Displaying information
        print("Employee {} is done with tasks({}/{}):".format(employee_name,
              completed_tasks, total_tasks))
        for title in completed_task_titles:
            print("\t {}".format(title))

    except requests.exceptions.RequestException as e:
        print("Error during API request:", e)
        exit(1)
