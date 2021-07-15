import os
import re
import difflib
import datetime

def find_max(data, devices):
    try:
        if devices == "2DVD":
            output = max(data)
            return output
        elif devices == "OTT":
            list_ott = []
            for i in data:
                list_ott.append(datetime.datetime.strptime(i, "%Y%m%d"))
            output = max(list_ott).strftime("%Y%m%d")
            return output
        elif devices == "CAWS":
            list_ott = []
            for i in data:
                list_ott.append(datetime.datetime.strptime(i, "%Y-%m-%d"))
            output = max(list_ott).strftime("%Y-%m-%d")
            return output
        elif devices == "Hyvis":
            list_ott = []
            for i in data:
                list_ott.append(datetime.datetime.strptime(i, "%Y%m%d"))
            output = max(list_ott).strftime("%Y%m%d")
            return output
        else:
            pass
    except Exception as e:
        # print("err,please check the device name")
        # print(e)
        pass

def change_dect(path, hou, regular, device):
    try:
        for root, dirs, files in os.walk(path):
            list = []
            list_full = []
            list_sel = []
            # print(root)  # 当前目录路径
            # print(dirs)  # 当前路径下所有子目录
            # print(files)  # 当前路径下所有非目录子文件
            for i in files:
                if ("".join(i).split(".", 1)[1] == hou):
                    list_sel.append(i)
            for i in list_sel:
                out = re.findall(regular, i)
                list.extend(out)
                #print(i)
                #print(out)
            # print("list:", list_sel)
            recent_file = find_max(list, device)
            max_name = difflib.get_close_matches(recent_file, list_sel, 1, cutoff=0.5)
            max_name1 = "".join(max_name)
            #print("max:",max_name1)
            return max_name1
    except Exception as e:
        print("err,please check the path")
        print(e)
        pass

path = "D:/OTT/"
hou = "mis"
regular = '^[a-zA-Z]+([0-9]+)'
device = "OTT"

recent_file = change_dect(path,hou,regular,device)
print(recent_file)