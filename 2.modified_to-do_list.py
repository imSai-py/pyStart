tasks = []

def show_menu():
    print('\n======== TO-DO LIST MENU ========')
    print('1. ➕ Add a Task')
    print('2. 👀 View Tasks')
    print('3. ❌ Remove Task')
    print('4. 🚪 Exit TO-DO')
    print('=================================')

def add_task():
    task = input('Enter a task: ').strip()
    if task:
        tasks.append(task)
        print('✅ Task added!')
    else:
        print('⚠️ Task cannot be empty.')

def view_tasks():
    if not tasks:
        print('No tasks yet!')
    else:
        print('\nYour Tasks:')
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')

def remove_task():
    if not tasks:
        print('No tasks to remove!')
        return
    view_tasks()
    try:
        num = int(input('Enter the task number to remove: '))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f'🗑️ Removed task: {removed}')
        else:
            print('⚠️ Invalid task number!')
    except ValueError:
        print('⚠️ Please enter a valid number.')

def main():
    while True:
        show_menu()
        choice = input('Choose an option (1-4): ').strip()
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print('👋 Exiting TO-DO List.')
            break
        else:
            print('⚠️ Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
