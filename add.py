def add_task(tasks):
    title = input("Enter new item name: ")
    task = {
        "title": title,
        "completed": False
    }
I
tasks.append(task)
print("Added successful item")