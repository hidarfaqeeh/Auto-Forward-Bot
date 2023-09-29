from os import getenv

class Config(object):
      API_HASH = getenv("c1259b40b2ba148a795f8db4a830cbf5")
      API_ID = int(getenv("24343527", 0))
      AS_COPY = True if getenv("True", False) == "True" else False
      BOT_TOKEN = getenv("1543026455:AAEMi_2iq71gnKn9jX-j_MGhTvoQOxLMe5c", "")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "").replace("\n", " ").split(' '))
