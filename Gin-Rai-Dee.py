"""Gin-Rai-Dee : Waiter bot"""

# import modules ที่จำเป็นต้องใช้
import random # สำหรับใช้งานคำสั่ง random เพื่อสุ่มเมนูอาหาร
import discord # สำหรับใช้งานคำสั่งที่เกี่ยวข้องกับ discord
from discord.ext import commands # ส่วนขยายจาก discord และแพ็คเกจ commands
import asyncio  # สำหรับใช้งานคำสั่งหน่วงเวลา typing ในการตอบกลับของบอท (บรรทัดที่ 115)
from firebase import firebase # สำหรับใช้คำสั่ง firebase เพื่อเก็บข้อมูลเมนูอาหาร
firebase = firebase.FirebaseApplication(
    "https://pythondatabase-7cf3e-default-rtdb.firebaseio.com/", None   # link database ที่เก็บข้อมูลเมนูแต่ละประเภท
)

# THAI
def th_sweets():
    """สุ่มขนมหวาน"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIDKF4XvF2Ue2PBsgk']) #-MqIDKF4XvF2Ue2PBsgk เป็น key สำหรับเก็บข้อมูลเมนูอาหารประเภทขนมหวาน(ภาษาไทย)

def th_drinks():
    """สุ่มเครื่องดื่ม"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIEOSGNvYSltNmI-Lz']) #-MqIEOSGNvYSltNmI-Lz เป็น key สำหรับเก็บข้อมูลเมนูเมนูอาหารประเภทเครื่องดื่ม(ภาษาไทย)

def th_savory():
    """สุ่มข้าว"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIF--345JGhIZbZK2r']) #-MqIF--345JGhIZbZK2r เป็น key สำหรับเก็บข้อมูลเมนูอาหารประเภทข้าว(ภาษาไทย)

def th_noodles():
    """สุ่มเส้น"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIFb8GCUqCFJvwJvKJ']) #-MqIFb8GCUqCFJvwJvKJ เป็น key สำหรับเก็บข้อมูลเมนูอาหารประเภทเส้น(ภาษาไทย)

def th_fbuffet():
    """สุ่ม Buffet"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqI715kaS7gPULwULUN']) #-MqI715kaS7gPULwULUN เป็น key สำหรับเก็บข้อมูลเมนูอาหารประเภท Buffet(ภาษาไทย)

def th_fast_food():
    """สุ่มอาหาร Fast_food"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqJGglyeYE6ccXqkdXH']) #-MqJGglyeYE6ccXqkdXH เป็น key สำหรับเก็บข้อมูลเมนู fastfood(ภาษาไทย)

def th_words():
    """สุ่มคำพูด"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIGY61JS9ZqG78zmU3']) #-MqIGY61JS9ZqG78zmU3 เป็น Key สำหรับเก็บข้อมูลข้อความที่ใช้ตอนแนะนำเมนู (ภาษาไทย)

def th_healthfood():
    """สุ่มอาหารเพื่อสุขภาพ"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIGm54hVQpDVZGzh-D']) #-MqIGm54hVQpDVZGzh-D เป็น key สำหรับเก็บข้อมูลเมนูอาหารเพื่อสุขภาพ(ภาษาไทย)

def th_fruits():
    """สุ่มผลไม้"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIMrbs48uvLrLWouT4']) #-MqIMrbs48uvLrLWouT4 เป็น key สำหรับเก็บข้อมูลเมนูผลไม้(ภาษาไทย)

def sticker():
    """สุ่มสติ๊กเกอร์"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIH3RgiLZBBgTuVu9J']) #-MqIH3RgiLZBBgTuVu9J เป็น key สำหรับเก็บสติกเกอร์ที่ใช้ในข้อความที่สุ่มเมนูออกมา

#ENGLISH
def en_sweets():
    """random sweets"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIHMuf_ncVlMR_KpNI']) #-MqIHMuf_ncVlMR_KpNI เป็น key สำหรับเก็บข้อมูลเมนูอาหารประเภทขนมหวาน(ภาษาอังกฤษ)

def en_drinks():
    """random drinks"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIHb6hxroKZtSNB2i8']) #-MqIHb6hxroKZtSNB2i8 เป็น key สำหรับเก็บข้อมูลเมนูเมนูอาหารประเภทเครื่องดื่ม(ภาษาอังกฤษ)

