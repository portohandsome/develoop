def add_task(tasks):
    title = input("ชื่อรายการ: ")
    task = {
        "title": title,
        "completed": False
     }
   
    tasks.append(task)
    print("เพิ่มรายการสำเร็จ")