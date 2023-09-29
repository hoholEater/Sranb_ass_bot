
import html
import telebot
import datetime
import threading
import random


chat_id = '-'

bot = telebot.TeleBot('')

test = False
test = True

string_for_izum = "����������� ���������������, ������ ������������, ������������ ����������, ���������������� �������������,\
               �������������� ������������, ����� ������������, ���� ���� ���� ���������� ������, �������� �����������������,\
               ���� �� ���� �����������, �������������� ����������, ��� ���� � ������ ����� �������� ������,\
               �������� ���� ������� ��������� ����� ��������� �����, ������������� ��������������� ��������������,\
               �������������� ������� ��������� ���������� ������, �������������������������������������������� ���������������, ������ � ��������,\
               �������� ������������� ���������� � ����� ��������������� ��������,�������������� ������������, �������� ����������,\
               ����� ����������, �������� ������,������������� ������������,���������������� ������������,\
               �������� ���� � �������� ����� ��������� � ������� ����,������������ �������������,���� ����� ����������,������������ ������������,\
               ����������� �����������������,�����,�����,�����,�����,������,�������,����, �����, �����, �����, ������, ������, ��������, ��������,\
               �����, �����, �������, �����, �����, ������, �������, �������, ���������, �������, ��������, ���������, ��������, �������, ������,\
               ����, �����������, ��������, �������, ��������, ���, �����, ����, ����, �����, ������, ���, ���������, �������, ��������, �����,\
               ������, ����, ������, �������, ��, �������, ������, ������, ����, ��������, �������, ��������, �������, ������, ������, �������,\
               ������, �������, ������, �������, �������, �������, ������, ������, ��������, ������, ��������, ������, ������, ����� � ������"

massiv_izuma = string_for_izum.split(',')


@bot.message_handler(commands=['start'])
def start_message(message):
    now = datetime.datetime.now()
    if now.time() > datetime.time(19,00,00):
        bot.send_message(message.chat.id,"������, ����������.")

    bot.send_message(message.chat.id,'������������ ��������� ����, �� ������ �����!')
    
    print("start ������� �� - " + str(threading.active_count()))
    start_routine()
    print("������� - " + str(threading.active_count()))

        
@bot.message_handler(commands=['avesranb'])
def avesranb_message(message):
    bot.send_message(message.chat.id,'AVE SRANb!111!11')

@bot.message_handler(commands=['help'])
def avesranb_message(message):
    bot.send_message(message.chat.id,'���� � ���� �� �������. Dinahoi.')

@bot.message_handler(commands=['test'])
def test_message(message):

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("��������!", callback_data = 'add_me'))
    markup.add(telebot.types.InlineKeyboardButton("������� ����������.", callback_data = 'roll'))
   
    bot.send_message(message.chat.id, "��������... ������������ �� @"+ message.from_user.username )
    bot.send_message(message.chat.id, message.text, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types='text')
def get_text_messages(message):
    
    if "���������" in str.lower(message.text):
        bot.send_message(message.chat.id, "�� ���������");
    elif "����" in str.lower(message.text):
        bot.send_message(message.chat.id, "� �� ������ ����, ��� ���� ������ ������ " +str(random.randint(1, 125))+ " ��., @" +message.from_user.username);
    elif ("�������" in str.lower(message.text)) and answer():
        bot.send_message(message.chat.id, "�������� ��� � ����, ��� ��� �����, @" +message.from_user.username);
    elif message.from_user.username == "xxxizymxxx":
        bot.send_message(message.chat.id, "����, " + str.lower(massiv_izuma[random.randint(0, len(massiv_izuma))]).strip() + ", �������.");

def answer():

    return random.randint(1, 100) > 50

def start_routine():
    
    print("start routine ������� - " + str(threading.active_count()))
    
    if threading.active_count() > 6:    
        return
        
    now = datetime.datetime.now()
    if now.time() > datetime.time(19,00,00):
        future_date = datetime.datetime.today() + datetime.timedelta(days=1)
        tomorrow = future_date.strftime("%Y-%m-%d")
        time_massive = [tomorrow + " 00:54:55",tomorrow + " 05:04:55", tomorrow + " 9:04:55",tomorrow + " 14:04:55",tomorrow + " 19:04:55"]
        reminder_set(time_massive)
        time_massive = [tomorrow + " 9:36:55",tomorrow + " 14:36:55",tomorrow + " 19:36:55"]
        reminder_set_jump(time_massive)
    else:
        today = datetime.datetime.today().strftime("%Y-%m-%d")
        time_massive = [today + " 00:54:55",today + " 05:04:55", today + " 9:04:55",today + " 14:04:55",today + " 19:04:55"]
        reminder_set(time_massive)
        time_massive = [today + " 9:36:55",today + " 14:36:55",today + " 19:36:55"]
        if test:
            t1 = now + datetime.timedelta(seconds=30)
            t2 = t1 + datetime.timedelta(seconds=30)
            
            time_massive = [t1.strftime('%Y-%m-%d %H:%M:%S'),t2.strftime('%Y-%m-%d %H:%M:%S')]
        reminder_set_jump(time_massive)

    print("������� - " + str(threading.active_count()))
    
    for thread in threading.enumerate():
        print("Thread name is %s." % thread.name)



def reminder_set(time_massive):
    
    result_text = ''
    
    for i in range(len(time_massive)):
        try:
            reminder_time = datetime.datetime.strptime(time_massive[i], '%Y-%m-%d %H:%M:%S')
            now = datetime.datetime.now()
            delta = reminder_time - now

            if delta.total_seconds() > 0:
                reminder_name = '������'
                reminder_timer = threading.Timer(delta.total_seconds(), send_reminder, [chat_id, reminder_name])
                reminder_timer.start()
                result_text = result_text + '\n'+str(time_massive[i])

        except ValueError:
            bot.send_message(chat_id, '��� ��������� ������� ����� ���-�� ����� �� ���.')

   # if datetime.datetime.now().time() > datetime.time(19,00,00):
    if result_text != '':
        bot.send_message(chat_id, '����������� ������� ���� ����� ����������� ��:' + result_text)
        
def reminder_set_jump(time_massive):
    result_text = ''
    for i in range(len(time_massive)):
        try:

            reminder_time = datetime.datetime.strptime(time_massive[i], '%Y-%m-%d %H:%M:%S')
            now = datetime.datetime.now()
            delta = reminder_time - now

            if delta.total_seconds() > 0:
                reminder_name = '������'
                reminder_timer = threading.Timer(delta.total_seconds(), send_reminder, [chat_id, reminder_name])
                reminder_timer.start()
                result_text = result_text + '\n'+str(time_massive[i])

        except ValueError:
            bot.send_message(chat_id, '��� ��������� ������� ������� ���-�� ����� �� ���.')

  #  if datetime.datetime.now().time() > datetime.time(19,00,00):
    if result_text != '':
       bot.send_message(chat_id, '����������� ������� � ������ ����������� ��:' + result_text)
          
        
def send_reminder(chat_id, reminder_name):
    
    print("reminder ������� �� - " + str(threading.active_count()))
    
    if reminder_name == '������':
        mess = bot.send_message(chat_id, '����� ������ ����!')
        bot.pin_chat_message(chat_id, mess.message_id)
        bot.unpin_chat_message(chat_id, mess.message_id)
    else:
        mess = bot.send_message(chat_id, '������ � ����������, ��������!')
        bot.pin_chat_message(chat_id, mess.message_id)
        bot.unpin_chat_message(chat_id, mess.message_id)
        
    print("reminder ������� - " + str(threading.active_count()))

    start_routine()


bot.polling(none_stop=True, interval=0); 



