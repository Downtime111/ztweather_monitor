import re
import csv

if __name__ == '__main__':
    status = "着火"
    filename = "./data/{}_格式1.txt".format(status)
    out_filename = "./data/数据集.csv"

    with open(out_filename, 'rt') as csvfile:
        reader = csv.reader(csvfile)

        column2 = [row[4] for row in reader]

        print(column2)


        #try:
           #with open(filename, "a",encoding="utf-8") as f:
           #     f.write(buffer)

        #except UnicodeEncodeError:
        #    print("编码错误, 该数据无法写到文件中, 直接忽略该数据")
    print("转换完成")
