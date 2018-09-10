import io
import json
import logging
import socket
import sys

import requests
import telebot
from pyotrs import Article, Client, Ticket

import config

# logfile ################################################################
#  logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
#                      level=logging.DEBUG,
#                      filename=u'')
#  def debug(*args):
#      logging.debug(args)
##########################################################################

arg1 = sys.argv[1]
arg2 = sys.argv[2]

def get_ticket(argument):
    client = Client(config.CLIENT_URL, config.USER, config.PASSWD)
    client.session_create()
    ticket = client.ticket_get_by_number(argument,articles=True)
    result = ticket.to_dct()
    json_string = json.dumps(result)
    parsed_string = json.loads(json_string)
    title = (parsed_string["Ticket"]["Title"])
    user = (parsed_string["Ticket"]["Article"][0]["From"])
    queue = (parsed_string["Ticket"]["Queue"])
    msg_body = (parsed_string["Ticket"]["Article"][0]["Body"])
    date = (parsed_string["Ticket"]["Created"])
    message = ('Очередь: ' + queue + '\n' + 'От кого: ' + user + '\n' + 'Тема: ' + title + '\n' + msg_body + '\n' + date)
    return message

msg = (get_ticket(arg1))
bot = telebot.TeleBot(config.BOT_TOKEN)
bot.send_message(config.CHANNEL_ID, msg)

