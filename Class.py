class Animals:
    hunger_level = 'hungry'
    def __init__(self,animal_name,animal_voice,animal_weight):
        self.animal_name = animal_name
        self.animal_voice = animal_voice
        self.animal_weight = animal_weight

    def Feed(self):
        self.hunger_level = 'full'

class Cow(Animals):
    milk_status = 'Full'

    def Milk(self):
        self.milk_status = 'Empty'

class Goat(Cow):
    def Milk(self):
        super().Milk()

class Sheep(Animals):
    wool = 'have'

    def haircut(self):
        self.wool = 'bald'
class Chicken(Animals):
    eggs = 'not collected'

    def collecting_eggs(self):
        self.eggs = 'collected'

class Duck(Chicken):
    def collecting_eggs(self):
        super().collecting_eggs()

class Goose(Chicken):

    def collecting_eggs(self):
        super().collecting_eggs()

list_of_animals = {}
list_of_cow = {}
list_of_chiken = {}
list_of_duck = {}
list_of_goose = {}
list_of_sheep = {}
list_of_goat = {}
while True:
    class_of_animal = input('Write "next step" or class of animal\n'
                            '"Chicken" "Goat" "Cow" "Sheep" "Duck" "Goose": ')
    if class_of_animal == 'next step':
        break
    name = input("Write name of animal: ")
    voice = input("Write voice of animal: ")
    weight = int(input('Write weight of animal: '))
    if class_of_animal == 'Cow':
        k = name
        k = Cow(name, voice, weight)
        list_of_animals[k] = {'Name': name}, {'Voice': voice}, {'Weight': weight}
        list_of_cow[k] = name
    elif class_of_animal == 'Goat':
        k = name
        k = Goat(name, voice, weight)
        list_of_animals[k] = {'Name': name}, {'Voice': voice}, {'Weight': weight}
        list_of_goat[k] = name
    elif class_of_animal == 'Chicken':
        k = name
        k = Chicken(name, voice, weight)
        list_of_animals[k] = {'Name': name}, {'Voice': voice}, {'Weight': weight}
        list_of_chiken[k] = name

    elif class_of_animal == 'Duck':
        k = name
        k = Duck(name, voice, weight)
        list_of_animals[k] = {'Name': name}, {'Voice': voice}, {'Weight': weight}
        list_of_duck[k] = name
    elif class_of_animal == 'Goose':
        k = name
        k = Goose(name, voice, weight)
        list_of_animals[k] = {'Name': name}, {'Voice': voice}, {'Weight': weight}
        list_of_goose[k] = name
    elif class_of_animal == 'Sheep':
        k = name
        k = Sheep(name, voice, weight)
        list_of_animals[k] = {'Name': name}, {'Voice': voice}, {'Weight': weight}
        list_of_sheep[k] = name
