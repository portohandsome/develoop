from view import view_task


def delete_task(tasks):
    view_task(tasks)

    delete_index = int(input("หมายเลขรายการทที่ต้องการลบ: "))

    if 0 <= delete_index <len(tasks):
        task.pop(delete_index)
        print("ลบ Task สำเร็จ")
    else:
        print("กรุณาเลือดหมายเลขให้ถูก")
    
