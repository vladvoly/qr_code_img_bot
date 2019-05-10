#!/usr/bin/env python
import os
import telebot
from telebot import types

#Request to the system to receive a variable token
TOKEN = os.environ['MY_BOT_TOKEN']
bot = telebot.TeleBot(TOKEN)

#Picture output function
def out_qr(in_t,in_c,in_q,mci):
	markup = types.ReplyKeyboardRemove()
	out_url = 'http://api.qrserver.com/v1/create-qr-code/?size=512x512&margin=5&data='+in_t+'&color='+in_c+'&ecc='+in_q
	markup = types.ReplyKeyboardRemove()
	bot.send_photo(mci, out_url, reply_markup=markup, caption='Your QR-Code')

#Commands for calling /start and /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = types.ReplyKeyboardRemove()
	if message.text == '/start':
		out_start = "Hey. I am Byte-Good-Bot.\nI will help you create a QR-code\n"
		bot.send_message(message.chat.id, out_start, reply_markup=markup)

	if message.text == '/help':
		out_start = "OK. I will help you.\n"
		out_start += "1) - Enter the text or URL - *Hello World! *\n"
		out_start += "2) - Choose the degree of resistance of QR-Code to damages - *Low/Medium/Quality/High*\n"
		out_start += "3) - Choose a QR-Code color - *Red/Green/Blue/Black/Other*\n"
		out_start += "4) - Get your QR-Code\n"
		bot.send_message(message.chat.id, out_start, reply_markup=markup, parse_mode="Markdown")

#Commands to process the received data from the telegram
@bot.message_handler(content_types = ['text'])
def send_text(message):
	
	ms_quality = ('Low', 'Medium', 'Quality', 'High')
	ms_color = ('Red', 'Green', 'Blue', 'Black')
	global in_text
	global in_quality
	global in_color 

	#2 - got the value of stability QR-code to damage
	if message.text in ms_quality:
		in_quality = message.text
		in_quality = in_quality[0]	
		markup = types.ReplyKeyboardMarkup(row_width=5, resize_keyboard=True)
		itembtn1 = types.KeyboardButton('Red')
		itembtn2 = types.KeyboardButton('Green')
		itembtn3 = types.KeyboardButton('Blue')
		itembtn4 = types.KeyboardButton('Black')
		itembtn5 = types.KeyboardButton('Other')
		markup.add(itembtn1, itembtn2, itembtn3,itembtn4,itembtn5)
		bot.send_message(message.chat.id, "Enter color QR-Code", reply_markup=markup)
	
	#3 - got the color value of QR-Code
	elif message.text in ms_color:
	 	in_color = message.text
	 	if in_color == 'Red':
	 		in_color = 'FF0000'
	 	elif in_color == 'Green':
	 		in_color = '00FF00'
	 	elif in_color == 'Blue':
	 		in_color = '0000FF'
	 	elif in_color == 'Black':
	 		in_color = '000000'
	 	out_qr(in_text,in_color,in_quality,message.chat.id)

	#4 - custom color request
	elif message.text == 'Other':
		markup = types.ReplyKeyboardRemove()
		bot.send_message(message.chat.id, "Enter your color in HTML HEX format", reply_markup=markup)

	#5 - output QR Code with custom color
	elif message.text[0] == '#':
		in_color = message.text[1:]
		out_qr(in_text,in_color,in_quality,message.chat.id)

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