import os
import re
import time
import datetime
import difflib
import urllib3
import shutil
import ctypes
from ftplib import FTP
urllib3.disable_warnings()

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
            #print("max:",max_name1)
            return max_name1
    except Exception as e:
        print("err,please check the path")
        print(e)
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

def ftp_connect(host,port, username, password):
    ftp = FTP()
    # 打开调试级别2，显示详细信息
    # ftp.set_debuglevel(2)
    ftp.connect(host, port)
    ftp.login(username, password)
    #exit(1)
    return ftp


def is_same_size(local_file, remote_file):
    """
    判断远程文件和本地文件大小是否一致
    参数:
    local_file: 本地文件
    remote_file: 远程文件
    """
    try:
        remote_file_size = ftp.size(remote_file)
    except Exception as err:
        # self.debug_print("is_same_size() 错误描述为：%s" % err)
        remote_file_size = -1

    try:
        local_file_size = os.path.getsize(local_file)
    except Exception as err:
        # self.debug_print("is_same_size() 错误描述为：%s" % err)
        local_file_size = -1

    print('local_file_size:%d  , remote_file_size:%d' % (local_file_size, remote_file_size))
    if remote_file_size == local_file_size:
        return 1
    else:
        return 0


def upload_file(local_file, remote_file, curr_time):
    """
    从本地上传文件到ftp
    参数:
    local_path: 本地文件
    remote_path: 远程文件
    """
    if not os.path.isfile(local_file):
        print('%s 不存在' % local_file)
        return

    #if is_same_size(local_file, remote_file):
    #    print('跳过相等的文件: %s' % local_file)
    #    return

    buf_size = 1024
    file_handler = open(local_file, 'rb')
    ftp.storbinary('STOR %s' % remote_file, file_handler, buf_size)
    file_handler.close()
    print("[{cur}] Upload {file} Successful".format(cur=curr_time,file=local_file))
    time.sleep(2)
    ftp.close() #关闭ftp

def create_floder(path,flo_name):
    filename = path + str(flo_name)  # 新建文件
    #print(filename)
    if not os.path.exists(filename):  # 判断文件夹是否存在
        os.makedirs(filename)  # 新建文件夹
    else:
        print('Cache folder has been create')


def copyfile(srcfile,dstpath):                       # 复制函数
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        shutil.copy(srcfile, dstpath + fname)          # 复制文件
        #print ("copy %s -> %s"%(srcfile, dstpath + fname))


def ftp_run(ip, username, password, curr_time):
    remote_path = "/SSTDDada/" + recent_file
    #remote_path = "/ftpTest/" + recent_file
    local_path = path + "cache/" + recent_file
    # host,port, username, password
    global ftp
    try:
        ftp = ftp_connect(ip, 21, username, password)
        #print(" ")
        #print(ftp.getwelcome())  # 打印出欢迎信息
        print("***FTP Server Connected***")

        # 设置FTP当前操作的路径
        ftp.cwd('/SSTDDada')
        # 显示目录下所有目录信息
        ftp.dir()


        #print(" ")
        upload_file(local_path, remote_path,curr_time)
        if ftp:
            ftp.close()
    except Exception as e:
        print("[ERR]:", e)
        reg = '([0-9]+)'
        code = int("".join(re.findall(reg, str(e))))
        #print(code)
        if code == 530:
            print("username or password error")
        elif code == 10061:
            print("FTP Server deny")
        elif code == 10065:
            print("Cannot connect to the FTP Server")
        else:
            print("the FTP Server cannot support")


def Get_currTime():
    currtime = datetime.datetime.now()
    curr_date = currtime.strftime("%Y-%m-%d")
    curr_time = currtime.strftime("%H:%M:%S")
    RTC = str(curr_date + " " + curr_time)
    # print("当前时间："+RTC)
    return RTC


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

if __name__ == "__main__":
    os.system("mode con cols=80 lines=30")
    device_num = 2
    global device, hou, regular, set_seconds
    if True:
        # ************** 2DVD *******************
        if int(device_num) == 1:
            device = "2DVD"
            hou = "hyd"
            regular = '^[a-zA-Z]?([0-9]+)'
            set_seconds = 87000  # 24h10m
        # ************** OTT *******************
        elif int(device_num) == 2:
            device = "OTT"
            hou = "mis"
            regular = '^[a-zA-Z]+([0-9]+)'
            set_seconds = 87000  # 24h10m
        # ************** CAWS ******************
        elif int(device_num) == 3:
            device = "CAWS"
            hou = "txt"
            regular = '^([0-9]+-[0-9]+-[0-9]+)'
            set_seconds = 87000  # 24h10m
        # ************** Hyvis *****************
        elif int(device_num) == 4:
            device = "Hyvis"
            hou = "csv"
            regular = '_([0-9]+)'
            set_seconds = 87000  # 24h10m
        # ************** VAISALA ***************
        elif int(device_num) == 5:
            print("Under development")
        # ************** OTHERS ****************
        elif int(device_num) == 6:
            print("Under development")
        else:
            print("Tips：Enter [1-6]")

    path = "D:/OTT/"
    #ip = "114.255.31.104"
    ip = "192.168.24.17"
    #fusername = "updata"
    fusername = "test"
    #fpassword = "data0311"
    fpassword = "1111"

    #m = input("m:")
    #s = input("s:")


    create_floder(path, "cache")
    print("Uploader is running...")

    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 128)
    while True:
        #print("正在运行")
        recent_file = change_dect(path, hou, regular, device)
        #print(recent_file)
        curr_time = Get_currTime()
        hour = curr_time[11:13]
        min = curr_time[14:16]
        sec = curr_time[17:19]
        '''
        #print(curr_time)
        #print(int(hour),int(min))
        if (int(min) == 26 and int(sec) == 45):
        #if (int(min) == m and int(sec) == s):
            print("1")
            copyfile(path + recent_file, path + "./cache/")
            time.sleep(3)
            ftp_run(ip,fusername,fpassword,curr_time)
        if (int(hour) == 5 and int(min) == 20 and int(sec) == 13):
            del_file(path+"cache")
            time.sleep(5)
        '''
        copyfile(path + recent_file, path + "./cache/")
        time.sleep(3)
        ftp_run(ip,fusername,fpassword,curr_time)
        del_file(path + "cache")
        time.sleep(5)
        #'''

    # 设置FTP当前操作的路径
    # ftp.cwd('/')
    # 显示目录下所有目录信息
    # ftp.dir()
    # 返回一个文件名列表
    # filename_list = ftp.nlst()
    # print(filename_list)
    # ftp.mkd('目录名')# 新建远程目录
    # ftp.rmd('目录名')  # 删除远程目录
    # ftp.delete('文件名')  # 删除远程文件
    # ftp.rename('fromname', 'toname')  # 将fromname修改名称为toname
    # 逐行读取ftp文本文件
    # file = '/upload/1.txt'
    # ftp.retrlines('RETR %s' % file)