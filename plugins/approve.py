from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserIsBlocked, PeerIdInvalid


@Client.on_chat_join_request()
async def accept_request(client, r):

    rm = InlineKeyboardMarkup([[
        InlineKeyboardButton("Blaster Hub", url=f"https://t.me/movieversepremium"),
        InlineKeyboardButton("Updates", url=f"https://t.me/movieversepremium")
    ]])
    
    try:
        await client.send_photo(
            r.from_user.id,
            'https://graph.org/file/5cb80fa6096997b7226b3.jpg',
            f"**Hello {r.from_user.mention}, Welcome To {r.chat.title}\nYour Request Has Been Approved...!!!**",
            reply_markup=rm)

    except UserIsBlocked:
        print("User blocked the bot")
    except PeerIdInvalid:
        print("Err")
    except Exception as e:
        print(f"#Error\n{str(e)}")

    await r.approve()
