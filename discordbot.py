# インストールした discord.py を読み込む
import discord
from config.const import InitConst
from event.message import Message

# 自分のBotのアクセストークンに置き換えてください
TOKEN = InitConst.TOKEN

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
    massageClass = Message()
    await massageClass.active(message)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)