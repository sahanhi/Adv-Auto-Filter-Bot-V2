#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("APP_ID"))

API_HASH = os.environ.get("API_HASH")

BOT_TOKEN = os.environ.get("BOT_TOKEN")

DB_URI = os.environ.get("DB_URI")

USER_SESSION = os.environ.get("USER_SESSION")

VERIFY = {}

IMDB_TEMPLATE = "Here what i found for your query : {query} \n\n🎬 𝙏𝙞𝙩𝙡𝙚 \t: <i><b>{title}</b></i> 🔘 <b>{kind}</b>\n ⭐️ 𝙍𝙖𝙩𝙞𝙣𝙜 \t: <b>{rating}/10</b> (<i>From {votes} user ratings.)</i>\n 📆 𝙍𝙚𝙡𝙚𝙖𝙨𝙚 𝙞𝙣𝙛𝙤 \t: <b>{release_date}</b>\n 🎃 𝙂𝙚𝙣𝙧𝙚𝙨 \t: <b>{genres}</b>\n 🎙️ 𝙇𝙖𝙣𝙜𝙪𝙖𝙜𝙚(𝙨) \t: <b>{languages}</b>\n 🗂 𝙎𝙚𝙖𝙨𝙤𝙣𝙨 \t: <b>{seasons}</b>\n 🎛️ 𝙍𝙪𝙣 𝙩𝙞𝙢𝙚 \t: <b>{runtime} Mins</b>\n 🤵 𝘿𝙞𝙧𝙚𝙘𝙩𝙤𝙧(𝙨) \t: <b>{director}</b>\n 📝 𝙒𝙧𝙞𝙩𝙚𝙧(𝙨) \t: <b>{writer}</b>"


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
