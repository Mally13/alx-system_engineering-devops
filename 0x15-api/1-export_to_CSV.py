#!/usr/bin/python3
"""Gathers data from an api and exports to csv"""
import requests
from sys import argv
import csv


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
        user_id = user_data.get('id')
        user_name = user_data.get('username')

        csv_filename = "{}.csv".format(user_id)

        # Writing data to CSV file
        with open(csv_filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Writing header
            csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Writing rows
            for task in todo_data:
                task_completed_status = "True" if task.get(
                    'completed') else "False"
                task_title = task.get('title')
                csv_writer.writerow(
                    [
                        user_id,
                        user_name,
                        task_completed_status,
                        task_title])

        print("CSV file '{}' has been created successfully.".format(
            csv_filename
        )
        )

    except requests.exceptions.RequestException as e:
        print("Error during API request:", e)
        exit(1)
