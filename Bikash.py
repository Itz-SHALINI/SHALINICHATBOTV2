from pyrogram import Client, filters, idle
from pyrogram.types import *
from pymongo import MongoClient
from pyrogram import enums
import requests
import random
import os
import re


API_ID = os.environ.get("API_ID", "none") 
API_HASH = os.environ.get("API_HASH", "none") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "none") 
MONGO_URL = os.environ.get("MONGO_URL", "none")
BOT_IMAGE = os.environ.get("BOT_IMAGE", "none")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "none")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "none")
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "none")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "none")
LOG_GROUP_ID = "-1002041372224"

bot = Client(
    "V_Chat_Bot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


STBUTTON = [
  [
       InlineKeyboardButton(
    text="Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
    url=f"https://t.me/Shalini_chat_Bot?startgroup=true",
        ),
  ],
  [
    InlineKeyboardButton(
      text="Uᴘᴅᴀᴛᴇs",
      url=f"https://t.me/ShaliniMusicBotSh",
    ),
    InlineKeyboardButton(
      text="Sᴜᴘᴘᴏʀᴛ",
      url=f"https://t.me/music_world_sh",
    ),
  ],
  [
    InlineKeyboardButton(
      text="Dᴇᴠᴇʟᴏᴘᴇʀ",
      url=f"tg://openmessage?user_id=6910477574",
    ),
  ],
]


pht_list = ["neko"]
pht = random.choice(pht_list)
url = f"https://api.waifu.pics/sfw/{pht}"


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.get_chat_members(
            chat_id, filter="administrators"
        )
    ]

            
@bot.on_message(filters.command("start") & filters.private)
async def start_(client: Client, message: Message):
    response = requests.get(url).json()
    try:
        up = response['url']
        sender_id = message.from_user.id
        sender_name = message.from_user.first_name
        await message.reply_photo(up,
            caption=f"""**━━━━━━━━━━━━━━━━━━❥\n\n✯ Hᴇʟʟᴏ {message.from_user.mention} \n✯I'ᴍ A Aɪ Bᴀsᴇᴅ Cʜᴀᴛ Bᴏᴛ ✨\n✯ Mʏ Nᴀᴍᴇ Is Ꮥʜꫝʟɪɴɪ cɦαƭ ɓσƭ\n✯ ᴛᴏ ᴇɴᴀʙʟᴇ ᴄʜᴀᴛ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴛʏᴘᴇ \n✯ /chatbot on|off \n✯ Jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴJᴏʏ sᴜᴘᴇʀ Hɪɢʜ ǫᴜᴀʟɪᴛʏ ᴄʜᴀᴛ\n\n━━━━━━━━━━━━━━━━━━❥**""",
            reply_markup=InlineKeyboardMarkup(STBUTTON)
        )
        await bot.send_message(
                LOG_GROUP_ID,
                f"{message.from_user.mention} has just started Bot.\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
        )
    except:
        up = response['url']
        sender_id = message.from_user.id
        sender_name = message.from_user.first_name
        await message.reply_photo(up,
            caption=f"""**━━━━━━━━━━━━━━━━━━❥\n\n✯ Hᴇʟʟᴏ {message.from_user.mention} \n✯I'ᴍ A Aɪ Bᴀsᴇᴅ Cʜᴀᴛ Bᴏᴛ ✨\n✯ Mʏ Nᴀᴍᴇ Is Ꮥʜꫝʟɪɴɪ cɦαƭ ɓσƭ\n✯ ᴛᴏ ᴇɴᴀʙʟᴇ ᴄʜᴀᴛ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴛʏᴘᴇ \n✯ /chatbot on|off \n✯ Jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴJᴏʏ sᴜᴘᴇʀ Hɪɢʜ ǫᴜᴀʟɪᴛʏ ᴄʜᴀᴛ\n\n━━━━━━━━━━━━━━━━━━❥**""",
            reply_markup=InlineKeyboardMarkup(STBUTTON)
        )
        await bot.send_message(
                LOG_GROUP_ID,
                f"{message.from_user.mention} has just started Bot.\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
        )

    
