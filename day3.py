todos = []

while True:
    user_action = input("Type your action: 1 to ADD, 2 to SHOW or 3 to QUIT:")
    user_action.strip()
    print(user_action)
    match user_action:
        case "1":
            todos.append(input("Enter a todo:"))
        case "2":
            for item in todos:
                print(item)
        case "3":
            break
