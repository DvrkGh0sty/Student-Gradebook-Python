def main():
    while True:
        print('1. Add tasks')
        print('2. View tasks')
        print('3. Delete tasks')
        print('4. Exit')
        choice = input('What would you like to do: ')
        if choice == '1':
            todo = input('Enter task: ')
            tasks.append(todo)
            print(f'{todo} has been added')
        elif choice == '2':
            if len(tasks) == 0:
                print('There are no tasks to view.')
            else:
                print('These are you tasks: ')
                i = 1
                for task in tasks:
                    print(str(i) + ". " + task)
                    i += 1
                print()
        elif choice == '3':
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
        elif choice == '4':
            decision = input('Are you sure you want to quit: ')
            if decision == 'y'.lower():
                break
        else:
            print('You have not entered a valid command')

tasks = []
main()