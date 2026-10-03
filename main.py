import todo

def create_memo():



if __name__ == '__main__':
    while True:
        print("【todo-cli 菜单栏，请输入0-7数字来完成以下功能：】\n")
        print("0.创建一个备忘录\n1.查看备忘录列表\n2.删除一个备忘录\n3.进入一个备忘录，查看其中的项目列表\n4.添加项目\n5.删除项目\n6.将项目设定为已完成\n7.一键清除已完成项目\n")
        a=input("请输入数字：")
        if a=="0":
            create_memo()


