def main():
    while True:
        print('1. Add tasks')
        print('2. View tasks')
        print('3. Delete tasks')
        print('4. Exit')
        choice = input('What would you like to do: ')
        if choice == '1':
            as

def add_tasks(task):
    tasks.append(task)
    print(f'{task} has been added.')
    try:
        add_tasks(input('Enter task: '))
    except TypeError:
        print('You have not entered a valid task.')
def view_tasks():
    if len(tasks) == 0:
        print('There are no tasks to view.')
    else:
        print('These are you tasks: ')
        i = 1
        for task in tasks:
            print(str(i) + ". " + task)
            i += 1
            print()
def delete_tasks():
    if len(tasks) == 0:
        print('There are no tasks to delete.')
    else:
        print('These are your tasks:')
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        try:
            remove = int(input('Enter the number of the task to delete: ')) - 1
            if remove < 0 or remove >= len(tasks):
                print('Invalid task number. Please try again.')
            else:
                deleted_task = tasks.pop(remove)
                print(f'"{deleted_task}" has been deleted.')
        except ValueError:
            print('Please enter a valid number.')
        print()
def exit_program():
    decision = input('Are you sure you want to quit y/n: ').lower()
    if decision == 'y':
        break
    else:
        print('You have not entered a valid command')
tasks = []
main()