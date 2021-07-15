import requests, json
import urllib3
import os
import re
import time
import datetime
import difflib
import ctypes

urllib3.disable_warnings()


def GetTokenFromServer(Corpid, Secret):
    """获取access_token"""
    Url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    Data = {
        "corpid": Corpid,
        "corpsecret": Secret
    }
    r = requests.get(url=Url, params=Data, verify=False)
    print(r.json())
    if r.json()['errcode'] != 0:
        return False
    else:
        Token = r.json()['access_token']
        file = open(Token_config, 'w')
        file.write(r.text)
        file.close()
        return Token


def SendMessage(Partyid, Subject, Content):
    try:
        file = open(Token_config, 'r')
        Token = json.load(file)['access_token']
        file.close()
    except:
        Token = GetTokenFromServer(Corpid, Secret)

    # 发送消息
    Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    Data = {
        "toparty": Partyid,
        "msgtype": "text",
        "agentid": Agentid,
        "text": {"content": Subject + '\n' + Content},
        "safe": "0"
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'Referer': 'http://61.183.175.130/sunxf/gtghj/index.html',
        'X - Requested - With': 'XMLHttpRequest',
        'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    r = requests.post(url=Url, data=json.dumps(Data, ensure_ascii=False).encode("utf-8"), verify=False, headers=headers)

    # 如果发送失败，将重试三次
    n = 1
    while r.json()['errcode'] != 0 and n < 4:
        n = n + 1
        Token = GetTokenFromServer(Corpid, Secret)
        if Token:
            Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
            r = requests.post(url=Url, data=json.dumps(Data, ensure_ascii=False).encode("utf-8"), verify=False,
                              headers=headers)
            print(r.json())
    return r.json()


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
                # print(i)
                # print(out)
            # print("list:", list_sel)
            recent_file = find_max(list, device)
            max_name = difflib.get_close_matches(recent_file, list_sel, 1, cutoff=0.5)
            max_name1 = "".join(max_name)
            # print("max:",max_name1)
            # print(recent_file)
            recent_path = root + "\\" + max_name1
            # print(recent_path)
            mtime = time.ctime(os.path.getmtime(recent_path))
            # print(mtime)
            change_time = datetime.datetime.strptime(mtime, "%a %b  %d %H:%M:%S %Y")
            print("      chan time:", change_time)
            curr_time = datetime.datetime.now()
            print("      curr time:", curr_time)
            seconds = (curr_time - change_time).seconds
            return seconds, recent_path, change_time
    except Exception as e:
        # print("err,please check the path")
        # print(e)
        pass


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


def alarm(device, location, change_time, interval):
    print("告警信息下发")
    Partyid = 1  # 通知群组 全局1
    Subject = "[{dev}设备信息]".format(dev=device)  # 通知标题
    Content = "状       态：数据保存异常\n地       点：{loc}\n告警时间：{tim}\n最后保存：{cha}\n间隔时间：{val_hour}小时（{val_min}分钟）" \
        .format(tim=Get_currTime(), loc=location, cha=change_time, val_hour=round(interval / 3600, 1),
                val_min=round(interval / 60, 1))  # 通知内容
    print(Subject)
    print(Content)
    Status = SendMessage(Partyid, Subject, Content)
    # print(Status)


def Get_currTime():
    currtime = datetime.datetime.now()
    curr_date = currtime.strftime("%Y-%m-%d")
    curr_time = currtime.strftime("%H:%M:%S")
    RTC = str(curr_date + " " + curr_time)
    # print("当前时间："+RTC)
    return RTC


if __name__ == '__main__':
    # ************* 企业微信API *******************
    # 企业号的标识
    Corpid = "wwcc04e978729e7ed6"
    # 管理组凭证密钥
    Secret = "v5_5ChZRZ9ZrrkWY6p_yB8D7QhHojjMInUcjdH_KTdI"
    # 应用ID
    Agentid = "1000002"
    # token_config文件放置路径
    Token_config = r'.\wechat_config.json'
    # ********************************************

    os.system("mode con cols=80 lines=30")
    path = '.\\'
    #path = '.\\test'
    # ********************************************************************************************

    print(
        '''
    ╒═══════════════════════════════════════════════════════════════════╕
    │       D E V I C E   D A T A   M O N I T O R I N G   T O O L       │
    ╞┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╡
    │  * Device List:                                                   │  
    │                                                                   │    
    │         [1] 2DVD            [2] OTT            [3] CAWS           │   
    │                                                                   │ 
    │         [4] Hyvis           [5] VAISALA        [6] OTHERS         │ 
    │                                                                   │    
    │  * location list:                                                 │ 
    │                                                                   │    
    │         [1] 海坨山          [2] 香山           [3] 铁塔           │  
    ╞┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╡
    │  * Put this program in the data folder.                           │
    │  * Input number selection device.                                 │
    ╘═══════════════════════════════════════════════════════════════════╛
'''
    )
    while True:
        device_num = input("Please select the device [1-6]:") or "1"
        c1 = re.match('^[0-9]+?$', device_num)
        global device, hou, regular, Partyid, Subject, Content
        if c1:  # 86400 24h
            # ************** 2DVD *******************
            if int(device_num) == 1:
                device = "2DVD"
                hou = "hyd"
                regular = '^[a-zA-Z]?([0-9]+)'
                set_seconds = 3600  # 24h10m
                break
            # ************** OTT *******************
            elif int(device_num) == 2:
                device = "OTT"
                hou = "mis"
                regular = '^[a-zA-Z]+([0-9]+)'
                set_seconds = 3600  # 24h10m
                break
            # ************** CAWS ******************
            elif int(device_num) == 3:
                device = "CAWS"
                hou = "txt"
                regular = '^([0-9]+-[0-9]+-[0-9]+)'
                set_seconds = 3600  # 24h10m
                break
            # ************** Hyvis *****************
            elif int(device_num) == 4:
                device = "Hyvis"
                hou = "csv"
                regular = '_([0-9]+)'
                set_seconds = 3600  # 24h10m
                break
            # ************** VAISALA ***************
            elif int(device_num) == 5:
                print("Under development")
            # ************** OTHERS ****************
            elif int(device_num) == 6:
                print("Under development")
            else:
                print("Tips：Enter [1-6]")
        else:
            print("Tips：Enter [1-6]")

    while True:
        location_num = input("Please select the location [1-3]:") or "1"
        c2 = re.match('^[0-9]+?$', device_num)
        if c2:
            if int(location_num) == 1:
                location = "海坨山"
                break
            elif int(location_num) == 2:
                location = "香山"
                break
            elif int(location_num) == 3:
                location = "铁塔"
                break
            else:
                print("Tips：Enter [1-3]")
        else:
            print("Tips：Enter [1-3]")

    os.system('cls')
    send_flag = 0
    while True:
        try:
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 128)

            print(
                '''
    ╒═══════════════════════════════════════════════════════════════════╕
    │       D E V I C E   D A T A   M O N I T O R I N G   T O O L       │
    ╞┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╡
    │  * Device List:                                                   │  
    │                                                                   │    
    │         [1] 2DVD            [2] OTT            [3] CAWS           │   
    │                                                                   │ 
    │         [4] Hyvis           [5] VAISALA        [6] OTHERS         │ 
    │                                                                   │    
    │  * location list:                                                 │ 
    │                                                                   │    
    │         [1] 海坨山          [2] 香山           [3] 铁塔           │  
    ╞┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅╡
    │  * Put this program in the data folder.                           │
    │  * Input number selection device.                                 │
    ╘═══════════════════════════════════════════════════════════════════╛
                '''
            )

            print("      *监测地点：{loc}                              *监测设备：{dev}".format(loc=location, dev=device))
            print(" ")
            interval_seconds, recent_path, change_time = change_dect(path, hou, regular, device)
            # sys.stdout.write("距离上次修改时间："+str(seconds)+"\r\n")
            # sys.stdout.flush()
            # print("距离上次修改时间：",seconds)
            print("      *监测文件:" + recent_path + "  *距离上次修改时间:" +
                  str(interval_seconds) + "秒({hour}小时)".format(hour=round(interval_seconds / 3600)))

            # print(interval_seconds, set_seconds)
            if interval_seconds > set_seconds:
                send_flag = send_flag + 1
            else:
                send_flag = 0
            # print(send_flag)
            if send_flag == 1:
                alarm(device, location, change_time, interval_seconds)
            time.sleep(5)
            os.system('cls')
        except Exception as e:
            print("err,please check the setting")
            print("Do you put this program in the data folder?")
            time.sleep(60)
            os.system('cls')
