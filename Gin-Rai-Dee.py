"""Gin-Rai-Dee : Waiter bot"""
def main():
    """Function Gin-Rai-Dee : Waiter bot"""
    import discord
    from discord.ext import commands

    token = input()
    bot = commands.Bot(command_prefix='-gin')

    @bot.event
    async def on_ready():
        print("Let's go!")

    @bot.event
    async def on_message(message):
        if message.content.startswith('-gin หิว'):
            await message.channel.send('รับอะไรดี!')
        if message.content.startswith('-gin ข้าว'):
            await message.channel.send('ลอง \'ข้าวมันไก่\' ดีไหม!')

    bot.run(token)
main()
