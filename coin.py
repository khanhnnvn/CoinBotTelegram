#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import commands
import json
import re
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
def send_msg(update, msg):
    update.message.reply_text(msg)

def help(bot, update):
    update.message.reply_text('Em là bót :D')

def get_id(bot, update):
    test = '{} {}'.format(update.message.chat_id, update.message.message_id)
    update.message.reply_text(test)
#-------------------------------------------------------------------------------
def get_btc(bot, update):
    #test = '{} {}'.format(update.message.chat_id, update.message.message_id)
    coins = requests.get("https://api.coinmarketcap.com/v1/ticker/").json()
    for i in coins:
        if i["id"] in ["bitcoin"]:
            sms1 = "---------\n"+ i['symbol'] + ': '+'$ '+ i['price_usd']+" ("+i['percent_change_24h']+"%)"
            update.message.reply_text(sms1)
#-------------------------------------------------------------------------------
def getprice(fuck):
    coins = requests.get("https://api.coinmarketcap.com/v1/ticker/?limit=100000000000").json()
#    hexprice = requests.get("https://hextracoin.com/rate.php").json()
#    khanh = float(hexprice['price'])
    try:
        for dongxu in coins:
            if dongxu["symbol"] == fuck:
                abc = "" + dongxu['symbol'] + ': '+'$ '+ dongxu['price_usd']+" ("+dongxu['percent_change_24h']+"%)"
        return abc
    except:
        return "Not found"
"""        if fuck == "HXT":
            abc = "HXT: " + hexprice['price'] + ' ' +hexprice['currency']
        else:
            return "Not found"
        return abc
"""        
#--------------

def tho(bot, update):
    a = update.message.text
    words = a.replace('/','').upper()
    #words = a[a.find('/')+1:].upper()
    print words
    tho = getprice(words)
    print tho
    update.message.reply_text(tho)

def error(bot, update, error):
    print error
#ham get price    
#khong biet gi
def unknown(bot, update):
     bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

#----------------------------------------------------------------------------------------------------------------------
def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("492386487:AAElto1SH-HtjcfcoVW64vxi6-RGZGwNJp4")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("id", get_id))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler("", tho))

    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()


    updater.idle()

if __name__ == '__main__':
    main()
