from pprint import pprint
#
# ### Color nomli listda hayvonlar rangi ajratiladi (ular 19 ta)
# color = []
# with open('hayvon.txt.txt', encoding='utf-8') as f:
#     for i in range(1000):
#         s = f.readline().rsplit(',', 4)
#         for j in s:
#             if s[1] not in color:
#                 color.append(s[1])
#
# # hdct nomli Dictionary Color(list) dagi qiymatlar kalit sifatida saqlanadi va
# # ularga qiymat sifatida bo'sh bo'lgan list beriladi
# # bo'sh listlar filedagi qatorlarni saqalsh uchun
# hdct = {}
# for i in color:
#     hdct.update([(i, [])])
# print(hdct)
#
# # hdct Dictionarydan items()lar olinadi s[1] joyda turgan (buyerda rang) qiymatbilan
# # kalit solishtiriladi agarda key qiymat s[1] bilan bir xil bo'lsa qator qiymat sifatida
# # bo'sh listga qo'shiladi
#
# for k, v in hdct.items():
#     with open('hayvon.txt.txt') as f:
#         for j in range(100):
#             s = f.readline().rsplit(',', 4)
#             if s[1] == k:
#                 hdct[k].append(s)
# pprint(hdct)
# """ funtion va moduldan foydalanmadim chalg'itgani sabab """


##### Xuddi o'sha masala qisqa kod bialn
with open('hayvon.txt.txt') as f:
    color = {}
    for i in f.read().split('\n'):
        c = i.rsplit(',',4)
        if c[1] not in color:
            color[c[1]] = c
        else:
            color[c[1]].append(c)
pprint(color)


