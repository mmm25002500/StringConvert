print('1.第一個字母大寫其餘小寫')
print('2.全部轉大寫')
print('3.全部轉小寫')
print('4.每個單字第一個字轉大寫 其餘小寫')
print('5.大小寫轉換')
print('6.換字')
print('7.搜尋字串')
print('8.計算字的出現次數')
print('9.檢查字串是否在指定範圍內(開始)')
print('10.檢查字串是否在指定範圍內(結束)')
print('11.分割字串')
print('12.合併字串')
print('13.是否為保留字')
print('14.是否為字母或是數字')
print('15.是否為字母')
print('16.是否為數字')
print('17.字母是否為大寫')
print('18.字串是否為小寫')
print('19.是否為空白字元')
print('20.轉換二禁制')
print('21.轉換八禁制')
print('22.轉換十六禁制')
print('23.轉換ASCII')
print('24.轉換Unicode')


choose = int(input('請輸入選項:'))
if choose == 1:
    sentence = input('請輸入句子:')
    print(sentence.capitalize())
elif choose == 2:
    sentence = input('請輸入句子:')
    print(sentence.upper())
elif choose == 3:
    sentence = input('請輸入句子:')
    print(sentence.lower())
elif choose == 4:
    sentence = input('請輸入句子:')
    print(sentence.title())
elif choose == 5:
    sentence = input('請輸入句子:')
    print(sentence.swapcase())
elif choose == 6:
    sentence = input('請輸入句子:')
    subSec = input('請輸入字串:')
    a = int(input('請輸入開始位置'))
    b = int(input('請輸入結束位置'))
    print(sentence.replace(subSec , a ,b))
elif choose == 7:
    sentence = input('請輸入句子:')
    subSec = input('請輸入字串')
    print(sentence.find(subSec))
elif choose == 8:
    sentence = input('請輸入句子:')
    subSec = input('請輸入字串')
    print(sentence.count(subSec))
elif choose == 9:
    sentence = input('請輸入句子:')
    subSec = input('請輸入字串:')
    a = int(input('請輸入開始位置'))
    b = int(input('請輸入結束位置'))
    print(sentence.startwith(subSec,a ,b))
elif choose == 10:
    sentence = input('請輸入句子:')
    subSec = input('請輸入字串:')
    a = int(input('請輸入開始位置'))
    b = int(input('請輸入結束位置'))
    print(sentence.endwith(subSec,a ,b))
elif choose == 11:
    sentence = input('請輸入句子:')
    sep = input('分隔符號:')
    strnum = int(input('分割次數:'))
    print(sentence.split(sep , strnum))
elif choose == 12:
    sentence1 = input('請輸入句子1:')
    sentence2 = input('請輸入句子2:')
    print(sentence1.join(sentence2))
elif choose == 13:
    sentence = input('請輸入句子:')
    print(sentence.isidentifier())
elif choose == 14:
    sentence = input('請輸入句子:')
    print(sentence.isalnum())
elif choose == 15:
    sentence = input('請輸入句子:')
    print(sentence.isalpha())
elif choose == 16:
    sentence = input('請輸入句子:')
    print(sentence.isdigit())
elif choose == 17:
    sentence = input('請輸入句子:')
    print(sentence.isupper())
elif choose == 18:
    sentence = input('請輸入句子:')
    print(sentence.islower())
elif choose == 19:
    sentence = input('請輸入句子:')
    print(sentence.isspace())
elif choose == 20:
    sentence = int(input('請輸入句子:'))
    print(bin(sentence))
elif choose == 21:
    sentence = input('請輸入句子:')
    print(oct(sentence))
elif choose == 22:
    sentence = input('請輸入句子:')
    print(hex(sentence))
elif choose == 23:
    sentence = input('請輸入句子:')
    print(chr(sentence))
elif choose == 24:
    sentence = input('請輸入句子:')
    print(ord(sentence))
