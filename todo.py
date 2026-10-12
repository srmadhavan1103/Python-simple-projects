class Task:
    def __init__(self,description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def display(self,number):
        status="Completed" if self.completed else "Pending"
        print(f"{number}. {self.description} - {status}")

class TodoList:
    def __init__(self):
        self.task = []

    def add_task(self):
        description= input("Enter task description: ").strip()
        if description:
            task=Task(description)
            self.task.append(task)
            print("Task added successFully!")
        else:
            print("Task description cannot be empty.")

    def view_tasks(self):
        if not self.tasks:
            print("No task available.")
            return
        print("\n----- Your Tasks -----")
        for number,task in enumerate(self.tasks, start=1):
            task.display(number)

    def complete_task(self):
        if not self.task:
            print("No tasks available.")
            return
        self.view_tasks()

        try:
            number =int(input("\nEnter task number to mark as completed: "))
            if 1<=number<=len(self.task):
                if self.task[number -1].completed:
                    print("Task is already completed.")
                else:
                    self.task[number -1].mark_completed()
                    print("Task marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
        def main():
            todo_list=TodoList()
            self.task=[]
            while True:
                print(" TO-DO LIST APP ")
                print("1. Add Task")
                print("2. View Task")
                print("3. Mark Task as Completed")
                print("4. Exit")
                choice=input("Enter your choice: ")
                if choice=="1":
                    todo_list.add_task()
                elif choice=="2":
                    todo_list.view_tasks()
                elif choice=="3":
                    todo_list.complete_task()
                elif choice=="4":
                    print("Thank you for using the To-Do List App!")
                    break
                else:
                    print("Invalid choice. Please try again.")
        if __name__ == "__main__":
            main()
                

        
