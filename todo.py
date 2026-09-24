import storage
from datetime import datetime

def out_memo_list():
    data=storage.load_data()
    memo_list=data["memo"] # 引用memo_list改data自动改
    return memo_list



    # if memo_list:
    #     print("备忘录列表：\n")
    #     for memo in memo_list:
    #         print(f"ID：{memo["id"]} 名称：{memo["name"]}\n")
    # else:
    #     print("备忘录列表为空，请先创建\n")


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


if __name__ == '__main__':
    memolist=out_memo_list()
    print(memolist)