user_prompt = "Enter your todo and exit to stop at any step: "
todos=[]
while True:
    todo = input(user_prompt)
    if todo.lower() == "exit":
        break
    print(todo.capitalize())
    todos.append(todo)

