import Task
import json
import csv

class TaskManager :
    __tasks : list[Task.Task] = []

    def __init__(self, tasks) :
        self.__tasks = tasks

    def add(self, task) :
        self.__tasks.append(task)
    
    def delete(self, num) :
        self.__tasks.pop(num)
    
    def get_number_of_tasks(self) :
        return len(self.__tasks)
    
    def get_task(self, num) :
        return self.__tasks[num]
    
    def show(self) :
        print("Task List :")
        print("")
        if (len(self.__tasks) == 0) :
            print("None")
            print("")
        else :
            for i in range(len(self.__tasks)) :
                print("Task")
                print("Title : " + self.__tasks[i].get_title())
                print("Description : " + self.__tasks[i].get_description())
                print("Due Date : " + self.__tasks[i].get_due_date())
                if (self.__tasks[i].get_completed() == True) :
                    print("Completed : Yes")
                else:
                    print("Completed : No")
                print("Priority : " + str(self.__tasks[i].get_priority()))
                print("")
        print("")

    def show_with_string(self) :
        string = "Task List :\n\n"
        if (len(self.__tasks) == 0) :
            string += "None\n"
        else :
            for i in range(len(self.__tasks)) :
                string += "Task " + str(i+1) + "\n"
                string += "Title : " + self.__tasks[i].get_title() + "\n"
                string += "Description : " + self.__tasks[i].get_description() + "\n"
                string += "Due Date : " + self.__tasks[i].get_due_date() + "\n"
                if (self.__tasks[i].get_completed() == True) :
                    string += "Completed : Yes" + "\n"
                else:
                    string += "Completed : No" + "\n"
                string += "Priority : " + str(self.__tasks[i].get_priority()) + "\n\n"
        return string

    def show_important(self, priority) : 
        print("Task List :")
        print("")
        if (len(self.__tasks) == 0) :
            print("None")
            print("")
        else :
            for i in range(len(self.__tasks)) :
                if (self.__tasks[i].get_priority()) :
                    print("Task")
                    print("Title : " + self.__tasks[i].get_title())
                    print("Description : " + self.__tasks[i].get_description())
                    print("Due Date : " + self.__tasks[i].get_due_date())
                    if (self.__tasks[i].get_completed() == True) :
                        print("Completed : Yes")
                    else:
                        print("Completed : No")
                    print("Priority : " + str(self.__tasks[i].get_priority()))
                    print("")
        print("")

    def save(self) :
        json_objects = []
        for i in range(len(self.__tasks)) :
            json_object = self.__tasks[i].get_dictionary()
            json_objects.append(json_object)

        with open('tasks.json', 'w') as f:
            f.write(json.dumps(json_objects))

    def export_csv(self) :
        with open('tasks.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for i in range(len(self.__tasks)) :
                writer.writerow([self.__tasks[i].get_title(), self.__tasks[i].get_description(), self.__tasks[i].get_due_date(), self.__tasks[i].get_completed(), self.__tasks[i].get_priority()])

    def load(self, file) :
        with open('tasks.json', 'r') as f:
            tasks_json = f.read().encode("utf-8")

        tasks = json.loads(tasks_json)

        self.__tasks = []

        for task in tasks :
            newTask = Task.Task("a", "b", "c", False, 0)
            newTask.get_task_from_dictionary(task)
            self.__tasks.append(newTask)

    def clear_json(self, file) :
        with open('tasks.json', 'w') as f:
            f.flush()
            f.write("[]")