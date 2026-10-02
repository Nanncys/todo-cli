import storage
from datetime import datetime

# 获得备忘录列表
def get_memo_list():
    data=storage.load_data()
    memo_list=data["memo"] # 引用memo_list改data自动改
    return memo_list

# # 输出当前备忘录列表
# def print_memo_list():
#     memo_list=get_memo_list()
#     if memo_list:
#         print("备忘录列表：\n")
#         for memo in memo_list:
#             print(f"ID：{memo["id"]} 名称：{memo["name"]}\n")
#     else:
#         print("备忘录列表为空，请先创建\n")

# 增加一个备忘录
def add_memo(name):
    data=storage.load_data()
    memo_list=data["memo"]  # 引用memo_list改data自动改
    if not memo_list:
        new_id=1
    else:
        all_id=[memo["id"] for memo in memo_list]
        new_id=max(all_id)+1
    memo_new={
        "id":new_id,
        "name":name,
        "create_time": datetime.now().isoformat(),
        "include": []
    }
    memo_list.append(memo_new)
    storage.save_data(data)

# 删除一个备忘录
def delete_memo(memo_id):
    data=storage.load_data()
    memo_list=data["memo"]
    found=False
    for memo in memo_list:
        if memo["id"]==memo_id:
            memo_list.remove(memo)
            found=True
            break
    if not found:
        return False
    storage.save_data(data)
    return True

# 在指定备忘录里面添加一个项目
def add_todo(target_id,new_content,new_dead):
    data=storage.load_data()
    memo_list=data["memo"]
    target_include=None
    found=False
    for memo in memo_list:
        # 找对应备忘录id包括的项目内容
        if memo["id"]==target_id:
            target_include=memo["include"]
            found=True
            break
    # 如果找不到相应的id，返回false，main.py收到后输出报错信息
    if not found:
        return False
    # 编号规则，从小到大
    if not target_include:
        new_id=1
    else:
        all_id=[include["id"] for include in target_include]
        new_id=max(all_id)+1
    # dead_time由main判断并输出报错信息
    todo_new={
        "id":new_id,
        "create_time":datetime.now().isoformat(),
        "dead_time":new_dead,
        "content":new_content,
        "done":False
    }
    target_include.append(todo_new)
    storage.save_data(data)
    return True

# 在指定 备忘录里删除一个项目
def delete_todo(memo_id,todo_id):
    data=storage.load_data()
    memo_list=data["memo"]
    found=False
    for memo in memo_list:
        if memo["id"]==memo_id:
            target_include=memo["include"]
            for todo in target_include:
                if todo["id"]==todo_id:
                    target_include.remove(todo)
                    found=True
                    break
        if found:
            break
    if not found:
        return False
    storage.save_data(data)
    return True

# 将备忘录中某项目设为已完成
def set_done(memo_id,todo_id):
    data=storage.load_data()
    memo_list=data["memo"]
    found=False
    for memo in memo_list:
        if memo["id"]==memo_id:
            target_include=memo["include"]
            for todo in target_include:
                if todo["id"]==todo_id:
                    todo["done"]=True
                    found=True
                    break
        if found:
            break
    if not found:
        return False
    storage.save_data(data)
    return True

# 一键清除已完成(在某备忘录内)
def clean_todo_done(memo_id):
    data=storage.load_data()
    memo_list=data["memo"]
    found=False

    for memo in memo_list:
        if memo["id"]==memo_id:
            found=True
            target_include=memo["include"]

            for todo in target_include[:]: # 切片生成浅拷贝副本，循环遍历副本，修改正式的data
                if todo["done"]:
                    target_include.remove(todo)

    if not found:
        return False
    storage.save_data(data)
    return True

if __name__ == '__main__':
    text=clean_todo_done(1)
    print(text)