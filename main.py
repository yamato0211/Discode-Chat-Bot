import os
import discord
from dotenv import load_dotenv
from TalkAPI import Talk_API


load_dotenv()
TOKEN = os.environ.get("DISCODE_KEY")
chat = False

client = discord.Client()

@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    global chat
    if message.author.bot:
        return
    if message.content == "!chat" and chat == False:
        await message.channel.send("即位しました！")
        chat = True
        return
    if message.content == "!quit" and chat == True:
        await message.channel.send("さようなら！")
        chat = False
        return
    if chat:
        try:
            result = Talk_API(talk_context=message.content)
            await message.channel.send(result.json()["results"][0]["reply"])
        except: 
            await message.channel.send("もう一度おっしゃってください")
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
