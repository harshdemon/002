import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler

SHAYARI_STRINGS = (
  "Har Tanha Raat Mein Ek Naam Yaad Aata Hai Kabhi Subhah To Kabhi Shaam Yaad Aata Hai,Jab Sochte Hain Kar Lein Dobara Mohabbat,Fir Pehli Mohabbat Ka Anzaam Yaad Aata Hai.",
  "Humein Shayar Samajh Ke Yoon Najar Andaz Mat Kariye,Najar Hum Fer Le To Husn Ka Baazar Gir Jayega.",
  "Humari Haisiyat Ka Andaza Tum Ye Jaan Ke Laga Lo,Hum Kabhi Unke Nahi Hote Jo Har Kisi Ke Ho Gaye.",
  "Iss Se Zyada Tujhe Aur Kitna Qareeb Laaun Main,Ki Tujhe Dil Mein Rakh Kar Bhi Mera Dil Nahi Bharta.",
  "Ye Zindagi Hasin Hai Iss Se Pyar Karo,Abhi Hai Raat To Subah Ka Intezar Karo,Wo Pal Bhi Ayega Jiski Khwahish Hai Aapko,Rab Par Rakho Bharosa Waqt Par Aitbar Karo.",
)

@run_async
def shayari(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SHAYARI_STRINGS))
    else:
      message.reply_text(random.choice(SHAYARI_STRINGS))


SHAYARI_HANDLER = DisableAbleCommandHandler("shayari", shayari)

dispatcher.add_handler(SHAYARI_HANDLER)
