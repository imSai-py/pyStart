Tasks = []

def show_menu():
    print('\n======== TO-DO LIST MENU ========')
    print('1. ➕ Add a Task')
    print('2. 👀 View Tasks')
    print('3. ❌ Remove Task')
    print('4. 🚪 Exit TO-DO')
    print('=================================')

    
def add_task():
    task = input('Enter a task: ')
    Tasks.append(task)
    print('Task Added!')

def view_task():
    if not Tasks:
        print('No task yet!')
    else:
        print('\nYour Tasks: ')
        for i, task in enumerate(Tasks, 1):
            print(f'{i}. {task}')
            
def remove_task():
    view_task()
    try:
        num = int(input('Enter the task number to be removed: '))
        if 1 <= num <= len(Tasks):
            removed = Tasks.pop(num - 1)
            print(f'Removed task: {removed}')
        else:
            print('Invalid Task number!')
    
    except ValueError:
        print('Enter a valid number')
        
while True:
    show_menu()

    choice = input('Choose an option between 1-4: ')
    if choice == '1':
        add_task()
    elif choice == '2':
        view_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print('Exiting TO-DO List.')
        break
    else:
        print('Ivalid Choice. Please Try Again')