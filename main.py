import todo
from datetime import datetime

# 时间校验函数
def check_iso_time(time_str: str):
    try:
        dt = datetime.fromisoformat(time_str)
        now = datetime.now()
        if dt <= now:
            return False, "截止时间不能是过去时间"
        return True, "OK"
    except ValueError:
        return False, "时间格式错误，请按照示例格式输入"


 # 输出当前备忘录列表
def print_memo_list():
    memo_list=todo.get_memo_list()
    if memo_list:
        print("备忘录列表：\n")
        for memo in memo_list:
            print(f"ID：{memo["id"]} 名称：{memo["name"]}\n")
    else:
        print("备忘录列表为空，请先创建\n")


def create_memo():
    name=input("请输入新建的备忘录名：")
    todo.add_memo(name)
    print_memo_list()

def ui_delete_memo():
    while True:
        try:
            memo_id=int(input("请输入要删除的备忘录id（数字）（输入-1退出删除操作）："))
            if memo_id==-1:
                break
            elif todo.delete_memo(memo_id):
                print(f"ID:{memo_id}删除成功！\n")
                break # 成功，跳出循环
            else:
                print("未找到ID，请重新输入\n")
        except ValueError:
            print("格式错误！请按格式输入数字id\n")

def print_todo_list():
    while True:
        try:
            memo_id=int(input("请输入要查看的备忘录ID（数字）（输入-1退出删除操作）："))
            if memo_id==-1:
                break
            else:
                todo_list=todo.get_todo_list(memo_id)
                memo_name=todo.get_memo_name(memo_id)
                if todo_list and memo_name:
                    print(f"备忘录【{memo_name}】项目列表：\n")
                    print("ID\t内容\t截止时间\t是否完成\n")
                    for t in todo_list:
                        print(f"{t["id"]}\t{t["content"]}\t{t["dead_time"]}\t{t["done"]}\n")
                    break
                elif memo_name and not todo_list:
                     print(f"备忘录【{memo_name}】项目列表为空，请先创建\n")
                     break
                elif not memo_name:
                     print("未找到ID，请重新输入\n")
        except ValueError:
            print("格式错误！请按格式输入数字id\n")


def ui_add_todo():
    while True:
        try:
            memo_id=int(input("请输入要添加项目的备忘录ID（数字）（输入-1退出添加操作）："))
            if memo_id==-1:
                break
            new_content=input("请输入添加的备忘录内容：")
            new_dead=input("请输入截止时间（示例：2026-09-21T15:30:22）：")
            
            ok, msg = check_iso_time(new_dead)
            if not ok:
                print(f"{msg}\n")
                continue  # 跳过后面，回到循环开头，重新输入
    
            if todo.add_todo(memo_id,new_content,new_dead):
                print("添加成功\n")
                break
            else:
                print("添加失败，备忘录ID不存在\n")
        except ValueError:
            print("ID格式错误！请输入数字\n")

def ui_delete_todo():
    while True:
        try:
            memo_id=int(input("请输入要删除项目的备忘录ID（数字）（输入-1退出删除操作）："))
            if memo_id==-1:
                break
            
            todo_list=todo.get_todo_list(memo_id)
            memo_name=todo.get_memo_name(memo_id)
            if todo_list and memo_name:
                print(f"备忘录【{memo_name}】项目列表：\n")
                print("ID\t内容\t截止时间\t是否完成\n")
                for t in todo_list:
                    print(f"{t["id"]}\t{t["content"]}\t{t["dead_time"]}\t{t["done"]}\n")
            elif memo_name and not todo_list:
                print(f"备忘录【{memo_name}】项目列表为空，请先创建\n")
                break
            elif not memo_name:
                print("未找到备忘录ID，请重新输入\n")

            todo_id=int(input("请输入要删除的项目ID（数字）（输入-1退出删除操作）："))
            if todo_id==-1:
                break
            if todo.delete_todo(memo_id,todo_id):
                print("删除成功\n")
                break
            else:
                print("删除失败，项目ID不存在\n")

        except ValueError:
            print("ID格式错误！请输入数字\n")

def ui_set_done():
    while True:
        try:
            memo_id=int(input("请输入已完成项目的备忘录ID（数字）（输入-1退出操作）："))
            if memo_id==-1:
                break
            
            todo_list=todo.get_todo_list(memo_id)
            memo_name=todo.get_memo_name(memo_id)
            if todo_list and memo_name:
                print(f"备忘录【{memo_name}】项目列表：\n")
                print("ID\t内容\t截止时间\t是否完成\n")
                for t in todo_list:
                    print(f"{t["id"]}\t{t["content"]}\t{t["dead_time"]}\t{t["done"]}\n")
            elif memo_name and not todo_list:
                print(f"备忘录【{memo_name}】项目列表为空，请先创建\n")
                break
            elif not memo_name:
                print("未找到备忘录ID，请重新输入\n")

            todo_id=int(input("请输入要设定已完成项目的项目ID（数字）（输入-1退出操作）："))
            if todo_id==-1:
                break
            if todo.set_done(memo_id,todo_id):
                print("设定项目已完成成功\n")
                break
            else:
                print("设定失败，项目ID不存在\n")

        except ValueError:
            print("ID格式错误！请输入数字\n")

def ui_clean_done():
    while True:
        try:
            memo_id=int(input("请输入要一键清除已完成项目的备忘录ID（数字）（输入-1退出添加操作）："))
            if memo_id==-1:
                break

            if todo.clean_todo_done(memo_id):
                print("清除成功\n")
                break
            else:
                print("清除失败，备忘录ID不存在\n")
        except ValueError:
            print("ID格式错误！请输入数字\n")


if __name__ == '__main__':
    while True:
        print("【todo-cli 菜单栏，请输入0-7数字来完成以下功能（输入-1退出）：】\n")
        print("0.创建一个备忘录\n1.查看备忘录列表\n2.删除一个备忘录\n3.进入一个备忘录，查看其中的项目列表\n4.添加项目\n5.删除项目\n6.将项目设定为已完成\n7.一键清除已完成项目\n")
        a=input("请输入数字：")
        if a=="-1":
            break
        elif a=="0":
            create_memo()
        elif a=="1":
            print_memo_list()
        elif a=="2":
            ui_delete_memo()
        elif a=="3":
            print_todo_list()
        elif a=="4":
            ui_add_todo()
        elif a=="5":
            ui_delete_todo()
        elif a=="6":
            ui_set_done()
        elif a=="7":
            ui_clean_done()
        else :
            print("输入格式错误，请重新输入\n")

        
