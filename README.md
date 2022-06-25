# qr_code_img_bot
[1]: https://t.me/qr_code_img_bot
Telegram bot. [Link][1]  
Bot can create a QR-code or Code-128 of your text or links(URL).  
Bot created for the beautiful implementation of the public API. This is my first bot implemented in Python.

### QR-code generation  
Bot uses third-party API to create QR-code. [API QR-code](https://barcode.tec-it.com/en/)

### Bot work  
Clicking on your [link][1] will meet the welcome record.  
![welcome record](https://i.imgur.com/SAarZFK.png)  

---
A command ```/start``` will make the bot listen to you.  
In response, the bot will send you these words  
>Hey. I am QR-Code Bot.  
>I will help you create a QR-code or Code-128

The ```/help``` command will show how to create a QR-code.  
In response, the bot will send you these words  
>OK. I will help you.  
>1) - Enter the text or URL - **Hello World!** 
>2) - Select the type of code (**QR-Code** or **Code-128**)  
>3) - Get your Code  
>
>Powered by - barcode.tec-it.com
---
Send the bot some text. Let it be **Hello World!**  

![bot text](https://i.imgur.com/w17Jbeg.jpg)  

The bot offers to choose the type of code. QR-Code or Code-128

---
**Code-128** has been selected  

![bot parameter](https://i.imgur.com/rJ9DkN6.jpg)  

This completes the creation of Code-128. The bot sent us an image of our code and we can scan it.  

---
Now let's create a QR Code. You need to enter any text or link again and then press the QR-Code button.

![bot img](https://i.imgur.com/0p7Uanr.jpg)   

The bot asks us to choose the degree of durability of the QR-Code.
Parameter determines the degree of data redundancy. The more data redundancy exists, the more data can be restored if a QR-code is damaged (i.e. scratches on a QR-code sticker or something like that).  
* Middle (~15% destroyed data may be corrected)  
* Quality (~25% destroyed data may be corrected)  
* High (~30% destroyed data may be corrected)  
---

Well done. QR-code is made. Now you can send it to a friend for scanning or save it to your device.  

![bot img](https://i.imgur.com/SilSx9H.jpg)

---

### If you have an ideas how to expand the functions of this bot or make it better, write to me.
