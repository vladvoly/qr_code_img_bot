#!/usr/bin/env python
import os
import telebot
from telebot import types

#Request to the system to receive a variable token
TOKEN = os.environ['MY_BOT_TOKEN']
bot = telebot.TeleBot(TOKEN)

#Picture output function
def out_qr(in_t,in_q,mci):
	markup = types.ReplyKeyboardRemove()
	out_url = 'https://qrcode.tec-it.com/API/QRCode?data='+in_t+'&errorcorrection='+in_q+'&backcolor=%23ffffff&quietzone=5&size=Large'
	markup = types.ReplyKeyboardRemove()
	bot.send_photo(mci, out_url, reply_markup=markup, caption='Your QR-Code')

#Commands for calling /start and /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = types.ReplyKeyboardRemove()
	if message.text == '/start':
		out_start = "Hey. I am QR-Code Bot.\nI will help you create a QR-code\n"
		bot.send_message(message.chat.id, out_start, reply_markup=markup)

	if message.text == '/help':
		out_start = "OK. I will help you.\n"
		out_start += "1) - Enter the text or URL - *Hello World! *\n"
		out_start += "2) - Choose the degree of resistance of QR-Code to damages - *Low/Medium/High*\n"
		out_start += "3) - Get your QR-Code\n"
		bot.send_message(message.chat.id, out_start, reply_markup=markup, parse_mode="Markdown")

#Commands to process the received data from the telegram
@bot.message_handler(content_types = ['text'])
def send_text(message):
	
	ms_quality = ('Low', 'Medium', 'Quality', 'High')
	global in_text
	global in_quality

	#2 - got the value of stability QR-code to damage
	if message.text in ms_quality:
		in_quality = message.text
		in_quality = in_quality[0]	
		out_qr(in_text,in_quality,message.chat.id)

	#1 - came plain text...
	else :
		in_text = message.text
		markup = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
		itembtn1 = types.KeyboardButton('Low')
		itembtn2 = types.KeyboardButton('Medium')
		itembtn3 = types.KeyboardButton('Quality')
		itembtn4 = types.KeyboardButton('High')
		markup.add(itembtn1, itembtn2, itembtn3,itembtn4)
		bot.send_message(message.chat.id, "Choose the degree of resistance of QR-Code to damages", reply_markup=markup)

bot.polling(timeout = 60)
