# on_massageで発火するクラス
class Message:
    async def active(self, message):
        if message.content == '!p':
            await message.channel.send('リズムよんだと思った？')
