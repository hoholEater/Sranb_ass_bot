
import telebot
import datetime
import random
from multiprocessing.context import Process
import schedule
import time
import logging
import openai
from googletrans import Translator
from langdetect import detect
import bot_configue
import sqlite3
import speech_recognition as sr
import os
import uuid


test = False
#test = True


chat_id = bot_configue.CHAT_ID

bot = telebot.TeleBot(bot_configue.BOT_TOKEN)

openai.api_key = bot_configue.GPT_TOKEN

# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users (
# id INTEGER PRIMARY KEY,
# username TEXT NOT NULL,
# email TEXT NOT NULL,
# age INTEGER
# )
# ''')


# connection.commit()
# connection.close()



challenge_mass      = {}
challenge_owner     = []
challenge_is_active = [False]
list_of_dlanevci    = []

translator = Translator()

logging.basicConfig(level=logging.INFO, filename="Sranb_log.log",filemode="a",format="%(asctime)s %(levelname)s %(message)s")


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

r = sr.Recognizer()

def recognise(filename):
    with sr.AudioFile(filename) as source:
        audio_text = r.listen(source)
        language='ru-RU'
        
        try:
            text = r.recognize_google(audio_text,language=language)
            print('Converting audio transcripts into text ...')
            print(text)
            return text
        except sr.RequestError as e:
            print("Ошибка сервиса; {0}".format(e))
            return "Ошибка сервиса. Что бы это ни значило."
        except sr.UnknownValueError:
            print('UnknownValueError.. run again...')
            return "Не разобрать твоё бормотание, проглоти - потом говори."
        except:
            print('Sorry.. run again...')
            return "Не удалось в этот раз... Проблема не во мне, проблема в тебе."

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    
    filename = str(uuid.uuid4())
    file_name_full="./voice/"+filename+".ogg"
    file_name_full_converted="./ready/"+filename+".wav"
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    with open(file_name_full, 'wb') as new_file:
        new_file.write(downloaded_file)
    
    os.system("ffmpeg -i "+file_name_full+"  "+file_name_full_converted)
    
    text = recognise(file_name_full_converted)
   
    bot.reply_to(message, text)
    os.remove(file_name_full)
    os.remove(file_name_full_converted)
    
@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        bot.send_message(message.chat.id,'Всё работает и без тебя.')
    except:
        print("Для вас конкурсов нет.")

        
@bot.message_handler(commands=['ave_sranb'])
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
        if str(message.chat.id) != chat_id:
           bot.send_message(message.chat.id, "Только в чате Драни Мола, сладкий.")
           return
        
        bot.send_message(message.chat.id, datetime.datetime.now())

    except:
        bot.send_message(message.chat.id,"Ошибка при формировании картинки.")
      
@bot.message_handler(commands=['img'])
def img_message(message):
    
    if str(message.chat.id) != chat_id:
        bot.send_message(message.chat.id, "Только в чате Драни Мола, сладкий.")
        return
    
    try:
        
        text = message.text.replace("/img ","")
        response = openai.Image.create(
          prompt = text,
          n=1,
          size="1024x1024"
        )
        image_url = response['data'][0]['url']

        bot.send_photo(message.chat.id,image_url)

    except:
        bot.send_message(message.chat.id,"Ошибка при формировании картинки.")

@bot.message_handler(commands=['tlk'])
def tlk_message(message):
    
    if str(message.chat.id) != chat_id:
        bot.send_message(message.chat.id, "Только в чате Драни Мола, сладкий.")
        return
    
    try:
        prompt = message.text.replace("/tlk ","")

        # completion = openai.ChatCompletion.create(model = 'gpt-3.5-turbo',
        # messages = [{'role': 'user', 'content': prompt}],temperature = 0.9)  
       
        response = openai.ChatCompletion.create( 
            model = "gpt-3.5-turbo", 
            messages = [ 
                {"role": "system", 'content': "Ты - остроумный, злой и жестокий человек который много матерится"},
                {"role": "assistant", "content": prompt}
            ],
            max_tokens = 1000,
            n = 1,
            temperature = 0.5,
        )
        
        bot.send_message(message.chat.id,response['choices'][0]['message']['content'])

     
    except:
        bot.send_message(message.chat.id,"Ошибка произношения.")
        
@bot.message_handler(commands=['sambo'])
def sambo_message(message):
    try:
        if message.reply_to_message != None:
            message.reply_to_message.from_user.username
        
            name2 = "@"+message.reply_to_message.from_user.username if \
                message.reply_to_message.from_user.username != None  else message.reply_to_message.from_user.full_name
        else:
            name2 = message.text.replace("/sambo ","")
            
        name1 = "@"+message.from_user.username if message.from_user.username != None  else message.from_user.full_name
        
        if name2 == "/sambo":
           bot.send_message(message.chat.id, "Найди себе партнёра в этой качалке.")
           return
        
        sambo(name1,name2)

    except:
        print("Для вас конкурсов нет.")

