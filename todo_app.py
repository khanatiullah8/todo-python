from mypackage import Todo, START_ID
import json

status_tuple = ('pending','completed')

with open('todo_item.json','r') as f:
    file_todo_item = json.load(f)
    file_todo_item = file_todo_item if file_todo_item else []
    
with open('next_todo_id.txt','r') as f:
    next_todo_id  = json.load(f)
    next_todo_id = int(next_todo_id) if next_todo_id else START_ID
    
todo = Todo(file_todo_item, next_todo_id)

while True:
    print("")
    print("----------------------------")
    print("Todo Application")
    print("----------------------------")
    print("1. Show all todos")
    print("2. Create todo")
    print("3. Update todo")
    print("4. Delete todo")
    print("5. Reset todo list")
    print("6. Exit")
    
    option = input("Select an option: ")
    
    if option == '1':
        is_todo = todo.read_all_todos()
        if not is_todo:
            print("!!! Your todo list is currently empty !!!")
    elif option == '2':
        title = input("Enter todo Title: ").strip().lower()
        created_id, all_todos = todo.create_todo(title)
        with open('todo_item.json','w') as todo_file:
            json.dump(all_todos, todo_file, indent=4)
        with open('next_todo_id.txt','w') as id_file:
            id_file.write(str(created_id+1))
        print("✅ Todo created successfully")
    elif option == '3':
        is_todo = todo.read_all_todos(read_only=False)
        if not is_todo:
            print("❌ Can't perform 'Update operation', your todo list is currently empty")
        else:
            id = input("Enter todo ID: ").strip().lower()
            title = input("Enter todo Title: ").strip().lower()
            status = input("Enter todo Status (pending/completed): ").strip().lower()

            # check if any todo's ID is matched with given ID 
            id_matched = todo.check_id(id)

            if not id_matched:
                print("❌ ID Mismatch")
            elif not title and not status:
                print("❌ Update atleast one field")
            elif status and status not in status_tuple:
                print("❌ Invalid status, try again")
            else:
                all_todos = todo.update_todo(id, title, status)
                with open('todo_item.json','w') as todo_file:
                    json.dump(all_todos, todo_file, indent=4)
                print(f"✅ Todo with an ID '{id}' is Updated successfully")
    elif option == '4':
        is_todo = todo.read_all_todos(read_only=False)
        
        if not is_todo:
            print("❌ Can't perform 'Delete operation', your todo list is currently empty")
        else:
            id = input("Enter todo ID: ").strip().lower()
            
            # check if any todo's ID is matched with given ID 
            id_matched = todo.check_id(id)
            
            if not id_matched:
                print("❌ ID Mismatch")
            else:
                all_todos = todo.delete_todo(id)
                with open('todo_item.json','w') as todo_file:
                    json.dump(all_todos, todo_file, indent=4)
                print(f"✅ Todo with an ID '{id}' is Deleted successfully")
    elif option == '5':
        confirm = input("Are you sure? (y/n): ").strip().lower()
        if confirm == 'y':
            with open('todo_item.json','w') as todo_file:
                json.dump([], todo_file)
            with open('next_todo_id.txt','w') as id_file:
                id_file.write(str(START_ID))
            todo.reset_todos()
            print("✅ Your todo list has been reset")
        elif confirm == 'n':
            print("!!! Okay then, let's continue again !!!")
        else:
            print("❌ invalid choice")
    elif option == '6':
        print("----------------------------")
        print('Thanks for using this App!')
        print("----------------------------")
        break
    else:
        print("❌ invalid selection--try again")