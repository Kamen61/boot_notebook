import telebot
import json

import add_contact
import del_contact
import serch_and_show_contacts

# creat json fail
# book = {'Василий Васильевич':{'phones':['8(495)192-28-34','8(495)254-16-51'],'mail':'vasya@mail.com','birthday':'25.01.1990'},
#         'Петя Петрович':{'phones':['8(495)680-78-57','8(495)118-22-05'],'mail':'vasya@mail.com','birthday':'25.01.1990'},
#         'Владимир Владимирович':{'phones':['8(495)865-71-22','8(495)146-08-02'],'mail':'vasya@mail.com','birthday':'25.01.1990'},
#         'Александр Александрович':{'phones':['8(495)671-22-32','8(495)406-70-15'],'mail':'vasya@mail.com','birthday':'25.01.1990'},
#         'Николай Николаевич':{'phones':['8(495)717-35-57','8(495)561-08-94'],'mail':'vasya@mail.com','birthday':'25.01.1990'},
#         'Сергей Сергеевич':{'phones':['8(495)475-80-36','8(495)084-70-37'],'mail':'vasya@mail.com','birthday':'25.01.1990'}}
# with open('sw_templates.json', 'w') as f:
#     json.dump(book, f)


API_TOKEN = '5899153603:AAHs10vl9WXO1JEp2BseytmORro4drvscRQ'



bot = telebot.TeleBot(API_TOKEN)

serch_name=''
list_contact_add=[]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Вы зашли в телефонную книгу")
    bot.send_message(message.chat.id, "Команда /add Поможет вам добавить контакт")
    bot.send_message(message.chat.id, "Команда /del Поможет вам удалить контакт")
    bot.send_message(message.chat.id, "Команда /search Поможет вам добавить контакт")
    bot.send_message(message.chat.id, "Команда /show Поможет вам добавить контакт")



@bot.message_handler(commands=['add'])
def start_message(message):
    bot.send_message(message.chat.id, "Введите полное имя контакта для добавления :")
    bot.register_next_step_handler(message,full_name)



@bot.message_handler(commands=['del'])
def start_message(message):
    bot.send_message(message.chat.id, "Введите полное имя контакта для удаления :")
    bot.register_next_step_handler(message,delet)


@bot.message_handler(commands=['search'])
def start_message(message):
    bot.send_message(message.chat.id, "Введите полное имя контакта для поиска :")
    bot.register_next_step_handler(message,serch)

@bot.message_handler(commands=['show'])
def start_message(message):
    bot.send_message(message.chat.id, "Весь список контактов:")
    bot.send_message(message.chat.id, serch_and_show_contacts.show())



# ----------------------------------------------------------------------------
@bot.message_handler(content_types='text')
def full_name(message):
    bot.send_message(message.chat.id, "Введите номер контакта (можно вводить несколько номеров через запятую):")
    list_contact_add.append(message.text)
    bot.register_next_step_handler(message, phones)
    # print(list_contact_add)

@bot.message_handler(content_types='text')
def phones(message):
    if add_contact.check_value_numbers(message.text):
        list_contact_add.append(add_contact.list_phones(message.text))
        bot.send_message(message.chat.id, "Введите электронную почту :")
        bot.register_next_step_handler(message, mail)
        print(list_contact_add)
    else:
        bot.send_message(message.chat.id, "Введите номер корректно")
        bot.register_next_step_handler(message, phones)


@bot.message_handler(content_types='text')
def mail(message):
    if add_contact.check_mail(message.text):
        list_contact_add.append(message.text.replace('',''))
        bot.send_message(message.chat.id, "Введите дату дня рождения в формате DD.MM.YYYY:")
        bot.register_next_step_handler(message, birthday)
    else:
        bot.send_message(message.chat.id, "Введите почту корректно")
        bot.register_next_step_handler(message, mail)


@bot.message_handler(content_types='text')
def birthday(message):
    text=message.text.replace(' ','')
    if add_contact.check_birthday(text):
        list_contact_add.append(message.text)
        name_contact,param_contact=add_contact.add_contact_in_dict(list_contact_add)
        print(name_contact)
        print(param_contact)
        add_contact.add_in_book(name_contact,param_contact)
        bot.send_message(message.chat.id, "Контакт добавлен !")
        bot.register_next_step_handler(message, start_message)
    else:
        bot.send_message(message.chat.id, "Введите дату корректно")
        bot.register_next_step_handler(message, birthday)




# ----------------------------------------------------------------------------
@bot.message_handler(content_types='text')
def serch(message):
    answer=serch_and_show_contacts.serch_in_book(message.text)
    if answer:
        bot.send_message(message.chat.id, answer)
    else:
        bot.send_message(message.chat.id, "Введенный контак не найден, попробуйте еще раз")
        bot.register_next_step_handler(message, serch)



# ----------------------------------------------------------------------------
@bot.message_handler(content_types='text')
def delet(message):
    if del_contact.del_cont(message.text):
        bot.send_message(message.chat.id, "Контак удален !")
    else:
        bot.send_message(message.chat.id, "Введенный контак не найден")
        bot.send_message(message.chat.id, "Для того чтобы увидеть все контакты, воспользуйтесь функцией ")
        bot.register_next_step_handler(message, delet)






bot.polling()

# @bot.message_handler(commands=['search'])
# def start_message(message):



# @bot.message_handler(content_types='text')
# def delet(message):

# bot.polling()
