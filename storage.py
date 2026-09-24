import json
import os
from datetime import datetime

# 要读取的文件名
DATA_FILE = "text.json"

# 读取数据，返回数据字典
def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:# r读，Win上必写utf-8
            data = json.load(f)# 不用file = open()为了保证文件一定会关闭
    except FileNotFoundError:
        # 文件不存在，创建文件，并写入空状态
        data={"memo":[]}
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except json.JSONDecodeError:
        # JSON损坏：先把坏文件改名备份，带时间戳
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        broken_name = f"text.json.broken_{timestamp}"
        os.rename(DATA_FILE, broken_name)
        # 新建正常空文件
        data = {"memo": []}
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    return data

# 写数据
def save_data(data):
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=2)


if __name__ == '__main__':
    # 测试用
    data=load_data()
    print(data)