# qr_code_img_bot
[1]: https://t.me/qr_code_img_bot
Telegram bot. [Link][1]  
Bot can create a QR-code of your text or links(URL).  
Bot created for the beautiful implementation of the public API. This is my first bot implemented in Python.

### QR-code generation  
Bot uses third-party API to create QR-code. [API QR-code](http://goqr.me/api/doc/create-qr-code/)

### Bot work  
Clicking on your [link][1] will meet the welcome record.  
![welcome record](https://i.imgur.com/SAarZFK.png)  

---
A command ```/start``` will make the bot listen to you.  
In response, the bot will send you these words  
>Hey. I am QR-Code Bot.  
>I will help you create a QR-code

The ```/help``` command will show how to create a QR-code.  
In response, the bot will send you these words  
>OK. I will help you.  
>1) - Enter the text or URL - **Hello World!**   
>2) - Choose the degree of resistance of QR-Code to damages - **Low/Medium/Quality/High**  
>3) - Choose a QR-Code color - **Red/Green/Blue/Black/Other**  
>4) - Get your QR-Code  
---
Send the bot some text. Let it be **Hello World!**  

![bot text](https://i.imgur.com/H7gjZ76.png)  

Parameter determines the degree of data redundancy. The more data redundancy exists, the more data can be restored if a QR-code is damaged (i.e. scratches on a QR-code sticker or something like that).  
* Low (~7% destroyed data may be corrected)  
* Middle (~15% destroyed data may be corrected)  
* Quality (~25% destroyed data may be corrected)  
* High (~30% destroyed data may be corrected)  
---
**Quality** has been selected  

![bot parameter](https://i.imgur.com/hetdGpf.png)  

Bot wants us to choose the color of the future QR-code.  
You can choose 4 preset colors or enter your own in HTML HEX format.  

![bot img](https://i.imgur.com/KzmQGee.png)   

---

Well done. QR-code is made. Now you can send it to a friend for scanning or save it to your device.  

---

You can support me.
* Bitcoin - ```15SK9zNqoDJfpdtrqiLBm1uESx52gLoqhs```  
* LiqPay - [donation](https://www.liqpay.ua/en/checkout/card/donationvlad)  

### If you have an ideas how to expand the functions of this bot or make it better, write to me.