"""Gin-Rai-Dee : Waiter bot"""

import random
import discord
from discord.ext import commands
import asyncio
from firebase import firebase
firebase = firebase.FirebaseApplication(
    "https://pythondatabase-7cf3e-default-rtdb.firebaseio.com/", None
)

# THAI
def th_sweets():
    """สุ่มขนมหวาน"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIDKF4XvF2Ue2PBsgk'])

def th_drinks():
    """สุ่มเครื่องดื่ม"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIEOSGNvYSltNmI-Lz'])

def th_savory():
    """สุ่มข้าว"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIF--345JGhIZbZK2r'])

def th_noodles():
    """สุ่มเส้น"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIFb8GCUqCFJvwJvKJ'])

def th_fbuffet():
    """สุ่ม Buffet"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqI715kaS7gPULwULUN'])

def th_fast_food():
    """สุ่มอาหาร Fast_food"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqJGglyeYE6ccXqkdXH'])

def th_words():
    """สุ่มคำพูด"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIGY61JS9ZqG78zmU3'])

def th_healthfood():
    """สุ่มอาหารเพื่อสุขภาพ"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIGm54hVQpDVZGzh-D'])

def th_fruits():
    """สุ่มผลไม้"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIMrbs48uvLrLWouT4'])

def sticker():
    """สุ่มสติ๊กเกอร์"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIH3RgiLZBBgTuVu9J'])

#ENGLISH
def en_sweets():
    """random sweets"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIHMuf_ncVlMR_KpNI'])

def en_drinks():
    """random drinks"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIHb6hxroKZtSNB2i8'])

def en_words():
    """random speech"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIHmdB6VTNe2IdCHZ4'])

def en_fastfood():
    """random fastfood"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqJGqEVk-_kfNSf6066'])

def en_healthfood():
    """random healthfood"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIIJUdS90Nvd2FdBjR'])

def en_savory():
    """random savory"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIIdGMKJ_alYMXdAIB'])

def en_fbuffet():
    """random Buffet"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIIpNfAg8vtyf7J7H2'])

def en_fruits():
    """random Fruit"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIN6ZdJnkOTrdH23t4'])

def main():
    """Function Gin-Rai-Dee : Waiter bot"""
    token = input()
    bot = commands.Bot(command_prefix = 'g! ')
    bot.remove_command('help')

    @bot.event
    async def on_ready():
        print("Let's go!")

    @bot.event
    async def on_message(message):
        async with message.channel.typing():
            await asyncio.sleep(0.1)
        await bot.process_commands(message)

    @bot.command()
    async def help(ctx):
        await ctx.send('```ชุดคำสั่งสำหรับเรียกใช้งานบอทจะขึ้นต้นด้วย g! เสมอ โดยจะมีหัวข้อหลักและย่อย ดังนี้\
            \n🥗  g! อาหารคลีน\n🍔  g! ฟาสต์ฟู้ด\n🍲  g! บุฟเฟ่ต์\n🍛  g! ข้าว\n🍜  g! เส้น\n🍰  g! ขนมหวาน\
            \n☕  g! เครื่องดื่ม\n🍎  g! ผลไม้\n\
            \nBot commands for Gin-Rai-Dee always begin with g! as follows:\n🥗  g! cleanfood\
            \n🍔  g! fastfood\n🍲  g! buffet\n🍛  g! savory\n🍰  g! sweets\n☕  g! drinks\
            \n🍎  g! fruits```')

    #THAI
    @bot.command()
    async def อาหารคลีน(ctx):
        await ctx.send('```เราขอแนะนำเมนูเพื่อสุขภาพนี่เลย! : ' + th_healthfood() + sticker() + '```')
    @bot.command()
    async def ฟาสต์ฟู้ด(ctx):
        await ctx.send("```" + th_words() + th_fast_food() + sticker() + "\n" \
        + "(การกินอาหารประเภทนี้บ่อยๆ ส่งผลเสียต่อสุขภาพมากเลยนะ! อย่ากินบ่อยนักละ <3) ```")
    @bot.command()
    async def บุฟเฟ่ต์(ctx):
        await ctx.send("```" + th_words() + th_fbuffet() + sticker() + "```")
    @bot.command()
    async def ข้าว(ctx):
        await ctx.send("```" + th_words() + th_savory() + sticker() + "```")
    @bot.command()
    async def เส้น(ctx):
        await ctx.send("```" + th_words() + th_noodles() + sticker() + "```")
    @bot.command()
    async def ขนมหวาน(ctx):
        await ctx.send('```' + th_words() + th_sweets() + sticker() + '```')
    @bot.command()
    async def เครื่องดื่ม(ctx):
        await ctx.send('```' + th_words() + th_drinks() + sticker() + "```")
    @bot.command()
    async def ผลไม้(ctx):
        await ctx.send('```' + th_words() + th_fruits() + sticker() + "```")

    #ENGLISH
    @bot.command()
    async def cleanfood(ctx):
        await ctx.send('```We highly recommend this one! : ' + en_healthfood() + sticker() + '```')
    @bot.command()
    async def fastfood(ctx):
        await ctx.send('```' + en_words() + en_fastfood() + sticker() + "\n" \
        + "(This kind of food is unhealthy and will negatively affect your health. Don't eat too often <3) ```")
    @bot.command()
    async def savory(ctx):
        await ctx.send("```" + en_words() + en_savory() + sticker() + "```")
    @bot.command()
    async def buffet(ctx):
        await ctx.send("```" + en_words() + en_fbuffet() + sticker() + "```")
    @bot.command()
    async def sweets(ctx):
        await ctx.send('```' + en_words() + en_sweets() + sticker() + '```')
    @bot.command()
    async def drinks(ctx):
        await ctx.send('```' + en_words() + en_drinks() + sticker() + "```")
    @bot.command()
    async def fruits(ctx):
        await ctx.send('```' + en_words() + en_fruits() + sticker() + "```")

    bot.run(token)
main()
