#!/usr/bin/env python
import os
import telebot
from telebot import types

#Request to the system to receive a variable token
TOKEN = os.environ['MY_BOT_TOKEN']
bot = telebot.TeleBot(TOKEN)




#Picture output function
def out_qr(in_t,in_q):
	markup = types.ReplyKeyboardRemove()
	out_url = 'https://qrcode.tec-it.com/API/QRCode?data='+in_t+'&errorcorrection='+in_q+'&backcolor=%23ffffff&quietzone=5&size=Large'
	markup = types.ReplyKeyboardRemove()
	bot.send_photo(message.chat.id, out_url, reply_markup=markup, caption='Your QR-Code')
	flag = 0

def out_bar(in_t):
	markup = types.ReplyKeyboardRemove()
	out_barcode = 'https://barcode.tec-it.com/barcode.ashx?data='+in_t+'&code=Code128&translate-esc=on'
	markup = types.ReplyKeyboardRemove()
	bot.send_photo(message.chat.id, out_barcode, reply_markup=markup, caption='Your Code-128')
	flag = 0
	
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
		out_start += "2) - Get your Code\n"
		bot.send_message(message.chat.id, out_start, reply_markup=markup, parse_mode="Markdown")

#Commands to process the received data from the telegram
@bot.message_handler(content_types = ['text'])
def send_text(message):
	
	ms_quality = ('Low', 'Medium', 'Quality', 'High')
	ms_c_format = ('QR-Code', 'Code-128')
	global in_text
	global in_quality
	global in_c_format
	global flag = 0

	if flag == 0:
		in_text = message.text
		markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
		itembtn1 = types.KeyboardButton('QR-Code')
		itembtn2 = types.KeyboardButton('Code-128')
		markup.add(itembtn1, itembtn2)
		bot.send_message(message.chat.id, "Select the type of code (*QR-Code* or *Code-128*).", reply_markup=markup,  parse_mode="Markdown")
		flag = 1
	
	else:
		if message.text in ms_c_format:
			in_c_format = message.text
			if in_c_format == 'Code-128':
				out_bar(in_text)
			if in_c_format == 'QR-Code':
				markup = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
				itembtn1 = types.KeyboardButton('Low')
				itembtn2 = types.KeyboardButton('Medium')
				itembtn3 = types.KeyboardButton('Quality')
				itembtn4 = types.KeyboardButton('High')
				markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
				bot.send_message(message.chat.id, "Choose the degree of resistance of QR-Code to damages", reply_markup=markup)
		if message.text in ms_quality:
			in_quality = message.text
			in_quality = in_quality[0]	
			out_qr(in_text,in_quality)

bot.polling(timeout = 60)