@bot.message_handler(commands=['trns'])
def translate_message(message):
    try:
       
       if message.reply_to_message != None and message.reply_to_message.content_type == "text":
           
           src = detect(message.reply_to_message.text)
           dest = "en" if src == "ru" else "ru"
           translated_text = translator.translate(message.reply_to_message.text, src='auto', dest=dest) 
           bot.send_message(message.chat.id,translated_text.text)  
    except: 
        bot.send_message(message.chat.id,"Трудности перевода. Дело не во мне - дело в тебе.")


@bot.message_handler(commands=['raffle'])
def ruffle_message(message):
    try:
        username = "@"+message.from_user.username if message.from_user.username != None  else message.from_user.full_name
        if message.text == '/raffle':
           bot.send_message(message.chat.id, "Конкурс без текста... Так нельзя, брат, нельзя =(", reply_to_message_id=message.id)
        else:
            if challenge_is_active[0]:
                bot.send_message(message.chat.id, "Сначала победи в существующем наличном конкурсе.", reply_to_message_id=message.id)
                return
            challenge_owner.clear()
            challenge_mass.clear()
            challenge_owner.insert(0,username)
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton("Участвую!", callback_data = 'add_me'))
            markup.add(telebot.types.InlineKeyboardButton("Выбрать победителя.", callback_data = 'roll'))
            challenge_is_active.clear()
            challenge_is_active.insert(0,True)
            bot.send_message(message.chat.id, "\U0001F4A5 Внимание... ДЛАНЕКОНКУРС от "+ username + "\n" + \
                             "\n" + \
                             "Уважаемые участники: \n", \
                              reply_to_message_id=message.id, parse_mode='html', reply_markup=markup)
    except:
            
        print("Для вас конкурсов нет.")

@bot.callback_query_handler(func=lambda call: True)
def challenge_func(call):
    if call.data == 'add_me':
        try:
            username = "@"+call.from_user.username if call.from_user.username != None else call.from_user.full_name

            if username in challenge_mass:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Ты куда лезешь второй раз, каззёл!?")
                return
            
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton("Участвую!", callback_data = 'add_me'))
            markup.add(telebot.types.InlineKeyboardButton("Выбрать победителя.", callback_data = 'roll')) 
            
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, \
                                  text = call.message.text+'\n \U0001F90E '+ username,reply_markup=markup)
           
            challenge_mass[username] = call.from_user.id
            
        except:
            logging.error("Ошибка при добавлении " + username, exc_info=True)
            print("Ошибка при добавлении")
        
    elif call.data == 'roll':
         
         try:
             username = "@"+call.from_user.username if call.from_user.username != None else call.from_user.full_name

             if len(challenge_owner) == 0: #Костыли, а чо мне.
                challenge_owner.insert(0,username)
                
             if username != challenge_owner[0]:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Не твой конкурс, родной. Или ты криворукий просто?")
                return  
         
             win_ner = random.choice(list(challenge_mass.items()))
            
             win_id = win_ner[1]
             winner = win_ner[0]
             result = bot.get_user_profile_photos(win_id).photos[0][0].file_id
             
             temp_mes = bot.send_message(call.message.chat.id,'Пошла жара, все по местам!', reply_to_message_id=call.message.id)
             
             bot.pin_chat_message(chat_id, temp_mes.message_id, False)
             time.sleep(3)
             bot.unpin_chat_message(chat_id, temp_mes.message_id)   
            
             bot.edit_message_text(chat_id=call.message.chat.id, message_id=temp_mes.message_id, text = 'Возможно победитель '+winner+"?")
             time.sleep(2.5)
             
             win_ner = random.choice(list(challenge_mass.items()))
             win_id = win_ner[1]
             winner = win_ner[0]
             
             bot.edit_message_text(chat_id=call.message.chat.id, message_id=temp_mes.message_id, text = 'или '+winner+"?")
             time.sleep(2.5)
             
             win_ner = random.choice(list(challenge_mass.items()))
             win_id = win_ner[1]
             winner = win_ner[0]
             
             photos = bot.get_user_profile_photos(win_id).photos
             
             if not photos:
                result = call.message.chat.photo                 
              
             result = photos[0][0].file_id
             
             bot.edit_message_text(chat_id=call.message.chat.id, message_id=temp_mes.message_id, text = 'А может ты '+str.lower(massiv_izuma[random.randint(0, len(massiv_izuma))]).strip()+"?")
             time.sleep(1)
             
             bot.delete_message(chat_id=call.message.chat.id, message_id=temp_mes.message_id)
             
             bot.send_photo(call.message.chat.id,result,'Выиграв у всех подебил '+winner+'! ')
             
             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = call.message.text+'\n\n\n Победил легендарный \U0001F496 '+winner + " \U0001F496")
             
             challenge_is_active.clear()
             challenge_is_active.insert(0,False)
             challenge_owner.clear()
             challenge_mass.clear()
         except:
             logging.error("Ошибка при запуске конкурса " + username, exc_info=True)
 
             bot.send_message(call.message.chat.id,'Конкурса не будет, возможно бот откис. Звоните программистам!11!1')
         