@bot.on_message(filters.command(["/start", f"start@{BOT_USERNAME}", "/alive", ".alive"]) & filters.group)
async def start(client: Client, message: Message):
    response = requests.get(url).json()
    try:
        up = response['url']
        await message.reply_photo(up,
            caption=f"""**━━━━━━━━━━━━━━━━━━❥\n\n✯ Hᴇʟʟᴏ Tʜᴇʀᴇ I'ᴍ A Aɪ Bᴀsᴇᴅ Cʜᴀᴛ Bᴏᴛ ✨\n✯ Mʏ Nᴀᴍᴇ Is Ꮥʜꫝʟɪɴɪ cɦαƭ ɓσƭ\n✯ ᴛᴏ ᴇɴᴀʙʟᴇ ᴄʜᴀᴛ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴛʏᴘᴇ \n✯ /chatbot on|off \n✯ Jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴJᴏʏ sᴜᴘᴇʀ Hɪɢʜ ǫᴜᴀʟɪᴛʏ ᴄʜᴀᴛ\n\n━━━━━━━━━━━━━━━━━━❥**""",
            reply_markup=InlineKeyboardMarkup(STBUTTON)
        )
    except:
        await message.reply_photo(up,
            caption=f"""**━━━━━━━━━━━━━━━━━━❥\n\n✯ Hᴇʟʟᴏ Tʜᴇʀᴇ I'ᴍ A Aɪ Bᴀsᴇᴅ Cʜᴀᴛ Bᴏᴛ ✨\n✯ Mʏ Nᴀᴍᴇ Is Ꮥʜꫝʟɪɴɪ cɦαƭ ɓσƭ\n✯ ᴛᴏ ᴇɴᴀʙʟᴇ ᴄʜᴀᴛ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴛʏᴘᴇ \n✯ /chatbot on|off \n✯ Jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴJᴏʏ sᴜᴘᴇʀ Hɪɢʜ ǫᴜᴀʟɪᴛʏ ᴄʜᴀᴛ\n\n━━━━━━━━━━━━━━━━━━❥**""",
            reply_markup=InlineKeyboardMarkup(STBUTTON)
        )


@bot.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    vdb = MongoClient(MONGO_URL)    
    v = vdb["vDb"]["v"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                " 𝐇𝐞𝐲 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀 𝐀𝐝𝐦𝐢𝐧 "
            )
    is_v = v.find_one({"chat_id": message.chat.id})
    if not is_v:
        v.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 🥀!")
    if is_v:
        await message.reply_text(f" 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐭 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 ")
    

@bot.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    vdb = MongoClient(MONGO_URL)    
    v = vdb["vDb"]["v"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_v = v.find_one({"chat_id": message.chat.id})
    if not is_v:           
        await message.reply_text(f"𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐲𝐄𝐧𝐚𝐛𝐥𝐞𝐝")
    if is_v:
        v.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐄𝐧𝐚𝐛𝐥𝐞𝐝 ")
    

@bot.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"** 𝐔𝐬𝐚𝐠𝐞  :**\n/chatbot [on|off] 𝐎𝐧𝐥𝐲 𝐆𝐫𝐨𝐮𝐩 ")


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       if not is_v:
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_v:                   
               await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       if not is_v:
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_v:                    
               await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def vprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")


@bot.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.first_name if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        matlabi_jhanto = message.chat.title
        response = requests.get("https://nekos.best/api/v2/neko").json()
        image_url = response["results"][0]["url"]
        served_chats = len(await get_served_chats())
        chat_id = message.chat.id
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = await client.export_chat_invite_link(message.chat.id)
        for member in message.new_chat_members:
            if member.id == bot.id:
                count = await bot.get_chat_members_count(chat_id)
        msg = (
            f"❄️ <b><u>ʙᴏᴛ #ᴀᴅᴅᴇᴅ ᴛᴏ ɴᴇᴡ ɢʀᴏᴜᴘ </u></b> \n\n"
            f"┏━━━━━━━━━━━━━━━━━┓\n"
            f"┣★ **ᴄʜᴀᴛ** › : {matlabi_jhanto}\n"
            f"┣★ **ᴄʜᴀᴛ ɪᴅ** › : {chat_id}\n"
            f"┣★ **ᴄʜᴀᴛ ᴜɴᴀᴍᴇ** › : @{message.chat.username}\n"
            f"┣★ **ɢʀᴏᴜᴘ ʟɪɴᴋ** › : [ᴛᴏᴜᴄʜ]({chatusername}) \n"
            f"┣★ **ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs** › : {count}\n"
         #   f"┣★ **ᴛᴏᴛᴀʟ ᴄʜᴀᴛ** › : {served_chats}\n"
            f"┣★ **ᴀᴅᴅᴇᴅ ʙʏ** › : {added_by} \n"
            f"┗━━━━━━━━━★ "
        )
        await bot.send_photo(LOG_GROUP_ID, photo=image_url, caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("sᴇᴇ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɢʀᴏᴜᴘ", url=chatusername)]
        ]))

@bot.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await bot.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        response = requests.get("https://nekos.best/api/v2/neko").json()
        image_url = response["results"][0]["url"]
        chat_id = message.chat.id
        left = (
            f"❄️ <b><u>ʙᴏᴛ #ʟᴇғᴛ_ɢʀᴏᴜᴘ </u></b> \n\n"
            f"๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {title}\n"
            f"๏ ɢʀᴏᴜᴘ ɪᴅ ➠ {chat_id}\n"
            f"๏ ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➠ {remove_by}\n"
           # f"๏ ʙᴏᴛ ɴᴀᴍᴇ ➠ @{app.username}"
        )
        await bot.send_photo(LOG_GROUP_ID, photo=image_url, caption=left, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]
        ]))
       
bot.start()
print("successfully deployed bot ")
idle()
