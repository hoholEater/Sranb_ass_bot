
import html
import telebot
import datetime
import threading
import random


chat_id = '-'

bot = telebot.TeleBot('')

test = False
test = True

string_for_izum = "пиздобратия мандопроушечная, уебище залупоглазое, дрочепиздище хуеголовое, пробиздоблядская мандопроушина,\
               гнидопаскудная хуемандовина, блядь семитаборная, чтоб тебя всем столыпином харили, охуевшее блядепиздопроёбище,\
               чтоб ты хуем поперхнулся, долбоебическая пиздорвань, хуй тебе в глотку через анальный проход,\
               распизди тебя тройным перебором через вторичный переёб, пиздоблятское хуепиздрическое мудовафлоебище,\
               мудовафлоебище сосущее километры трипперных членов, трихломидозопиздоеблохуеблядеперепиздическая спермоблевотина, гондон с гонореей,\
               блядская пиздапроебина охуевающая в своей пидарастической сущности,Хуелептический пиздопрозоид, еблоухий мандохвост,\
               сосун хуеголовый, пидрасня ебаная,Залупоголовая блядоящерица,Трипиздоблядская промудохуина,\
               Распроеб твою в крестище через коромысло в копейку мать,Членососущий вафломеханизм,лунь пизду склевавший,Мордоблядина залупоглазая,\
               Склипездень двужопостворчатый,Пидор,Хуйло,Хохол,Чурка,Уебень,Говноед,сука, пидор, блядь, мудло, уебище, ебосос, хуисоска, педрилка,\
               вафел, еблан, пидарас, уебок, хуила, мудила, блядина, уебанок, трахарила, ебарила, гавносос, миньетчик, пидэраст, пиздоеб, дрочер,\
               жопа, сцукаблянах, пиздарас, хуеплет, пиздолиз, хуй, мудак, хуяк, ебак, сцука, уебина, чмо, вафлеглот, гавноеб, захуятор, пидар,\
               хуиман, хуеб, ёблядь, хуёблядь, еб, ебалдуй, пиздун, хуесос, ебил, выблядок, гавноед, гавнажуй, долбаеб, выебок, мудоеб, обмудок,\
               овцееб, свиноеб, ебозер, ахуятэр, хуетрон, хуеглот, мудень, залупа, злоуебок, гандон, хуесрань, пиздец, пиздюк, хуйло и параша"

massiv_izuma = string_for_izum.split(',')


@bot.message_handler(commands=['start'])
def start_message(message):
    now = datetime.datetime.now()
    if now.time() > datetime.time(19,00,00):
        bot.send_message(message.chat.id,"Привет, полуёбошные.")

    bot.send_message(message.chat.id,'Производится настройка бота, не лезьте блядб!')
    
    print("start Потоков до - " + str(threading.active_count()))
    start_routine()
    print("Потоков - " + str(threading.active_count()))

        
@bot.message_handler(commands=['avesranb'])
def avesranb_message(message):
    bot.send_message(message.chat.id,'AVE SRANb!111!11')

@bot.message_handler(commands=['help'])
def avesranb_message(message):
    bot.send_message(message.chat.id,'Тебе и врач не поможет. Dinahoi.')

@bot.message_handler(commands=['test'])
def test_message(message):

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Участвую!", callback_data = 'add_me'))
    markup.add(telebot.types.InlineKeyboardButton("Выбрать победителя.", callback_data = 'roll'))
   
    bot.send_message(message.chat.id, "Внимание... ДЛАНЕКОНКУРС от @"+ message.from_user.username )
    bot.send_message(message.chat.id, message.text, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types='text')
def get_text_messages(message):
    
    if "пидорните" in str.lower(message.text):
        bot.send_message(message.chat.id, "Ну пидорните");
    elif "член" in str.lower(message.text):
        bot.send_message(message.chat.id, "Я по глазам вижу, что твой пчленб длиной " +str(random.randint(1, 125))+ " см., @" +message.from_user.username);
    elif ("попобав" in str.lower(message.text)) and answer():
        bot.send_message(message.chat.id, "Попобава лох и казёл, это все знают, @" +message.from_user.username);
    elif message.from_user.username == "xxxizymxxx":
        bot.send_message(message.chat.id, "Изюм, " + str.lower(massiv_izuma[random.randint(0, len(massiv_izuma))]).strip() + ", динахой.");

def answer():

    return random.randint(1, 100) > 50

def start_routine():
    
    print("start routine Потоков - " + str(threading.active_count()))
    
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

    print("Потоков - " + str(threading.active_count()))
    
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
                reminder_name = 'Пилить'
                reminder_timer = threading.Timer(delta.total_seconds(), send_reminder, [chat_id, reminder_name])
                reminder_timer.start()
                result_text = result_text + '\n'+str(time_massive[i])

        except ValueError:
            bot.send_message(chat_id, 'При установке времени ярены что-то пошло не так.')

   # if datetime.datetime.now().time() > datetime.time(19,00,00):
    if result_text != '':
        bot.send_message(chat_id, 'Напоминание СПИЛИТЬ ЛАХА НАХОЙ установлено на:' + result_text)
        
def reminder_set_jump(time_massive):
    result_text = ''
    for i in range(len(time_massive)):
        try:

            reminder_time = datetime.datetime.strptime(time_massive[i], '%Y-%m-%d %H:%M:%S')
            now = datetime.datetime.now()
            delta = reminder_time - now

            if delta.total_seconds() > 0:
                reminder_name = 'Подзем'
                reminder_timer = threading.Timer(delta.total_seconds(), send_reminder, [chat_id, reminder_name])
                reminder_timer.start()
                result_text = result_text + '\n'+str(time_massive[i])

        except ValueError:
            bot.send_message(chat_id, 'При установке времени запрыга что-то пошло не так.')

  #  if datetime.datetime.now().time() > datetime.time(19,00,00):
    if result_text != '':
       bot.send_message(chat_id, 'Напоминание ПРЫГАТЬ В ПОДЗЕМ установлено на:' + result_text)
          
        
def send_reminder(chat_id, reminder_name):
    
    print("reminder Потоков до - " + str(threading.active_count()))
    
    if reminder_name == 'Пилить':
        mess = bot.send_message(chat_id, 'Время пилить лаха!')
        bot.pin_chat_message(chat_id, mess.message_id)
        bot.unpin_chat_message(chat_id, mess.message_id)
    else:
        mess = bot.send_message(chat_id, 'ПРЫГАЙ В ПОДЗЕМЕЛЬЕ, ДЛАНЕВИЦ!')
        bot.pin_chat_message(chat_id, mess.message_id)
        bot.unpin_chat_message(chat_id, mess.message_id)
        
    print("reminder Потоков - " + str(threading.active_count()))

    start_routine()


bot.polling(none_stop=True, interval=0); 



