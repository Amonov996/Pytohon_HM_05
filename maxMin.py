#Avtomobillar qaysi davlarda ko'p va qaysi birida kam ekanligini aniqlash
# Aynan qaysi modellar ekanligini aniqlash
# id,first_name,last_name,gender,brand,year,color,country
from pprint import pprint
with open('salom.txt') as f:
    dct_country = {}
    dct_cars = {}
    for i in f.read().split('\n')[1::]:
        line = i.split(',')
        if line[4] not in dct_cars:
            dct_cars[line[4]] = 1
        else:
            dct_cars[line[4]] +=1

        if line[-1] not in dct_country:
            dct_country[line[-1]] = [line[4]]
        else:
            dct_country[line[-1]].append(line[4])
brand = max(dct_cars, key=dct_cars.get)
print(brand)
# pprint(dct_country)

max_countyr = max(dct_country.items(), key=lambda x: x[1].count(brand))[0]
min_countyr = min(dict(filter(lambda x: x[1].count(brand)>0, dct_country.items())),key=lambda x: x[1].count(brand))
print(min_countyr)