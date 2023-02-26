import vk_api
from config import all_token
import time

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

    session = vk_api.VkApi(token=all_token)
    vk = session.get_api()
    ID = str(input('Введите Ваш ID: '))
    # Получить ID - https://regvk.com/

    print('=================ПОЛУЧАЕМ СПИСОК ВАШИХ ДРУЗЕЙ==========================')
    print(f'========================ВАШ ID {ID}===============================')


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

    def send_messages(send_id):
        while True:
            vk.messages.send(peer_id=int(input('Введите числовой id кому отправить сообщение: ')),
                             message=str(input('Введите текст письма: ')), random_id=0)

            s = '|'
            for i in range(11):
                time.sleep(0.05)
                print('\r', 'Отправка', i * s, str(i) + str(0), '%', end='')
            print(f'\nСообщение отправлено!︎')



    get_friens(ID)
    send_messages(ID)

except KeyboardInterrupt:
    print('Goodbye!')
