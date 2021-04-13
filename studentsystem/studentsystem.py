import os
import re


def main():
    ctrl = True
    while(ctrl):
        menu()
        option = input("please choose:")
        option_str = re.sub("\D", "", option)
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 0:
                print('您已退出系统！')
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()

# 功能菜单
def menu():
    # 输出菜单
    print("| ========= 功能菜单 =========== |\n"
          "|                                |\n"
          "|     1.录入学生信息             |\n"
          "|     2.查找学生信息             |\n"
          "|     3.删除学生信息             |\n"
          "|     4.修改学生信息             |\n"
          "|     5.排序                     |\n"
          "|     6.统计学生总人数           |\n"
          "|     7.显示所有学生信息         |\n"
          "|     0.退出系统                 |\n"
          "|                                |\n"
          "| ===============================|")

# 将学生信息保存到文件
def save(student):
    try:
       student_txt = open("student", "a")   # 已追加模式打开
    except Exception as e:
        student_txt = open("student", "w")   # 文件不存在，创建文件并打开
    for info in student:
        student_txt.write(str(info) + "\n")   # 按行存储，添加换行符
    student_txt.close()   #关闭文件

# 录入学生信息
def insert():
    studentList = []
    mark = True
    while mark:
        id = input("请输入ID：")
        if not id:
            break
        name = input("请输出名字：")
        if not name:
            break
        try:
            english = int(input("请输入英语成绩："))
            python = int(input("请输入python成绩："))
            c = int(input("请输入c语言成绩："))
        except:
            print("输入无效，不是整数值，请重新录入")
            continue
        student = {"id":id, "name":name, "english":english, "python":python, "c":c}
        studentList.append(student)
        inputMark = input("是否继续添加？（y/n）:")
        if inputMark == "n":
            mark = False
        save(studentList)
        print("学生信息录入完毕！")

#删除学生信息
def delete():
    mark = True
    while mark:
        studentId = input("请输入要删除的学生ID：")
        if studentId is not "":
            #判断文件是否存在
            if os.path.exists("student"):
                with open("student", 'r') as rfile:
                    #读取文件内容
                    student_old = rfile.readlines()
            else:
                student_old = []
            #标记是否删除
            ifdel = False
            if student_old:
                with open("student", 'w') as wfile:
                    d = {}
                    for list in student_old:
                        #字符串转字典
                        d = dict(eval(list))
                        if d['id'] != studentId:
                            wfile.write(str(d) + "\n")
                        else:
                            ifdel = True
                    if ifdel:
                        print("ID为 %s 的学生信息已经被删除....." % studentId)
                    else:
                        print("没有找到ID为 %S 的学生信息...." % studentId)
            else:
                print("无学生信息....")
                break
            show()
            inputMark = input("是否继续删除？ （y/n）：")
            if inputMark == "n":
                mark = False

#修改学生信息
def modify():
    # TODO 显示全部学生信息
    show()
    if os.path.exists("student"):
        with open("student", 'r') as rfile:
            student_old = rfile.readlines()
    else:
        return
    studentId = input("请输入要修改的学生ID：")
    with open("student", 'r') as wfile:
        for student in student_old:
            #字符串转字典
            d = dict(eval(student))
            if d["id"] == studentId:
                print("找到了这名学生，可以修改他的信息!")
                while True:
                    try:
                        d["name"] = input("请输入姓名：")
                        d["english"] = int(input("请输入英语成绩："))
                        d["python"] = int(input("请输入python成绩："))
                        d["c"] = int(input("请输入c语言成绩："))
                    except:
                        print("您的输入有误，请重新输入。")
                    else:
                        break
                #TODO 字典转换为字符串
                student = str(d)
                #TODO 将修改的信息写入到文件
                wfile.write(student + "\n")
                print("修改成功！")
            else:
                #TODO 将未修改的信息写入到文件
                wfile.write(student)
    mark = input("是否继续修改其他学生信息？（y/n）：")
    if mark == "y":
        modify()
