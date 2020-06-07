import os
import telegram
import telebot
from telebot import types
import emoji
from blockchain import blockexplorer
from flask import Flask, request

from coinbase.wallet.client import Client


# Configuration variable
TOKEN = os.getenv("bot_token")

ADMIN_ID = os.getenv("bot_admin")

# Coinbase API for payments
API_KEY = os.getenv("cb api")
API_SECRET = os.getenv("cb secret")

bot = telebot.TeleBot(TOKEN, threaded=True)

import importdir
importdir.do("handlers", globals())
