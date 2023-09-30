import telebot
import datetime
import random
from multiprocessing.context import Process
import schedule
import time


chat_id = '-'

bot = telebot.TeleBot(':')

test = False
#test = True

challenge_mass = []
challenge_owner = []
challenge_is_active = [False]


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
    try:
        bot.send_message(message.chat.id,'Всё работает и без тебя.')
    except:
        print("Для вас конкурсов нет.")

        
@bot.message_handler(commands=['avesranb'])
def avesranb_message(message):
    try:
        bot.send_message(message.chat.id,'AVE SRANb!111!11')
    except:
        print("Для вас конкурсов нет.")
        
@bot.message_handler(commands=['help'])
def avesranb_message(message):
    try:
        bot.send_message(message.chat.id,'Тебе и врач не поможет. Dinahoi.')
    except:
            
        print("Для вас конкурсов нет.")
        
@bot.message_handler(commands=['test'])
def test_message(message):
    try:
        bot.send_message(message.chat.id, datetime.datetime.now())
    except:
            
        print("Для вас конкурсов нет.")
        
@bot.message_handler(commands=['raffle'])
def ruffle_message(message):
    try:
        if message.text == '/raffle':
           bot.send_message(message.chat.id, "Конкурс без текста... Так нельзя, брат, нельзя =(", reply_to_message_id=message.id)
        else:
            if challenge_is_active[0]:
                bot.send_message(message.chat.id, "Сначала победи в существующем наличном конкурсе.", reply_to_message_id=message.id)
                return
            challenge_owner.clear()
            challenge_mass.clear()
            challenge_owner.insert(0,"@"+ message.from_user.username)
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton("Участвую!", callback_data = 'add_me'))
            markup.add(telebot.types.InlineKeyboardButton("Выбрать победителя.", callback_data = 'roll'))
            challenge_is_active.clear()
            challenge_is_active.insert(0,True)
            bot.send_message(message.chat.id, "\U0001F4A5 Внимание... ДЛАНЕКОНКУРС от @"+ message.from_user.username + "\n" + \
                             "\n" + \
                             "Уважаемые участники: \n", \
                              reply_to_message_id=message.id, parse_mode='html', reply_markup=markup)
    except:
            
        print("Для вас конкурсов нет.")

@bot.callback_query_handler(func=lambda call: True)
def challenge_func(call):
    if call.data == 'add_me':
        try:
            if '@' + call.from_user.username in challenge_mass:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Ты куда лезешь второй раз, каззёл!?")
                return
            
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton("Участвую!", callback_data = 'add_me'))
            markup.add(telebot.types.InlineKeyboardButton("Выбрать победителя.", callback_data = 'roll')) 
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, \
                                  text = call.message.text+'\n \U0001F90E @'+ call.from_user.username,reply_markup=markup)
         
            challenge_mass.insert(0,"@"+ call.from_user.username)
        except:
            
            print("Ошибка при добавлении")
        
    elif call.data == 'roll':
         try:
             if len(challenge_owner) == 0: #Костыли, а чо мне.
                challenge_owner.insert(0,"@"+ call.from_user.username)
                
             if '@'+ call.from_user.username != challenge_owner[0]:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Не твой конкурс, родной. Или ты криворукий просто?")
                return  
         
             winner = challenge_winner(challenge_mass)
             bot.send_message(call.message.chat.id,'Подебил ' + winner, reply_to_message_id=call.message.id)
             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = call.message.text+'\n\n\n Победил легендарный \U0001F496 '+winner + "\U0001F496")
             challenge_is_active.clear()
             challenge_is_active.insert(0,False)
             challenge_owner.clear()
             challenge_mass.clear()
         except:
             
             bot.send_message(call.message.chat.id,'Конкурса не будет, возможно бот откис. Звоните программистам!11!1')
         
def challenge_winner(challenge_mass):
    if len(challenge_mass) > 0:
         return challenge_mass[random.randint(0,len(challenge_mass)-1)]


@bot.message_handler(content_types='text')
def get_text_messages(message):
    try:
        if "пидорните" in str.lower(message.text):
            bot.send_message(message.chat.id, "Ну пидорните");
        elif "член" in str.lower(message.text):
            bot.send_message(message.chat.id, "Я по глазам вижу, что твой пчленб длиной " +str(random.randint(1, 125))+ " см. \U0001F90F, @" +message.from_user.username);
        elif ("попобав" in str.lower(message.text)) and answer():
            bot.send_message(message.chat.id, "Попобава лох и казёл, это все знают, @" +message.from_user.username);
        elif message.from_user.username == "xxxizymxxx":
            bot.send_message(message.chat.id, "Изюм, " + str.lower(massiv_izuma[random.randint(0, len(massiv_izuma))]).strip() + ", динахой.");
    except:
        bot.send_message(call.message.chat.id,'С тобой какие-то проблемы, брат.')
        
def answer():

    return random.randint(1, 100) > 50

        
def send_reminder(chat_id, reminder_name):
   
    if reminder_name == 'Пилить':
        mess = bot.send_message(chat_id, 'Время пилить лаха!\n Готовность - 1 минута.')
        bot.pin_chat_message(chat_id, mess.message_id)
        time.sleep(0.5)
        bot.unpin_chat_message(chat_id, mess.message_id)
    else:
        mess = bot.send_message(chat_id, 'ПРЫГАЙ В ПОДЗЕМЕЛЬЕ, ДЛАНЕВИЦ!\n Готовность - 1 минута.')
        bot.pin_chat_message(chat_id, mess.message_id)
        time.sleep(0.5)
        bot.unpin_chat_message(chat_id, mess.message_id)

     
schedule.every().day.at("00:54").do(send_reminder,chat_id, "Пилить")
schedule.every().day.at("05:04").do(send_reminder,chat_id, "Пилить")
schedule.every().day.at("09:04").do(send_reminder,chat_id, "Пилить")
schedule.every().day.at("14:04").do(send_reminder,chat_id, "Пилить")
schedule.every().day.at("19:04").do(send_reminder,chat_id, "Пилить")

schedule.every().day.at("09:36").do(send_reminder,chat_id, "")
schedule.every().day.at("14:36").do(send_reminder,chat_id, "")
schedule.every().day.at("19:36").do(send_reminder,chat_id, "")


class ScheduleMessage():
    def try_send_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)
 
    def start_process():
        p1 = Process(target=ScheduleMessage.try_send_schedule, name = "bot_shed", args=())
        p1.start()
 
 
if __name__ == '__main__':
    ScheduleMessage.start_process()
    try:
        bot.polling(none_stop=True)
    except:
        pass

