import re
import csv


def format_num(line):
    global num1, num2, num3, num4
    Temp = re.findall(r'Temp: (.+?),', line)
    for i in Temp:
        num1 = int(i)
    Hum = re.findall(r'Hum: (.+?),', line)
    for i2 in Hum:
        num2 = int(i2)
    Somg = re.findall(r'Somg: (.+?),', line)
    for i3 in Somg:
        num3 = float(i3)
    Co = re.findall(r'Co: (.+?),', line)
    for i4 in Co:
        num4 = float(i4)
    return str(num1), str(num2), str(num3), str(num4)


if __name__ == '__main__':
    filename = "./data/着火.csv"
    out_filename = "./data/着火.txt"
    alarm = 2
    number = 1
    for line in open(out_filename, encoding="utf-8"):
        l = (list(format_num(line)))
        buffer = [l[0], l[1], l[2], l[3], alarm]
        # print(buffer)
        try:
            with open(filename, "a+", newline='') as csvfile:
                writer = csv.writer(csvfile)
                # 以读的方式打开csv 用csv.reader方式判断是否存在标题。
                with open(filename, "r", newline="") as f:
                    reader = csv.reader(f)
                    if not [row for row in reader]:
                        writer.writerow(["Temp", "Hum", "Somg", "Co", "预测等级（0正常/1阴燃/2着火）"])
                        writer.writerows([buffer])
                    else:
                        writer.writerows([buffer])
        except UnicodeEncodeError:
            print("编码错误, 该数据无法写到文件中, 直接忽略该数据")
    print("转换完成")
