'''
三、实践练习
现在让我们通过一个简单的例子来巩固所学的知识：

练习：创建一个程序，计算一个人的BMI指数（体重指数）

步骤：

输入身高（单位：米）
输入体重（单位：千克）
计算BMI = 体重 / (身高 * 身高)
根据BMI值输出对应的体重状况
'''

# 输入身高（单位：米）
height = float(input("请输入您的身高（单位：米）："))
# 输入体重（单位：千克）
weight = float(input("请输入您的体重（单位：千克）："))
# 计算BMI
bmi = weight / (height * height)
# 根据BMI值输出对应的体重状况
if bmi < 18.5:
    print(f"您的BMI为{bmi:.2f}，体重过轻")
elif 18.5 <= bmi < 24:
    print(f"您的BMI为{bmi:.2f}，体重正常")
elif 24 <= bmi < 28:
    print(f"您的BMI为{bmi:.2f}，体重过重")
else:
    print(f"您的BMI为{bmi:.2f}，肥胖")
