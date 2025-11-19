def view_task(tasks):
    count = 0

    for task in tasks:
        
        print(f"{count + 1}.","รายการ : ", task["title"])