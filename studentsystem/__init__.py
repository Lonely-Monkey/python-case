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
        print("学生信息录入完毕！")