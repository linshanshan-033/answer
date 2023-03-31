import re

# 1、长文本
long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

# 2、长文本转换为列表
text_list = []
sentence = ''
for e in long_text:
    if e != '\n':
        sentence += e
    else:
        text_list.append(sentence)
        sentence = ''
# 去掉列表空元素
text_list.remove('')

# 3、列表解析为字典格式
text_dict = {'name': text_list[0], 'lei': text_list[1], 'sub_fund': []}
count = -1
for i in range(2, len(text_list)):
    if re.match('^\d', text_list[i]):
        text_dict['sub_fund'].append({'title': '', 'isin': []})
        count += 1
        text_dict['sub_fund'][count]['title'] = text_list[i]
    else:
        if count <= 100:
            text_dict['sub_fund'][count]['isin'].append(text_list[i])

print(text_dict)