def challenge_winner(challenge_mass):
    if len(challenge_mass) > 0:
         return random.randint(0,len(challenge_mass)-1)


@bot.message_handler(content_types='text')
def get_text_messages(message):
    try:
        username = "@"+message.from_user.username if message.from_user.username != None  else message.from_user.full_name
        
        if username not in list_of_dlanevci:
            list_of_dlanevci.append(username)       
                  
        if "пидорн" in str.lower(message.text) or "пидоря" in str.lower(message.text) or "пидарн" in str.lower(message.text):
            bot.send_message(message.chat.id, "Пидорните этого казла - " + random.choice(list_of_dlanevci)+" \U0001F92C");
        
        elif "член" in str.lower(message.text):
           
            bot.send_message(message.chat.id, "Я по глазам вижу, что твой пчленб длиной " +str(round(random.uniform(1.0, 25.0),2))+\
                             " см. \U0001F90F, " +username);
        
        elif username == "@xxxizymxxx" and answer():
            bot.send_message(message.chat.id, "Изюм, " + str.lower(massiv_izuma[random.randint(0, len(massiv_izuma)-1)]).strip() + ", динахой.",reply_to_message_id=message.id);
    except:
        logging.error(message.text, exc_info=True)
        bot.send_message(message.chat.id,'С тобой какие-то проблемы, брат.',reply_to_message_id=message.id)
        
def answer():

    return random.randint(1, 100) > 50

        
def send_reminder(chat_id, reminder_name):
   
    if reminder_name == 'Пилить':
        bot.send_sticker(chat_id,"CAACAgIAAxkBAAEKbKJlGHZe57sEFXQAAQreK1yGIS11W9cAAi0AA8Lf0BWgxLT-UqQgODAE")
        mess = bot.send_message(chat_id, 'Время пилить лаха!\nГотовность - 1 минута.')
        bot.pin_chat_message(chat_id, mess.message_id, False)
        time.sleep(1)
        bot.unpin_chat_message(chat_id, mess.message_id)
    else:
        bot.send_sticker(chat_id,"CAACAgIAAxkBAAEKbKBlGHZJNGfUgpDQL5nbH8WWFSP44gACAQADwt_QFTJzIDG-COPZMAQ")
        mess = bot.send_message(chat_id, 'ПРЫГАЙ В ПОДЗЕМЕЛЬЕ, ДЛАНЕВИЦ!\nГотовность - 1 минута.')
        bot.pin_chat_message(chat_id, mess.message_id, False)
        time.sleep(1)
        bot.unpin_chat_message(chat_id, mess.message_id)

     

def sambo(name1, name2):
    
    bot.send_message(chat_id, 'Оу май... '+ name1 + ' решил посамбоваться с ' + name2)
    time.sleep(2)
    
    mess = bot.send_message(chat_id, text = 'Происходит мощная борьба.')
    time.sleep(2)
   
    bot.edit_message_text(chat_id=chat_id, message_id=mess.message_id, text = 'В самбовании победил ' + name1 if answer() else 'В самбовании победил ' + name2 + " (победила дружба вообще-то.)")
    bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEKdRZlHq_kbx3Adqp3yWv7B7LrXi4jlQACKBcAAgbygErCTNkBu8AvAzAE')
    

schedule.every().day.at("00:54").do(send_reminder,chat_id, "Пилить")
schedule.every().day.at("05:04").do(send_reminder,chat_id, "Пилить")
schedule.every().day.at("09:04").do(send_reminder,chat_id, "Пилить")
schedule.every().day.at("14:04").do(send_reminder,chat_id, "Пилить")
schedule.every().day.at("19:04").do(send_reminder,chat_id, "Пилить")

schedule.every().day.at("09:36").do(send_reminder,chat_id, "Прыгать")
schedule.every().day.at("14:36").do(send_reminder,chat_id, "Прыгать")
schedule.every().day.at("19:36").do(send_reminder,chat_id, "Прыгать")


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
        bot.infinity_polling(timeout=10, long_polling_timeout = 5)
    except:
        logging.error("Ошибка при рестарте шедулера.", exc_info=True)
        pass

