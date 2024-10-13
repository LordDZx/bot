import time
from selenium import webdriver
from telebot import TeleBot
from telebot.types import Message

# إعداد متصفح الويب
driver = webdriver.Chrome()

# إعداد البوت
bot = TeleBot('7605903896:AAHrNiIghrli36jri2OWxrTZk_GTlxhOgDM')
chat_id = '-4532788813'

# أمر لأخذ لقطة شاشة وإرسالها
@bot.message_handler(commands=['screenshot'])
def send_screenshot(message: Message):
    driver.get('https://lorddzx.github.io/Bots/baduo/ranks1.html')  # استبدل بالرابط الذي تريد زيارته
    screenshot = driver.save_screenshot('screenshot.png')
    
    # إرسال الصورة إلى مجموعة تيليجرام
    with open('screenshot.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

# تشغيل البوت
bot.polling()

# دالة لجدولة لقطة الشاشة كل ساعة
def take_screenshot_and_send():
    driver.get('https://lorddzx.github.io/Bots/baduo/ranks1.html')  # استبدل بالرابط الذي تريد زيارته
    screenshot = driver.save_screenshot('screenshot.png')
    
    # إرسال الصورة إلى مجموعة تيليجرام
    with open('screenshot.png', 'rb') as photo:
        bot.send_photo(chat_id, photo)

while True:
    take_screenshot_and_send()
    time.sleep(3600)  # الانتظار لمدة ساعة
