import re
import pandas as pd

# 1、解析表格信息，列名包含序号、债券代码、债券名称、计息方式、债券面额（万元）、年利率(%)这6列
data_org = pd.read_excel('./charge.xlsx')
data_new = data_org.iloc[:, :6]

# 2、数据只包含带数字序号的行数据
for i in range(len(data_new)):
    if re.findall('[^0-9]', str(data_new['序号'][i])):
        data_new = data_new.drop(labels=i)

# 3、保存成csv文件
data_new.to_csv('./charge_new.csv', index=None)


print('OVER!')
