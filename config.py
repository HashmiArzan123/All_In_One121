#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6940389122:AAHeyfLYS_97D5ktEiAJna9kmQ9aNWGveQk")
    API_ID = int(os.environ.get("API_ID", " 4942197"))
    API_HASH = os.environ.get("API_HASH", "13248a2c551b73193969b42194023635")
    AUTH_USERS = "5892781710"

