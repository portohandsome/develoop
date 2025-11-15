def add_task(task):
    title = input("ใส่ชื่อรายการใหม่")
    task = {
         "title": title,
         "completed": True 
    }

    task.append(task)
    print("correct เพิ่มรายการสำเร็จ")