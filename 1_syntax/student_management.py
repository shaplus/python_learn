# student_management.py
students = []

def add_student(name, age, grade):
    """添加学生"""
    '''返回0表示添加成功，1表示参数错误，2表示年龄错误，3表示年级错误'''
    # 判断参数合法性
    if not name or not age or not grade:
        return 1
    if not isinstance(age, int) or not isinstance(grade, int):
        return 2
    if age < 1 or age > 120:
        return 3
    if grade < 0 or grade > 100:
        return 4
    student = {'name': name, 'age': age, 'grade': grade}
    students.append(student)
    return 0

def get_student(name):
    """获取学生信息"""
    '''返回学生信息字典，如果学生不存在则返回None'''
    for student in students:
        if student['name'] == name:
            return student
    return None

def update_student(name, **kwargs):
    """更新学生信息"""
    '''返回0表示更新成功，1表示学生不存在'''
    student = get_student(name)
    if student is None:
        return 1
    for key, value in kwargs.items():
        if key in student:
            student[key] = value
    return 0

def del_student(name):
    """删除学生"""
    '''返回0表示删除成功，1表示学生不存在'''
    student = get_student(name)
    if student is None:
        return 1
    students.remove(student)
    return 0

def list_students():
    """列出所有学生"""
    for student in students:
        print(student)
    return 0

# 测试
if __name__ == '__main__':
    print(students)
    print('添加学生张三')
    add_student('张三', 18, 90)
    print('添加学生李四')
    add_student('李四', 19, 85)
    list_students()
    print('更新学生张三')
    update_student('张三', age=19, grade=95)
    list_students()
    print('删除学生李四')
    del_student('李四')
    list_students()