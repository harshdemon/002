#khud banaya hai kang karna hai toh credit de dena
import html
import random
import time

from typing import Optional
from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from tswift import Song
from telegram.error import BadRequest

import SaitamaRobot.modules.shayari_strings as shayari_strings
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.alternate import send_message, typing_action
from SaitamaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from SaitamaRobot.modules.helper_funcs.extraction import extract_user

@run_async
def shayari(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(shayari_strings.SHAYARI))



SHAYARI_HANDLER = DisableAbleCommandHandler("shayari", shayari)

dispatcher.add_handler(SHAYARI_HANDLER)
