#!/usr/bin/env python
import os
import telebot
from telebot import types
flag = 0

#Request to the system to receive a variable token
TOKEN = os.environ['MY_BOT_TOKEN']
bot = telebot.TeleBot(TOKEN)

#Picture output function
def out_qr(in_t,in_q,mci):
	markup = types.ReplyKeyboardRemove()
	out_url = 'https://qrcode.tec-it.com/API/QRCode?data='+in_t+'&errorcorrection='+in_q+'&backcolor=%23ffffff&quietzone=5&size=Large'
	markup = types.ReplyKeyboardRemove()
	bot.send_photo(mci, out_url, reply_markup=markup, caption='Your QR-Code')

def out_barcode(in_t1,mci):
	markup = types.ReplyKeyboardRemove()
	out_url1 = 'https://barcode.tec-it.com/barcode.ashx?data='+in_t1+'&code=Code128&translate-esc=true&dpi=300&qunit=Mm&quiet=5'
	markup = types.ReplyKeyboardRemove()
	bot.send_photo(mci, out_url1, reply_markup=markup, caption='Your Code-128')

#Commands for calling /start and /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = types.ReplyKeyboardRemove()
	if message.text == '/start':
		out_start = "Hey. I am QR-Code Bot.\nI will help you create a QR-code or Code-128\n"
		bot.send_message(message.chat.id, out_start, reply_markup=markup)

	if message.text == '/help':
		out_start = "OK. I will help you.\n"
		out_start += "1) - Enter the text or URL - *Hello World!*\n"
		out_start += "2) - Select the type of code (*QR-Code* or *Code-128*)\n"
		out_start += "3) - Get your Code\n"
		out_start += " \n"
		out_start += "Powered by - *barcode.tec-it.com*\n"
		bot.send_message(message.chat.id, out_start, reply_markup=markup, parse_mode="Markdown")

#Commands to process the received data from the telegram
@bot.message_handler(content_types = ['text'])
def send_text(message):
	
	ms_quality = ('Medium', 'Quality', 'High')
	ms_qrorbar = ('QR-Code', 'Code-128')
	global in_text
	global in_quality
	global in_qrorbar
	global flag

	if flag == 0:
		in_text = message.text
		markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
		itembtn1 = types.KeyboardButton('QR-Code')
		itembtn2 = types.KeyboardButton('Code-128')
		markup.add(itembtn1,itembtn2,)
		bot.send_message(message.chat.id, "Select the type of code (*QR-Code* or *Code-128*)", reply_markup=markup, parse_mode="Markdown")
		flag = 1
	else:
		if message.text in ms_qrorbar:
			in_qrorbar = message.text
			if in_qrorbar == 'Code-128':
				out_barcode(in_text,message.chat.id)
				flag = 0
			if in_qrorbar == 'QR-Code':
				markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
				itembtn1 = types.KeyboardButton('Medium')
				itembtn2 = types.KeyboardButton('Quality')
				itembtn3 = types.KeyboardButton('High')
				markup.add(itembtn1,itembtn2,itembtn3)
				bot.send_message(message.chat.id, "Choose the degree of resistance of QR-Code to damages", reply_markup=markup)
		if message.text in ms_quality:
			in_quality = message.text
			in_quality = in_quality[0]	
			out_qr(in_text,in_quality,message.chat.id)
			flag = 0

bot.polling(timeout = 60)
