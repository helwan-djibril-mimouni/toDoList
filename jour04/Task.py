class Task :
    __title = ""
    __description = ""
    __due_date = ""
    __completed = False
    __priority = 0

    def __init__(self, title, description, due_date, completed, priority):
        self.__title = title
        self.__description = description
        self.__due_date = due_date
        self.__completed = completed
        self.__priority = priority

    def get_title(self) :
        return self.__title
    
    def set_title(self, title) :
        self.__title = title

    def get_description(self) :
        return self.__description
    
    def set_description(self, description) :
        self.__description = description
    
    def get_due_date(self) :
        return self.__due_date
    
    def set_due_date(self, due_date) :
        self.__due_date = due_date

    def get_completed(self) :
        return self.__completed
    
    def set_completed(self, completed) :
        self.__completed = completed
    
    def get_priority(self) :
        return self.__priority
    
    def set_priority(self, priority) :
        self.__priority = priority
    
    def get_dictionary(self) :
        dict_obj = {
            "title": self.__title,
            "description": self.__description,
            "dueDate": self.__due_date,
            "completed": self.__completed,
            "priority": self.__priority
        }

        return dict_obj
    
    def get_task_from_dictionary(self, dict_obj:dict) :
        self.__title = dict_obj.get("title")
        self.__description = dict_obj.get("description")
        self.__due_date = dict_obj.get("dueDate")
        self.__completed = dict_obj.get("completed")
        self.__priority = dict_obj.get("priority")
    
    def get_task_from_string(self, string:str) :
        start = string.find("title")+9
        end = string.find('", "description')
        self.__title = string[start:end]
        start = string.find("description")+15
        end = string.find('", "dueDate')
        self.__description = string[start:end]
        start = string.find("dueDate")+11
        end = string.find('", "completed')
        self.__due_date = string[start:end]
        start = string.find("completed")+12
        end = string.find(', "priority')
        if (string[start:end] == "false") :
            self.__completed = False
        elif (string[start:end] == "true") :
            self.__completed = True
        start = string.find("priority")+11
        end = string.find('}')
        self.__completed = string[start:end]
        