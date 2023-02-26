import vk_api
import time
import configparser

try:
    print('''.................................................__________......
         .... _________________________________________ ./           \\___
         .___/             /..|        /_/   _____   |_ |   _______   ||..
         .__/ ____       //...|   ____/  |  |.....| ||..|  /...||...\ ||..
         ../_____/      //....|   || ....|  |_____| ||..|   ___||___  ||..
         ......./      //.....|   |____..|       ___||..|  |___  ___| ||..
         ....../      //......|    ___/..|   |\   \\ ...|   ...||...  ||..
         ...../      //.......|   || ....|   |.\   \\ ..|   ...||...  ||..
         ..../      //_______ |   |______|_  |..\   \\ .|  \___||___/ ||..
         .../  ____________ /_|           /  |__.\   \\ |             ||..
         __/_______________/.\___________/_____/..\___\\\____________//...\n''')

    config = configparser.ConfigParser()
    config.read("config.ini")
    session = vk_api.VkApi(token=config['VK']['token'])
    vk = session.get_api()
    print('Получить токен - "https://vkhost.github.io/"')
    print('Получить ID - "https://regvk.com/"')
    ID = str(input('Введите Ваш ID: '))

    print(f'========================ВАШ ID {ID}===============================')
    print('=================ПОЛУЧАЕМ СПИСОК ВАШИХ ДРУЗЕЙ==========================')


    def get_friens(user_id):
        friends = session.method('friends.get', {'user_id': user_id})
        online = session.method('friends.getOnline', {'user_id': user_id})
        for friend_id, friend in enumerate(friends['items']):
            user = session.method('users.get', {'user_ids': friend})
            print(f'{friend_id + 1}: {user[0]["id"]}, {user[0]["first_name"]}, {user[0]["last_name"]}')
        print('')
        for onl in friends['items']:
            if onl in online:
                user = session.method('users.get', {'user_ids': onl})
                print(f'Status online: {user[0]["id"]}, {user[0]["first_name"]}, {user[0]["last_name"]}')
        print('')


    get_friens(ID)

    try:
        def send_messages(send_id):
            while True:
                vk.messages.send(peer_id=int(input('Введите числовой id кому отправить сообщение: ')),
                                 message=str(input('Введите текст письма: ')), random_id=0)

                s = '|'
                for i in range(11):
                    time.sleep(0.05)
                    print('\r', 'Отправка', i * s, str(i) + str(0), '%', end='')
                print(f'\nСообщение отправлено!︎')


        send_messages(ID)

    except ValueError:
        print('Синтаксическая ошибка!\nПроверьте правильность заполнения полей!')

except KeyError:
    print('Не указан токен в config.ini!')

except vk_api.exceptions.ApiError:
    print('Указан неверный ID или токен!')

except KeyboardInterrupt:
    print('\nGoodbye!')
