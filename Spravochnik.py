import json
def save():
    with open("phonebook.json","w", encoding="utf-8") as ph:
        ph.write(json.dumps(users,ensure_ascii=False))
def load():
    with open("phonebook.json","r",encoding="utf-8") as ph:
            users = json.load(ph)
    return users
try:
    users=load()
except:
    users={}
    save()
if len(users)==0:
    id = users['vsego_id'] = '0'
else:
    id=int(users['vsego_id'])
save()
print('==============================================')
print('==============================================')
print('====ВАС ПРИВЕТСТВУЕТ ТЕЛЕФОННЫЙ СПРАВОЧНИК====')
print('==============================================')
while True:
    users = load()
    print('==============================================')
    print('1 - Добавить контакт \n2 - Показать контакты \n3 - Удалить \n4 - Редактировать \n5 - Поиск \n6 - Выход')
    command = input('Введите команду: ')
    if command == '1':
        name = input('Введите Имя: ')
        surname = input('Введите Фамилию: ')
        telephone = input('Введите Телефонный номер: ')
        date_of_birth = input('Введите Дату Рождения: ')
        mail = input('Введите Почту: ')
        data = [name,surname,telephone,date_of_birth,mail]

        id += 1
        users['id:'+str(id)] = data
        users['vsego_id']=str(id)
        print('+++Запись добавлена+++')
    elif command == '2':
            print('----------------------------------------')
            for k, v in users.items(): 
                print(k,*v)
            print('----------------------------------------') 
    elif command == '3':
        i = input('Какой id вхотите удалить? ')
        try:
            del users['id:'+i]
            print('---запись удалена---')   
        except:       
            print('---запись несуществует---')
    elif command == '4':
        i = input('Какую запись(id) вы хотите изменить? ')
        if ('id:'+i) in users.keys():
            print('1 - Всё  2 - Имя  3 - Фамилия  4 - Телефон  5 - Дату  6 - Почту')
            command = input('Что вы хотите изменить? ')
            if command == '1':
                name = input('Введите Имя: ')
                surname = input('Введите Фамилию: ')
                telephone = input('Введите Телефонный номер: ')
                date_of_birth = input('Введите Дату Рождения: ')
                mail = input('Введите Почту: ')
                data = [name,surname,telephone,date_of_birth,mail]
                users['id:'+i] = data
                print('запись успешно изменина')
            elif command == '2':
                data = users['id:'+i]
                data[0] = input('Введите Новое Имя: ')
                users['id:'+i] = data
                print('-+-запись успешно изменена-+-')
            elif command == '3':
                data = users['id:'+i]
                data[1] = input('Введите Новую Фамилию: ')
                users['id:'+i] = data
                print('-+-запись успешно изменена-+-')
            elif command == '4':
                data = users['id:'+i]
                data[2] = input('Введите Новый Номер: ')
                users['id:'+i] = data
                print('-+-запись успешно изменена-+-')
            elif command == '5':
                data = users['id:'+i]
                data[3] = input('Введите Новую Дату: ')
                users['id:'+i] = data
                print('-+-запись успешно изменена-+-')
            elif command == '6':
                data = users['id:'+i]
                data[4] = input('Введите Новую Почту: ')
                users['id:'+i] = data
                print('-+-запись успешно изменена-+-')
            else:
                print('!!!Команда неизвестна!!!')
        else:
            print('---запись несуществует---')
    elif command == '5':
        i = input('Введите любое значение для поиска: ').lower()
        print('***Результаты поиска ниже***')
        for k, v in users.items(): 
            if (str(v).lower()).find(i) > -1:
                print(k,*v)
        print('***Результаты поиска выше***')   
    elif command == '6': 
        break
    else:
        print('!!!Команда неизвестна!!!')
    save()


        




               

