#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# with open('code.txt', 'r') as code:
#     code = code.read()

# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# s = code
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")


#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

def Compression(text): #алгоритм сжатия
    compresdata = ''

    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count += 1
            i += 1
        compresdata += str(count) + text[i]
        i += 1
    
    return compresdata


def Recovery(text): #алгоритм восстановления
    datarecovery = ''

    i = 0
    while i < len(text):
        datarecovery += str(text[i+1]) * int(text[i])
        i+=2
    
    return datarecovery


with open('Text1.txt', 'r') as t1:
    t1 = t1.read()    

with open('Text2.txt', 'w+') as t2:
    t2.write(Compression(t1))
    t2.seek(0)                     #возврат курсора на начало строки
    t2 = t2.read()
 
with open('Text3.txt', 'w') as t3:
    t3.write(Recovery(t2))
