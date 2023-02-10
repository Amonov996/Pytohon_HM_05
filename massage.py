# id,first_name,last_name,gender,brand,year,color,country

with open('salom.txt') as f:
    for i in f.read().split('\n')[1::]:
        line = i.split(',')
        if int(line[5]) < 2005:
            # with open(f'{line[1]}.txt', 'w') as massage:
            #     massage.write(f'Hurmaltli {line[1], line[2]}!\n'
            #           f'{line[4]} Rusumli {line[5]}-yilda ishlab chiqarilgan \n'
            #           f'mashinangizni, texnik ko"rinkdan o"tkazishingizni so"raymiz.\n')

            print(f'Hurmaltli {line[1], line[2]}!\n'
                  f'{line[4]} Rusumli {line[5]}-yilda ishlab chiqarilgan \n'
                  f'mashinangizni, texnik ko"rinkdan o"tkazishingizni so"raymiz.\n')