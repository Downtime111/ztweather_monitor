import threading
import time
import serial
import datetime
import math
import re
import os
import ctypes



#11111
#2222

class SerThread:
    def __init__(self, Port, Baud):
        # 初始化串口、blog文件名称
        self.my_serial = serial.Serial()
        self.my_serial.port = Port
        self.my_serial.baudrate = Baud
        self.my_serial.timeout = 1
        self.alive = False
        self.waitEnd = None
        fname = time.strftime("%Y%m%d")  # blog名称为当前时间
        self.rfname = 'r' + fname  # 接收blog名称
        self.sfname = 's' + fname  # 发送blog名称
        self.thread_read = None
        self.thread_send = None

    def waiting(self):
        # 等待event停止标志
        if not self.waitEnd is None:
            self.waitEnd.wait()

    def start(self):
        # 开串口以及blog文件
        #self.rfile = open(self.rfname, 'w')
        #self.sfile = open(self.sfname, 'w')
        try:
            self.my_serial.open()
        except Exception as e:
            print(e)
            while True:
                time.sleep(30)
                break

        if self.my_serial.isOpen():
            self.waitEnd = threading.Event()
            self.alive = True

            self.thread_read = threading.Thread(target=self.Reader)
            self.thread_read.setDaemon(True)

            self.thread_send = threading.Thread(target=self.send_RTC)
            self.thread_send.setDaemon(True)

            self.thread_read.start()
            self.thread_send.start()
            return True
        else:
            return False

    def Reader(self):
        global rx_sec, rx_min, chazhi
        rx_sec = ''
        rx_min = ''
        chazhi = 0
        while self.alive:
            try:
                n = self.my_serial.inWaiting()
                data = ''
                if n:

                    print(">>>[" + str(datetime.datetime.now())+"]")
                    data = str(self.my_serial.readline()[:-2], encoding='utf-8')
                    print("RX:" + data)
                    # print('recv' + ' ' + time.strftime("%Y-%m-%d %X") + ' ' + data.strip())
                    rx_sec = data[18:20]
                    rx_min = data[15:17]
                    rx_time = datetime.datetime.strptime(data[1:20],"%Y-%m-%d %H:%M:%S")
                    #print(rx_time)
                    if int(datetime.datetime.now().strftime("%H%M%S")) >= int(rx_time.strftime("%H%M%S")):
                        chazhi = datetime.datetime.now()-rx_time
                    elif int(rx_time.strftime("%H%M%S")) > int(datetime.datetime.now().strftime("%H%M%S")):
                        chazhi = rx_time-datetime.datetime.now()
                    chazhi = chazhi.seconds
                    #print(chazhi)
                    # print(time.strftime("%Y-%m-%d %X:") + data.strip(), file=self.rfile)
                    if len(data) == 1 and ord(data[len(data) - 1]) == 113:  # 收到字母q，程序退出
                        break
            except Exception as ex:
                print(ex)
        self.waitEnd.set()
        self.alive = False

    def send_RTC(self):

        while self.alive:
            try:
                '''
                print(interval)
                snddata = input("input data:\n")
                self.my_serial.write(snddata.encode('utf-8'))
                print('sent' + ' ' + time.strftime("%Y-%m-%d %X"))
                print(snddata, file=self.sfile)
                '''

                global chazhi
                global sec, cu_sec

                hour = int(str(datetime.datetime.now())[11:13])
                min = int(str(datetime.datetime.now())[14:16])
                sec = int(str(datetime.datetime.now())[17:19])
                #print("cu",self.Get_currTime())
                #print("cal",self.Get_Caltime())
                #print(chazhi)
                if (sec % 30 == 0):
                    if (chazhi != ""):
                        print("    ====Difference:", chazhi, "====")
                        if (int(chazhi) > 2):
                            print(">>>[" + str(datetime.datetime.now())+"]")
                            self.my_serial.write(self.Get_Caltime().encode('utf-8'))
                            print("    ====Command Injection Successful====")
                            rx_sec = ''
                            rx_min = ''
                    
                        else:
                            '''
                            if int(rx_min) != int(min):
                                print(">>>[" + str(datetime.datetime.now()) + "]")
                                self.my_serial.write(self.Get_Caltime().encode('utf-8'))
                                print("    ====Command Injection Successful====")
                            '''
                            pass

                time.sleep(1)
            except Exception as ex:
                print(ex)
        self.waitEnd.set()
        self.alive = False

    def stop(self):
        self.alive = False
        # self.thread_read.join()
        # self.thread_send.join()
        if self.my_serial.isOpen():
            self.my_serial.close()
       # self.rfile.close()
       # self.sfile.close()

    def Get_currTime(self):
        currtime = datetime.datetime.now()
        #curr_date = currtime.strftime("%Y-%m-%d")
        #curr_time = currtime.strftime("%H:%M:%S")
        #RTC = str(curr_date + " " + curr_time)
        # print("当前时间："+RTC)
        return currtime

    def Get_Caltime(self):
        RTC = str(self.Get_currTime())[0:-7]
        left_data = RTC[0:-2]
        #print(left_data)
        second_data = int(RTC[-2:]) + 3
        cal_RTC = left_data + "{:0>2d}".format(second_data)
        command = "settime " + cal_RTC
        print("TX:" + command)
        with open("AutoTimeCal.log", "a+") as log:
            log.write(self.my_serial.port+" : "+command+'\n')
        return command


