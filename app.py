from  add import python_function
def getSelectMenuNumber():
    print("--------------To do list app---------------")
    print("menu")
    print("1. เพิ่มรายการ")
    print("2. แสดงรายการ")
    print("3. ลบรายกาาร")
    print("4.ทำเครื่องหมายว่าเสร็จแล้ว")
    print("5. บันทึกข้อมูลลงไฟล์")
    print("6. โหลลดข้อมูลลขากไฟล์")

    select_menu = input("เลือกเมนู (ตัวเลข) : ")
    select_menu_number = int(select_menu)

    print("menu i choose: ", select_menu_number)

    return select_menu_number

print("--------------------")
python_function(select_menu_number)


tasks = []

if select_menu_number == 1 :
    print("คุนเลือกเมนูที่1")
elif select_menu_number == 2 :
    print("คุนเลือกเมนูที่2")
elif select_menu_number == 3 :
    print("คุนเลือกเมนูที่3")
elif select_menu_number == 4 :
    print("คุนเลือกเมนูที่4")
elif select_menu_number == 5 :
    print("คุนเลือกเมนูที่5")
elif select_menu_number == 6 :
    print("คุนเลือกเมนูที่6")
else:
    print("ควยไรมั่วละ")