def main():
    while True:
        print('1. Add tasks')
        print('2. View tasks')
        print('3. Delete tasks')
        print('4. Exit')
        choice = input('What would you like to do: ')
        if choice == '1':
            todo = input('Enter task to be added: ')
            priority = input('Enter priority (high and low): ')
            status = input('Complete or incomplete: ')
            add_tasks(todo, priority, status)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_tasks()
        else:
            break

def add_tasks(task, priority, status='incomplete'):
    tasks.append({'task': task, 'priority': priority, 'status': status})
    print('Your todo has been added.')
    while True:
        priority1 = input('Priority high/low: ')
        if priority1.lower() == 'higher' or priority.lower() == 'low':
            break
        else:
            print('Invalid information, data must be within high or low.')
def view_tasks(tasks):
    if len(tasks) == 0:
        print('There are no tasks to view.')
    else:
        for task in tasks:
            print(f"Task: {task['task']}, Priority: {task['priority']}")
def delete_tasks():
    if len(tasks) == 0:
        print('There are no tasks to delete.')
    else:
        print('These are your tasks:')
        i = 1
        for task in tasks:
            print(str(i) + ". " + task)
            i += 1
        try:
            deleted = int(input('Enter the number of the task you want to delete: ')) - 1
            if deleted < 0 or deleted >= len(tasks):
                print('The number entered is too high, there is no task of this value.')
            else:
                removed_task = tasks.pop(deleted)
                print(f'{removed_task} has been deleted')
        except ValueError:
            print('Make sure the value entered is a number instead of a symbol or letter.')
        print()
def exit_program():
    decision = input('Are you sure you want to quit y/n: ').lower()
    print('You have not entered a valid command')
tasks = []
main()