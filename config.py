from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "e876f42ba75b74de9edad8cd1247763a")
      API_ID = int(getenv("API_ID", "28992411"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7456885062:AAHH_Z6H8-5v8K2vqfS_EFnn5sx2udTE_Jg")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001722984461:-1002373408251").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
