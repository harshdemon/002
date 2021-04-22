import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
   "Saans bhi loon to uski mehak aati hai…. usne thukraya hai mujhe itne qareeb aane k baad..",
   "Hum toh bane hii tabah hone k liye the,, tumhara milna toh bas ek bahana tha…!!",
   "Jo Ho Ijazat To Tum Se ek Baat Punchhu…… Jo Hum Se Ishq Seekha Tha Woh Ab Tum Kis Se Karte Ho….!!!!",
   "Bandh mutthi me Ret ki Tarah, Bhoola diya tumne zara zara karke..!!",
   "mere halaat par muskurate ho, Baddua hAI tujHe ishq ho jaAye.",
   "Teri Mohabbat Bhi Kiraye Ke Ghar Ki Tarah Thi, Kitna Bhi Sajaya, Par Mere Na Hue.",
   "Tu agar khawab tha mera to bata kyu meri neend se bahaar nikla",
   "fāsla nazroñ kā dhoka bhī to ho saktā hai vo mile yā na mile haath baḌhā kar dekho",
  )

@run_async
def shayari(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))


SHAYARI_HANDLER = DisableAbleCommandHandler("shayari", dhokha)

dispatcher.add_handler(SHAYARI_HANDLER)
