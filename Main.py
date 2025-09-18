
def main():
    while True:
        print('1. Add tasks')
        print('2. View tasks')
        print('3. Delete tasks')
        print('4. Filter tasks')
        print('5. Exit')
        choice = input('What would you like to do: ')
        if choice == '1':
            todo = input('Enter task to be added: ')
            priority = input('Enter priority (high and low): ')
            status = input('Complete or incomplete: ')
            add_tasks(todo, priority, status)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_tasks()
        elif choice == '4':
            print('High Priority Tasks:')
            high_tasks = list(filter(lambda t: t['priority'] == 'high', tasks))
            if len(high_tasks) == 0:
                print('No high priority tasks found.')
            else:
                for task in high_tasks:
                    print(f"Task: {task['task']}, Status: {task['status']}")
        elif choice == '5':
            exit_program()
        else:
            break

def add_tasks(task, priority, status='incomplete'):
    if priority.lower() not in ['high', 'low']:
        print('Invalid priority. Priority must be high or low.')
        return
    tasks.append({'task': task, 'priority': priority.lower(), 'status': status})
    print(f'Your {task} has been added.')
def view_tasks(tasks):
    if len(tasks) == 0:
        print('There are no tasks to view.')
    else:
        i = 1
        for task in tasks:
            print(f"{str(i)}. Task: {task['task']}, Priority: {task['priority']}, Status: {task['status']}")
            i += 1
        view_tasks_alone = list(map(lambda x: x['task'], tasks))
        print("Tasks list:", view_tasks_alone)
def delete_tasks():
    if len(tasks) == 0:
        print('There are no tasks to delete.')
    else:
        print('These are your tasks:')
        i = 1
        for task in tasks:
            print(f'{str(i)} + Task: {task["task"]}')
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
    if decision == 'y':
        print('Goodbye!')
        exit()
    else:
        print('You have not entered a valid command')
tasks = []
main()