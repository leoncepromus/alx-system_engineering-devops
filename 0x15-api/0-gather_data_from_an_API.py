#!usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the API endpoint URL (replace 'BASE_URL' with the actual API base URL)
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    endpoint = f'{BASE_URL}/todos?userId={employee_id}'

    try:
        # Send GET request to the API endpoint
        response = requests.get(endpoint)
        todos = response.json()

        if response.status_code == 200:
            # Get user info to display employee name
            user_info = requests.get(f'{BASE_URL}/users/{employee_id}').json()
            employee_name = user_info['name']

            # Calculate completed and total tasks
            total_tasks = len(todos)
            completed_tasks = sum(1 for todo in todos if todo['completed'])

            # Display employee TODO list progress
            print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

            # Display completed task titles
            for todo in todos:
                if todo['completed']:
                    print(f"\t {todo['title']}")

        else:
            print(f"Error: Unable to fetch TODO list. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

