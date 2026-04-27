# 4_7_实战使用自制学生管理模块.py
import student_management

print(student_management.students)
print('添加学生张三')
student_management.add_student('张三', 18, 90)
print('添加学生李四')
student_management.add_student('李四', 19, 85)
student_management.list_students()
print('更新学生张三')
student_management.update_student('张三', age=19, grade=95)
student_management.list_students()
print('删除学生李四')
student_management.del_student('李四')
student_management.list_students()
