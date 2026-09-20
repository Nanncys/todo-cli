import json
import os


def load_data():
    try:
        with open("text.json", "r", encoding="utf-8") as file:#r读，Win上必写utf-8
            data = json.load(file)#不用file = open()为了保证文件一定会关闭
    except FileNotFoundError:
        #文件不存在，创建文件，并写入空状态
        data={"memo":[]}
        with open("text.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except json.JSONDecodeError:
        # JSON损坏：先把坏文件改名备份
        broken_name = "text.json.broken"
        os.rename("text.json", broken_name)
        # 新建正常空文件
        data = {"memo": []}
        with open("text.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    return data


def save_data(data):
    json.dump(data, )


def create(data,memo_name):
    pass

if __name__ == '__main__':
    data=load_data()
    print(data)