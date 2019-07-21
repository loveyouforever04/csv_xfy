import csv
import os
# Global: Define file name & path
filename = 'test_write.csv'
csv_path = os.getcwd() + '\\csv_files\\' + filename

# Practice 1  - write
# write a row once
header_data = ["行号", "列名1", "列名2"]
row_data = [1, '第1列数据', '第2列数据']  # data of a row
with open(csv_path, "w", encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header_data)
    writer.writerow(row_data)

header_data = ["行号", "列名1", "列名2"]
reapt_times = 10  # data of a row
with open(csv_path, "w", encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header_data)
    for cnt in range(reapt_times):
        row_data = [cnt,'第1列数据','第2列数据']
        writer.writerow(row_data)

# Practice 3 - get filed(cell)
with open(csv_path, "r", encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    row_cnt = 0
    for line in reader:
        row_cnt += 1
        print('第 %d 行， 行号是 %s, 第一列是 %s, 第二列是 %s' %
              (row_cnt, line[0], line[1], line[2]))
