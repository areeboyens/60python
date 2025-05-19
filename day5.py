todos = []

while True:
    user_action = input("Type your action: 1 to ADD, 2 to SHOW, 3 to EDIT or 4 to QUIT:")
    user_action.strip()
    print(user_action)
    match user_action:
        case "1":
            todos.append(input("Enter a todo:"))
        case "2":
            for item in todos:
                print(item)
        case "3":
            for item in todos:
                print(item)
            number=int(input("Which todo to edit:"))
            number = number-1
            new_todo = input("Enter the new todo value:")
            todos[number]=new_todo
            print("updated list is as below")
            for item in todos:
                print(item)
        case "4":
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
