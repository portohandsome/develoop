def add_tasks(tasks):
    title = input("ใส่ชื่อรายการใหม่: ")
    task = {
        "title": title,
        "completed": False
     }
   
    tasks.append(task)
    print("เพิ่มรายการสำเร็จ")