print(list_of_animals)
print(list_of_chiken,list_of_cow,list_of_sheep,list_of_goose,list_of_duck,list_of_goat)
while True:
    do = input('What are you going to do next?\n'
               'Write "exit"\n'
               '"ch" to check status of hungry\n'
               '"tm" to take milk \n'
               '"hc" to do haircut \n'
               '"te" to take eggs \n'
               '"cw" to calculate weight of all animals in class ')
    if do == 'ch':
        type_of_animal = input('Write "exit" or which type of animal do you want to check?\n'
                               '"Chicken" "Goat" "Cow" "Sheep" "Duck" "Goose" "all": ')
        if type_of_animal == 'all':
            for k,v in list_of_animals.items():
                print(f"{v}  is {k.hunger_level}")
            type_of_animal = input('Do you want to feed them? ')
            if type_of_animal == 'yes':
                for k,v in list_of_animals.items():
                    k.Feed()
                    print(f"{v} is {k.hunger_level}")
                else:
                    continue
        elif type_of_animal == 'Chicken':
            if len(list_of_chiken) == 0:
                print('You dont have Chicken')
                continue
            for k,v in list_of_chiken.items():
                print(f"{v}  is {k.hunger_level}")
                type_of_animal = input('Do you want to feed them? \n "yes" or "not": ')
                if type_of_animal == 'yes':
                    for k,v in list_of_chiken.items():
                        k.Feed()
                        print(f"{v}  is {k.hunger_level}")
                    else:
                        continue
        elif type_of_animal == 'Goat':
            if len(list_of_goat) == 0:
                print('You dont have Goat')
                continue
            for k, v in list_of_goat.items():
                print(f"{v}  is {k.hunger_level}")
                type_of_animal = input('Do you want to feed them? \n "yes" or "not": ')
                if type_of_animal == 'yes':
                    for k, v in list_of_goat.items():
                        k.Feed()
                        print(f"{v}  is {k.hunger_level}")
                    else:
                        continue
        elif type_of_animal == 'Cow':
            if len(list_of_cow) == 0:
                print('You dont have Cow')
                continue
            for k, v in list_of_cow.items():
                print(f"{v}  is {k.hunger_level}")
                type_of_animal = input('Do you want to feed them? \n "yes" or "not": ')
                if type_of_animal == 'yes':
                    for k, v in list_of_cow.items():
                        k.Feed()
                        print(f"{v}  is {k.hunger_level}")
                    else:
                        continue
        elif type_of_animal == 'Duck':
            if len(list_of_duck) == 0:
                print('You dont have Duck')
                continue
            for k, v in list_of_duck.items():
                print(f"{v}  is {k.hunger_level}")
                type_of_animal = input('Do you want to feed them? \n "yes" or "not": ')
                if type_of_animal == 'yes':
                    for k, v in list_of_duck.items():
                        k.Feed()
                        print(f"{v}  is {k.hunger_level}")
                    else:
                        continue
        elif type_of_animal == 'Goose':
            if len(list_of_goose) == 0:
                print('You dont have Goose')
                continue
            for k, v in list_of_goose.items():
                print(f"{v}  is {k.hunger_level}")
                type_of_animal = input('Do you want to feed them? \n "yes" or "not": ')
                if type_of_animal == 'yes':
                    for k, v in list_of_goose.items():
                        k.Feed()
                        print(f"{v}  is {k.hunger_level}")
                    else:
                        continue
        elif type_of_animal == 'Sheep':
            if len(list_of_sheep) == 0:
                print('You dont have Sheep')
                continue
            for k, v in list_of_sheep.items():
                print(f"{v}  is {k.hunger_level}")
                type_of_animal = input('Do you want to feed them? \n "yes" or "not": ')
                if type_of_animal == 'yes':
                    for k, v in list_of_sheep.items():
                        k.Feed()
                        print(f"{v}  is {k.hunger_level}")
                    else:
                        continue
        elif type_of_animal == 'exit':
            break
    elif do == 'exit':
        print('See you!')
        break

    elif do == 'tm':
        type_of_animal = input('You can milk only next animals:\n"Goat" "Cow" "all" these \nYour decision? ')
        if type_of_animal == 'all':
            if len(list_of_cow) == 0 and len(list_of_goat) == 0:
                print('You dont have this animals')
                continue
            for k,v in list_of_cow.items():
                k.Milk()
                print(f'{v} now is {k.milk_status}')
            for k,v in list_of_goat.items():
                k.Milk()
                print(f'{v} now is {k.milk_status}')
        elif type_of_animal == 'Goat':
            if  len(list_of_goat) == 0:
                print('You dont have this animals')
                continue
            for k,v in list_of_goat.items():
                k.Milk()
                print(f'{v} now is {k.milk_status}')
        elif type_of_animal == 'Cow':
            if len(list_of_cow) == 0:
                print('You dont have this animals')
                continue
            for k, v in list_of_cow.items():
                k.Milk()
                print(f'{v} now is {k.milk_status}')
        else:
            continue

    elif do == 'hc':
        if len(list_of_sheep) == 0:
            print('You dont have this animal')
            continue
        type_of_animal = input('Do you want to do haircut for "all" sheep or for "one"? ')
        if type_of_animal == 'all':
            for k,v in list_of_sheep.items():
                k.haircut()
                print(f'{v} now is {k.wool}')
        elif type_of_animal == 'one':
            for k,v in list_of_sheep.items():
                print(f'{v} --> {k.wool}')
            type_of_animal = input('Write name of sheep: ')
            if type_of_animal not in list_of_sheep:
                print('You dont have this sheep')
                continue
            for k,v in list_of_sheep.items():
                if v == type_of_animal:
                    k.haircut()
                    print(f'{v} now is {k.wool}')

    elif do == 'te':
        if len(list_of_chiken) == 0 and len(list_of_duck) == 0 and len(list_of_goose) ==0:
            print('You can not take eggs because you dont have animals')
        for k,v in list_of_chiken.items():
            k.collecting_eggs()
            print(f'Your take eggs from{v}. Now status is {k.eggs}')
        for k,v in list_of_duck.items():
            k.collecting_eggs()
            print(f'Your take eggs from{v}. Now status is {k.eggs}')
        for k,v in list_of_goose.items():
            v.collecting_eggs()
            print(f'Your take eggs from{v}. Now status is {k.eggs}')

    elif do ==  'cw':
        dict_of_weight_all_in_class = {}
        dict_of_weight_all = {}
        sum_weight = 0
        type_of_animal = input('Which weight you want to calculate? ')
        if type_of_animal == 'Cow':
            for k,v in list_of_cow.items():
                sum_weight += k.animal_weight
                dict_of_weight_all_in_class[k] = k.animal_weight
            print(f'so,weight of all {type_of_animal}s is {sum_weight}')
            for k,v in dict_of_weight_all_in_class.items():
                z = max(dict_of_weight_all_in_class.values())
                if z == v:
                    print(f'The heaviest animal in class {type_of_animal }have name {k.animal_name} and weight {v}')

        elif type_of_animal == 'Goat':
            for k,v in list_of_goat.items():
                sum_weight += k.animal_weight
                dict_of_weight_all_in_class[k] = k.animal_weight
            print(f'so,weight of all {type_of_animal}s is {sum_weight}')
            for k,v in dict_of_weight_all_in_class.items():
                z = max(dict_of_weight_all_in_class.values())
                if z == v:
                    print(f'The heaviest animal in class {type_of_animal }have name {k.animal_name} and weight {v}')

        elif type_of_animal == 'Goose':
            for k,v in list_of_goose.items():
                sum_weight += k.animal_weight
                dict_of_weight_all_in_class[k] = k.animal_weight
            print(f'so,weight of all {type_of_animal}s is {sum_weight}')
            for k, v in dict_of_weight_all_in_class.items():
                z = max(dict_of_weight_all_in_class.values())
                if z == v:
                    print(f'The heaviest animal in class {type_of_animal }have name {k.animal_name} and weight {v}')

        elif type_of_animal == 'Chicken':
            for k,v in list_of_chiken.items():
                sum_weight += k.animal_weight
                dict_of_weight_all_in_class[k] = k.animal_weight
            print(f'so,weight of all {type_of_animal}s is {sum_weight}')
            for k,v in dict_of_weight_all_in_class.items():
                z = max(dict_of_weight_all_in_class.values())
                if z == v:
                    print(f'The heaviest animal in class {type_of_animal }have name {k.animal_name} and weight {v}')

        elif type_of_animal == 'Duck':
            for k,v in list_of_duck.items():
                sum_weight += k.animal_weight
                dict_of_weight_all_in_class[k] = k.animal_weight
            print(f'so,weight of all {type_of_animal}s is {sum_weight}')
            for k,v in dict_of_weight_all_in_class.items():
                z = max(dict_of_weight_all_in_class.values())
                if z == v:
                    print(f'The heaviest animal in class {type_of_animal }have name {k.animal_name} and weight {v}')

        elif type_of_animal == 'Sheep':
            for k,v in list_of_sheep.items():
                sum_weight += k.animal_weight
                dict_of_weight_all_in_class[k] = v.animal_weight
            print(f'so,weight of all {type_of_animal}s is {sum_weight}')
            for v in dict_of_weight_all_in_class.values():
                z = max(dict_of_weight_all_in_class.values())
                if z == v:
                    print(f'The heaviest animal in class {type_of_animal }have name {k} and weight {v}')

        elif type_of_animal == 'all':
            for k in list_of_animals.keys():
                sum_weight += k.animal_weight
                dict_of_weight_all[k] = k.animal_weight
            z = max(dict_of_weight_all)
            print(f'The heaviest animal have name {k.animal_name} and weight {k.animal_weight}')





