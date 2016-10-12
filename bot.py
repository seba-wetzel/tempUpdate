# -*- coding: utf-8 -*- 
import telebot # Importamos las librería
 
TOKEN = "289415643:AAEXB1wu6Q7SSk_j3RM4-osylaOJFCPuqi0" # Ponemos nuestro Token generado con el @BotFather
 
bott = telebot.TeleBot(TOKEN) # Combinamos la declaración del Token con la función de la API

@bott.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bott.reply_to(message, "Howdy, how are you doing?")

@bott.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bott.reply_to(message, "Howdy, how are you doing?")

@bott.message_handler(func=lambda message: True)
def echo_all(message):
        bott.reply_to(message, message.text)

bott.polling()
