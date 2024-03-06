import argparse
class Task:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
    def mark_as_completed(self):
        self.completed = True
class TaskManager:
    def __init__(self):
        self.tasks = {}
    def add_task(self, title, description):
        id = len(self.tasks) + 1
        new_task = Task(id, title, description)
        self.tasks[id] = new_task
        print("Task added successfully.")
    def remove_task(self, id):
        if id in self.tasks:
            del self.tasks[id]
            print(f"Task {id} removed successfully.")
        else:
            print("Task not found.")
    def mark_task_completed(self, id):
        if id in self.tasks:
            self.tasks[id].mark_as_completed()
            print(f"Task {id} marked as completed.")
        else:
            print(f"Task with ID {id} not found.")
    def list_tasks(self):
        if self.tasks:
            for id, task in self.tasks.items():
                print(f"ID: {id}, Title: {task.title}, Completed: {task.completed}")
        else:
            print("No tasks available.")
    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks.values():
                f.write(f"{task.id},{task.title},{task.description},{task.completed}\n")
    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    id, title, description, completed = line.strip().split(',')
                    id = int(id)
                    completed = completed == 'True'
                    self.tasks[id] = Task(id, title, description, completed)
        except FileNotFoundError:
            print("Task file not found. Starting with an empty task list.")
def main():
    parser = argparse.ArgumentParser(description="Task Management System")
    subparsers = parser.add_subparsers(dest="command")
    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("-t", "--title", required=True, help="Task title")
    add_parser.add_argument("-d", "--description", help="Task description")
    # Remove task command
    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("-i", "--id", type=int, required=True, help="Task ID")
    # Mark task completed command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("-i", "--id", type=int, required=True, help="Task ID")
    # List tasks command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    args = parser.parse_args()
    # Create TaskManager object
    task_manager = TaskManager()
    task_manager.load_tasks('tasks.txt')  # Load tasks from file
    if args.command == "add":
        title = args.title
        description = args.description
        task_manager.add_task(title, description)
        task_manager.save_tasks('tasks.txt')  # Save tasks to file
    elif args.command == "remove":
        task_id = args.id
        task_manager.remove_task(task_id)
        task_manager.save_tasks('tasks.txt')  # Save tasks to file
    elif args.command == "complete":
        task_id = args.id
        task_manager.mark_task_completed(task_id)
        task_manager.save_tasks('tasks.txt')  # Save tasks to file
    elif args.command == "list":
        task_manager.list_tasks()
    else:
        print("Invalid command. Please use 'add', 'remove', 'complete', or 'list'.")
if __name__ == "__main__":
    main()