def send_email (mesage, recipient, *, sender = 'university.help@gmail.com'):
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")) or "@" not in sender or not sender.endswith ((".com", ".ru", ".net")):
        print ("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!') # А почему нельзя? Можно же!!!
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    elif sender != 'university.help@gmail.com':
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!!! Письмо отравлено!!!'
              'Его отправил некий', sender, 'на Ваш адрес', recipient)
send_email('Письмо дедушке', 'lukash@mail.bu')
send_email('Второе письмо дедушке', 'lukash@mail.bu', sender = 'vnuk@sobaka.ru')
send_email('Тест работы почты', 'sasha@mail.ru', sender = 'sasha@mail.ru')
send_email('Здравтвуйте, Вы в деле!', 'alexlast@mail.net')
send_email('Выпей йаду', 'james.bond@super.com', sender = 'killer@boom.ru')