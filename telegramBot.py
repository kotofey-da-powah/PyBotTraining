#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep

from config import telegramToken
from vkFeedParser import get_post

update_id = None


def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot(telegramToken)

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename=u'mylog.log')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message.text:  # your bot can receive updates without messages
            # Reply to the message
            text = update.message.text
            if text == '/start':
                update.message.reply_text(
                    'Привет!\nНапиши мне /getrandompost чтобы получить случайный пост посвященный Python.')
            elif text == '/getrandompost':
                update.message.reply_text(get_post())
            else:
                update.message.reply_text(
                    'Напиши мне /getrandompost чтобы получить случайный пост посвященный Python.')



if __name__ == '__main__':
    main()
