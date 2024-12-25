# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "10685201"))
    API_HASH = getenv("API_HASH", "8e039b83a886a2c2b97309ccc6298c20")
    BOT_TOKEN = getenv("BOT_TOKEN", "6564513574:7778283881:AAGXnKgTJOnDQlVM_fsDQuJ6OnJZsR9ki3o")
    FSUB = getenv("FSUB", "TelexOriginals")
    CHID = int(getenv("CHID", "-982105601"))
    SUDO = list(map(int, getenv("SUDO", "6168162777").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://mongodb+srv://arunready160:arun8899@cluster0.38pp4.mongodb.net/")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
