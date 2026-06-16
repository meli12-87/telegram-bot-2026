import telebot
import base
import api_movie

bot = telebot.TeleBot(base.TOKEN)
print('bot created...')


@bot.message_handler(commands= ['start'])
def say_hello(message):
    bot.send_message(message.chat.id, text = 'به بات Melimedia خوش آمدید')

@bot.message_handler(commands=['help', 'contact'])
def support(message):
    bot.reply_to(message,'در صورت نیاز به پشتیبانی با آیدی @Melflh در تماس باشید')

@bot.message_handler(commands=['news'])
def show_news(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn1 = telebot.types.InlineKeyboardButton(text = 'اخبار فیلم ها', url= 'https://collider.com/')


    btn2 = telebot.types.InlineKeyboardButton(text = 'سایت IMDB', url = 'https://www.imdb.com/')

    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text='یکی از گزینه زیر را انتخاب کنید', reply_markup=markup)

@bot.message_handler(commands=['menu'])
def show_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    btn1 = telebot.types.KeyboardButton(text='تماس با ما')
    btn2 = telebot.types.KeyboardButton(text='درباره ما')
    btn3 = telebot.types.KeyboardButton(text='بازگشت')
    markup.add(btn1, btn2 , btn3)
    bot.send_message(message.chat.id, text='یکی از گزینه زیر را انتخاب کنید', reply_markup=markup)


@bot.message_handler(commands =['movie'])
def get_movie_step_one(message):
    msg = bot.send_message(message.chat.id, text='نام فیلم مورد نظر را وارد کنید:')
    bot.register_next_step_handler(msg, get_movie_info)

def get_movie_info(message):
    movie_name= message.text
    result = api_movie.get_movie_info_by_name(movie_name)
    title= result[0]
    year = result[1]
    country=result[2]
    imdb_rate = result[3]

    info = f'title: {title}\nyear: {year}\ncountry: {country}\nimdb_rate: {imdb_rate}'
    bot.send_message(message.chat.id, text=info)

@bot.message_handler(func= lambda message: True)
def answer_to_other_msg(message):
    if message.text == 'تماس با ما':

        mobile = '09352663758'
        email = 'falahianmelina0@gmail.com'
        info = f'mobile:{mobile}\nemail: {email}'
        bot.send_message(message.chat.id, text = info)

    elif message.text == 'درباره ما':
        bot.send_message(message.chat.id, 'این بات مربوط به فیلم و سریال میباشد')
    elif message.text == 'بازگشت':
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text = "بازگشت به منوی اصلی", reply_markup=markup)




if __name__ == '__main__':
    bot.infinity_polling()