def en_words():
    """random speech"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIHmdB6VTNe2IdCHZ4']) #-MqIHmdB6VTNe2IdCHZ4 เป็น Key สำหรับเก็บข้อมูลข้อความที่ใช้ตอนแนะนำเมนู(ภาษาอังกฤษ)

def en_fastfood():
    """random fastfood"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqJGqEVk-_kfNSf6066']) #-MqJGqEVk-_kfNSf6066 เป็น key สำหรับเก็บข้อมูลเมนูอาหารประเภทฟาสต์ฟู้ด(ภาษาอังกฤษ)

def en_healthfood():
    """random healthfood"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIIJUdS90Nvd2FdBjR']) #-MqIIJUdS90Nvd2FdBjR เป็น key สำหรับเก็บข้อมูลเมนูอาหารเพื่อสุขภาพ(ภาษาอังกฤษ)

def en_savory():
    """random savory"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIIdGMKJ_alYMXdAIB']) #-MqIIdGMKJ_alYMXdAIB เป็น key สำหรับเก็บข้อมูลเมนูอาหารประเภทข้าว(ภาษาอังกฤษ)

def en_fbuffet():
    """random Buffet"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIIpNfAg8vtyf7J7H2']) #-MqIIpNfAg8vtyf7J7H2 เป็น key สำหรับเก็บข้อมูลเมนูอาหารประเภทบุฟเฟต์(ภาษาอังกฤษ)

def en_fruits():
    """random Fruit"""
    result = firebase.get('/TEST DATABASE/FIREBASE', '')
    return random.choice(result['-MqIN6ZdJnkOTrdH23t4']) #-MqIN6ZdJnkOTrdH23t4 เป็น key สำหรับเก็บข้อมูลอาหารประเภทผลไม้(ภาษาอังกฤษ)

def main():
    """Function Gin-Rai-Dee : Waiter bot"""
    bot = commands.Bot(command_prefix = 'g! ') #กำหนดคำสั่งเรียกใช้บอท ซึ่งจะขึ้นต้นด้วย g!
    bot.remove_command('help') #ลบ command help ออก เพื่อสร้างและกำหนดรูปแบบใหม่

    #เมื่อบอทพร้อมใช้งานจะแสดงข้อความ 'Ready' ใน Terminal
    @bot.event
    async def on_ready():
        print("Ready")

    #เมื่อมีการเรียกใช้งาน บอทจะแสดง Bot is typing.. ใต้ช่องข้อความเป็นเวลา 0.05 วินาที
    @bot.event
    async def on_message(message):
        async with message.channel.typing():
            await asyncio.sleep(0.05)
        await bot.process_commands(message)

    # new command help
    @bot.command()
    async def help(ctx):
        await ctx.send('```ชุดคำสั่งสำหรับเรียกใช้งานบอทจะขึ้นต้นด้วย g! เสมอ โดยจะมีหัวข้อหลักและย่อย ดังนี้\
            \n🥗  g! อาหารคลีน\n🍔  g! ฟาสต์ฟู้ด\n🍲  g! บุฟเฟ่ต์\n🍛  g! ข้าว\n🍜  g! เส้น\
            \n🍰  g! ขนมหวาน\n☕  g! เครื่องดื่ม\n🍎  g! ผลไม้\n\
            \nBot commands for Gin-Rai-Dee always begin with g! as follows:\n🥗  g! cleanfood\
            \n🍔  g! fastfood\n🍲  g! buffet\n🍛  g! savory\n🍰  g! sweets\n☕  g! drinks\
            \n🍎  g! fruits\n\nสนใจดูปริมาณแคลอรี่ที่ควรได้รับต่อวันไหม? สามารถใช้คำสั่งนี้ได้เลย!\
            \nWant to know how much calories you should get per day? Try this command!:\
            \n💬  g! cal\n\nสนใจเทียบค่าดัชนีมวลกายไหม? สามารถใช้คำสั่งนี้ได้เลย!\
            \nWant to check your BMI? Try this command!\n💬  g! bmi\n\
            \nสนใจดูตารางอาหารแต่ละหมู่ไหม? สามารถใช้คำสั่งนี้ได้เลย!\
            \nWant to see the 5 food group? Try this command!\n💬  g! groups```')

    #PICS
    #คำสั่งสำหรับส่งข้อมูลรูปภาพแสดงปริมาณแคลอรี่ที่ควรได้รับต่อวัน
    @bot.command()
    async def cal(ctx):
        await ctx.send('https://i.postimg.cc/SRDxcPGd/calories.jpg') #link  ภาพแสดงปริมาณแคลอรี่ที่ควรได้รับต่อวัน

    #คำสั่งสำหรับส่งข้อมูลรูปภาพแสดงค่าดัชนีมวลกาย (bmi)
    @bot.command()
    async def bmi(ctx):
        await ctx.send('https://i.postimg.cc/bY6zJ0s1/bmi.jpg') #link ภาพตารางเทียบค่าดัชนีมวลกาย(bmi)

    #คำสั่งสำหรับส่งข้อมูลรูปภาพแสดงตารางอาหาร 5 หมู่
    @bot.command()
    async def groups(ctx):
        await ctx.send('https://i.postimg.cc/N0FXJ3dL/Groups.jpg') #link ภาพตารางอาหาร 5 หมู่

    #THAI
    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทอาหารคลีน (ภาษาไทย)
    @bot.command()
    async def อาหารคลีน(ctx):
        await ctx.send('```เราขอแนะนำเมนูเพื่อสุขภาพนี่เลย! : ' + th_healthfood() + sticker() + '```')

    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทฟาสต์ฟู้ด (ภาษาไทย)
    @bot.command()
    async def ฟาสต์ฟู้ด(ctx):
        await ctx.send("```" + th_words() + th_fast_food() + sticker() + "\n" \
        + "(การกินอาหารประเภทนี้บ่อยๆ ส่งผลเสียต่อสุขภาพมากเลยนะ! อย่ากินบ่อยนักละ <3) ```")

    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทบุฟเฟต์ (ภาษาไทย)
    @bot.command()
    async def บุฟเฟ่ต์(ctx):
        await ctx.send("```" + th_words() + th_fbuffet() + sticker() + "```")

    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทข้าว (ภาษาไทย)
    @bot.command()
    async def ข้าว(ctx):
        await ctx.send("```" + th_words() + th_savory() + sticker() + "```")

    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทเส้น (ภาษาไทย)
    @bot.command()
    async def เส้น(ctx):
        await ctx.send("```" + th_words() + th_noodles() + sticker() + "```")

    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทขนมหวาน (ภาษาไทย)
    @bot.command()
    async def ขนมหวาน(ctx):
        await ctx.send('```' + th_words() + th_sweets() + sticker() + '```')

    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทเครื่องดื่ม (ภาษาไทย)
    @bot.command()
    async def เครื่องดื่ม(ctx):
        await ctx.send('```' + th_words() + th_drinks() + sticker() + "```")

    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทผลไม้ (ภาษาไทย)
    @bot.command()
    async def ผลไม้(ctx):
        await ctx.send('```' + th_words() + th_fruits() + sticker() + "```")

    #ENGLISH
    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทอาหารคลีน (ภาษาอังกฤษ)
    @bot.command()
    async def cleanfood(ctx):
        await ctx.send('```We highly recommend this one! : ' + en_healthfood() + sticker() + '```')

    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทฟาสต์ฟู้ด (ภาษาอังกฤษ)
    @bot.command()
    async def fastfood(ctx):
        await ctx.send('```' + en_words() + en_fastfood() + sticker() + "\n" \
        + "(This kind of food is unhealthy and will negatively affect your health. Don't eat too often <3) ```")

    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทอาหารคาว (ภาษาอังกฤษ)
    @bot.command()
    async def savory(ctx):
        await ctx.send("```" + en_words() + en_savory() + sticker() + "```")

    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทบุฟเฟต์ (ภาษาอังกฤษ)
    @bot.command()
    async def buffet(ctx):
        await ctx.send("```" + en_words() + en_fbuffet() + sticker() + "```")

    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทขนมหวาน (ภาษาอังกฤษ)
    @bot.command()
    async def sweets(ctx):
        await ctx.send('```' + en_words() + en_sweets() + sticker() + '```')

    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทเครื่องดื่ม (ภาษาอังกฤษ)
    @bot.command()
    async def drinks(ctx):
        await ctx.send('```' + en_words() + en_drinks() + sticker() + "```")

    #คำสั่งบอทสำหรับสุ่มเมนูอาหารประเภทผลไม้ (ภาษาอังกฤษ)
    @bot.command()
    async def fruits(ctx):
        await ctx.send('```' + en_words() + en_fruits() + sticker() + "```")

    bot.run(token) #ใส่ token ของบอทสำหรับใช้งาน
main()
