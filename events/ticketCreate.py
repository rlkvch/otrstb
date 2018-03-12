import io
import json
import logging
import socket
import sys

import requests
import telebot
from pyotrs import Article, Client, Ticket

import config

# Debug ################################################################
# logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
#                     level=logging.DEBUG,
#                     filename=u'path_to_logs')
# def debug(*args):
#     logging.debug(args)
########################################################################

arg1 = sys.argv[1]
arg2 = sys.argv[2]

def get_ticket():
    client = Client(config.CLIENT_URL, config.USER, config.PASSWD)
    client.session_create()
    ticket = client.ticket_get_by_number(arg1)
    result = ticket.to_dct()
    json_string = json.dumps(result)
    parsed_string = json.loads(json_string)
    title = (parsed_string["Ticket"]["Title"])
    user_id = (parsed_string["Ticket"]["CustomerUserID"])
    queue = (parsed_string["Ticket"]["Queue"])
    date = (parsed_string["Ticket"]["Created"])
    phone = (parsed_string["Ticket"]["DynamicField"][0]["Value"])
    message = (title + '\n' + user_id + '\n' + queue + '\n' + date + '\n' + phone)
    return message

msg = (get_ticket())
bot = telebot.TeleBot(config.BOT_TOKEN)
bot.send_message(config.CHANNEL_ID, msg)
