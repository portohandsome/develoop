def add_task(tasks):
    title = input("ใส่ชื่อรายการใหม่: ")
    task = {
        "title": title,
        "completed": True
     }
   
    tasks.append(task)
    print("เพิ่มรายการสำเร็จ")