if __name__ == '__main__':
    os.system("mode con cols=80 lines=30")
    print(
"""
    *********************************************************************
      ═══════════════  ══════════════  ══════════════  ═══         ═══
      ║                ║            ║  ║            ║  ║  ║       ║  ║       
      ║      ════════  ║               ║            ║  ║   ║     ║   ║      
      ║             ║                  ║            ║  ║    ║   ║    ║        
      ║             ║  ║            ║  ║            ║  ║     ║ ║     ║       
      ═══════════════  ══════════════  ══════════════  ═      ═      ═  
      S E R I A L   P O R T   A U T O M A T I C   T I M I N G   T O O L                                                                                      
    *********************************************************************
"""
    )
    while True:
        sernum = input("[1/2]Enter serial num:")
        c1=re.match('^[0-9]+?$',sernum)
        if c1:
            break
        else:
            print(
"""
**[Tips:] If the port is \"COM2\",just enter \"2\"**")
"""
            )
    while True:
        try:
            baud = input("[2/2]Enter the baudrate(default 115200):") or 115200
            c2 = re.match('^[0-9]+?$', str(baud))
            if baud==110 or 300 or 600 or 1200 or 2400 or 4800 or 9600 or 14400 or 19200 or 38400 or 43000 or 57600 or 76800 or 115200 or 128000 or 230400 or 256000 or 460800 or 921600 or 1000000 or 2000000 or 3000000:
                if c2:
                    break
                else:
                    print(
"""
**Optional baud rate:**
110 300 600 1200 2400 4800 9600 14400 19200 
38400 43000 57600 76800 115200 128000 230400
256000 460800 921600 1000000 2000000 3000000
"""
                    )
        except Exception as e:
            print(
"""
**Optional baud rate:**
110 300 600 1200 2400 4800 9600 14400 19200 
38400 43000 57600 76800 115200 128000 230400
256000 460800 921600 1000000 2000000 3000000
"""
            )
    ser = SerThread('com'+str(sernum),baud)
    print("** Serial Port \"COM"+sernum+"\" is Open **")
    time.sleep(1)
    print("** Data Transmission Start **")
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), 128)
    try:
        if ser.start():
            ser.waiting()
            ser.stop()
        else:
            pass
    except Exception as ex:
        print(ex)
    if ser.alive:
        ser.stop()
    print('Program shutdown')
    time.sleep(10)
    del ser
