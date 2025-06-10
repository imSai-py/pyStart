# Simple to do list 
# A list to store tasks
tasks = []
# Function to display the tasks
def show_menu():
    print('\nTo-Do List Menu:')
    print('1. Add Task')
    print('2. View Tasks')
    print('3. Remove Task')
    print('4. Exit')
# function to add a task
def add_task():
    task = input('Enter a task: ')
    tasks.append(task)
    print('Task added!')
# function to view tasks
def view_tasks():
    if not tasks:
        print('No tasks yet.')
    else:
        print('\nYour Tasks: ')
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')
# function to remove a task
def remove_task():
    view_tasks()
    try:
        num = int(input('Enter the task number to remove: '))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f'Remonved task: {removed}')
        else:
            print('Invalid task number!')
    except ValueError:
        print('Please enter a valid number.')

# Main loop to run the to-do list application
while True:
    show_menu()
    choice = input('Choose an option (1-4): ')
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print('Exiting the To-Do List. Goodbye!')
        break
    else:
        print('Ivalid choice. Please try again.')