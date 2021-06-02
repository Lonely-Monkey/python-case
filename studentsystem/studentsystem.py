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
        if studentId != "":
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
    with open("student", 'w') as wfile:
        for student in student_old:
            #字符串转字典
            #eval()函数用于执行一个字符串表达式并且返回表达式的值
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

#查找学生信息
def search():
    mark = True
    student_query = []
    while mark:
        id = ""
        name = ""
        if os.path.exists("student"):
            mode = input("按ID查输入1；按学生姓名查输入2：")
            if mode == "1":
                id = input("请输入学生ID：")
            elif mode == "2":
                name = input("请输入姓名：")
            else:
                print("您输入有误，请重新输入！")
                search()
            with open("student", 'r') as file:
                #读取全部内容
                student = file.readlines()
                for list in student:
                    #字符串转字典
                    d = dict(eval(list))
                    if d['id'] == id or d['name'] == name:
                        student_query.append(d)
                #显示查询结果
                show_student(student_query)
                student_query.clear()
                inputMark = input("是否继续查询？（y/n）:")
                if inputMark == "n":
                    mark = False
        else:
            print("暂未缓存数据信息！")
            return

# 将保存在列表中的学生信息展示出来
def show_student(studentList):
    if not studentList:
        print("(o@.@o) 无数据信息 （o@.@o） \n")
        return
    #定义标题显示格式
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    #使用format方法对其进行格式化，数字：所占列宽，^：居中显示，\t：添加一个制表符
    print(format_title.format("ID", "名字", '英语成绩', 'python成绩', 'c语言成绩', '总成绩'))
    #定义具体内容显示格式
    format_data = "{:^8}{:^10}\t{:^10}\t{:^10}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(info.get('id'),
                                 info.get('name'),
                                 str(info.get('english')),
                                 str(info.get('python')),
                                 str(info.get('c')),
                                 str(info.get('english') + info.get('python') + info.get('c')).center(12)))

#统计学生总数
def total():
    if os.path.exists('student'):
        with open('student', 'r') as rfile:
            student_old = rfile.readlines()
            if student_old:
                #统计学生人数
                print("一共有 %d 名学生！" % len(student_old))
            else:
                print("还没有录入学生信息！")
    else:
        print('暂未保存数据信息.....')

#显示所有学生信息
def show():
    student_new = []
    if os.path.exists('student'):
        with open('student', 'r') as rfile:
            student_old = rfile.readlines()
        for list in student_old:
            student_new.append(eval(list))
        if student_new:
            show_student(student_new)
    else:
        print('暂未保存数据信息....')

#排序
def sort():
    show()
    if os.path.exists('student'):
        with open('student', 'r') as file:
            student_old = file.readlines()
            student_new = []
        for list in student_old:
            d = dict(eval(list))
            student_new.append(d)
    else:
        return
    ascORdesc = input("请选择（0升序；1降序）：")
    if ascORdesc == '0':
        ascORdescBool = False
    elif ascORdesc == '1':
        ascORdescBool = True
    else:
        print("您输入有误，请重新输入！")
        sort()
    mode = input('请选择排序方式（1按英语成绩排序；2按python成绩排序；3按c语言成绩排序；0按总成绩排序）：')
    if mode == '1':
        #key：排序的键；reverse：是否为降序排序
        student_new.sort(key=lambda x: x['english'], reverse=ascORdescBool)
    elif mode == '2':
        student_new.sort(key=lambda x: x['python'], reverse=ascORdescBool)
    elif mode == '3':
        student_new.sort(key=lambda x: x['c'], reverse=ascORdescBool)
    elif mode == '0':
        student_new.sort(key=lambda x: x['english'] + x['python'] + x['c'], reverse=ascORdescBool)
    else:
        print('您的输入有误，请重新输入！')
        sort()
    show_student(student_new)

if __name__ == '__main__':
    main()