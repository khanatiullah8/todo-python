from tabulate import tabulate

START_ID = 1000

class Todo:
    def __init__(self, todo_list=[], start_id=START_ID):
        self.__todos = todo_list
        self.__id = self.id_generator(start_id)

    # read
    def id_generator(self, start_id):
        while True:
            yield start_id
            start_id += 1
    
    # reset todos
    def reset_todos(self):
        self.__id = self.id_generator(START_ID)
        self.__todos = []
        
    # check if given ID is matched or not
    def check_id(self, id): 
        id_matched = [todo for todo in self.__todos if id == todo['id']]
        return len(id_matched)
        
    # read
    def read_all_todos(self,read_only=True):
        if(self.__todos):
            if read_only:
                print(tabulate(self.__todos,headers="keys",tablefmt="grid"))
        return self.__todos
    
    # create
    def create_todo(self, title):
        id = next(self.__id)
        todo = {"id":f"id{id}","title":title,"status":"pending"}
        self.__todos[:0] = [todo]                   #! 1st method
        # self.__todos = [todo, *self.__todos]      #! 2nd method
        return id, self.__todos
        
    # update
    def update_todo(self, id, title="", status="pending"):
        for todo in self.__todos:
            if id == todo['id']:
                if title: todo['title'] = title
                if status: todo['status'] = status
                break
        return self.__todos
    
    # delete
    def delete_todo(self, id):
        self.__todos = list(filter(lambda x: id != x['id'], self.__todos))              #! 1st method
        # self.__todos = [todo for todo in self.__todos if todo['id'] != id]            #! 2nd method
        return self.__todos
