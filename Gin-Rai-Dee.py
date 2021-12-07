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
    return random.choice(result['-MqIG8r4S7-KfOQofd5l'])

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
def en_sweets(order):
    """random sweets"""
    ans = {'sweet' : ['small chocolate cake', 'marble cake', 'pumpkin bread',\
                'chocolate pound cake', 'soft pumpkin cookies', 'sugar cookies',\
                'biscoff cookies', 'red velvet cookies','tahini cookies',\
                'banana cupcakes', 'brownies', 'chocolate', 'caramel slice',\
                'chocolate coconut slice', 'easter egg rocky road',\
                'lemon slice', 'easy vanilla cheesecakes', 'sour cream cake', \
                'classic trifle', 'chocolate bread', 'vegan chocolate cake'], \
                'drinks' : ['coffee', 'iced tea', 'hot chocolate', 'juice', 'milkshake', 'tea',\
                'milk', 'green tea', 'chocolate milk', 'smoothie', 'bahamas punch', \
                'spiced pineapple cooler', 'lychee spritzer', 'coconut milk',\
                'pomegranate sparkle', 'blue thyme', 'life hacker', 'orange juice',\
                'upside down blue lemonade', 'lemonade', 'cocoa', 'tea bag']}
    return ans[order]

def en_words():
    """random speech"""
    words = ['Where there is good food, there is happiness : ',\
            'To live a full life, you have to fill your stomach first : ', \
            'Food is really and truly the most effective medicine : ',\
            'They told me to follow my heart. Guess where it led me? To the fridge : ',\
            'We only live once… Lick the bowl.', 'You can’t live a full life on an empty stomach : ',\
            'Come on, hog it out! : ', 'There is no “we” in fries. Remember that! : ',
            'My favorite hobby is eating : ', 'Savor the flavor : ']
            
    return words

def en_fastfood():
    """random fastfood"""
    fast_food = ['waffle fries', 'double-double', 'fries', 'chicken sandwich', 'curly fries',\
                'bacon cheeseburger', 'animal style burger', 'mcnuggets', 'cheesy gordita crunch',\
                'pretzel', 'spicy chicken sandwich', 'chicken tenders', 'biscuits', 'blizzard',\
                'pizza', 'glazed doughnut', 'mcgriddle', 'subway', 'church\'s chicken honey butter biscuits',\
                'panda express orange chicken', 'checkers seasoned fries', 'donut', 'big mac']
    return fast_food

def en_healthfood():
    """random healthfood"""
    ans = ['Breakfast Casserole', 'Giada\'s Broiled Salmon with Herb Mustard Glaze', 'Whole30 Bacon and Egg Cups',\
        'Slow-Cooker Pork Tacos', 'Vegetable Noodle Soup', 'Angel Food Cake', 'Blueberry Compote', 'Giada\'s Chicken Saltimboccaง', \
        'Spaghetti Squash and Meatballs', 'Ellie\'s Tuscan Vegetable Soup', 'Quinoa Salad', 'Low-Cal Fettuccine Alfredo',\
        'Giada\'s Chia Seed Pudding', 'Hasselback Sweet Potatoes', ' Beef Stir-Fry', 'Gazpacho', 'Healthy Cauliflower Rice',\
        'American Macaroni Salad', 'Chicken and Broccoli Stir-Fry', 'Oven-Baked Salmon', 'Ina\'s Roasted Brussels Sprouts']
    return ans

def en_savory():
    """random savory"""
    ans = ['Chilli cheese toats', 'Cheesy Macaroni', 'Spaghetti Bolognese', 'Curry soup', \
    'Gravy Noodles', 'Spaghetti Carbonara', 'Roast pork', 'Fish and chips', 'Macaroni', \
    'Meatlolf', 'Meatballs', 'Omelette', 'Oxtail Soup', 'Pasta with truffle cream sauce', \
    'Bolognese fettuccine', 'mac and cheese']
    return ans

def en_fbuffet():
    """random Buffet"""
    buffet = ['MK', 'Grilled Butter', 'Shabushi', 'Shabu', 'MOMO Paradise'\
            'Khun Phon Yang Kham', 'King Kong Yakiniku Buffet',\
            'Oishi Eaterium','barbqplaza', 'Japaness Buffet',\
            'Suki Teenoi', 'CP-Harbour Resaurant', 'Copper Buffet', 'Daruma']
    return buffet

def main():
    """Function Gin-Rai-Dee : Waiter bot"""
    #token = input()
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
        await ctx.send('```We highly recommend this one! : ' + random.choice(en_healthfood()) + random.choice(sticker()) + '```')
    @bot.command()
    async def fastfood(ctx):
        await ctx.send('```' + random.choice(en_words()) + random.choice(en_fastfood()) + random.choice(sticker()) + "\n" \
        + "(This kind of food is unhealthy and will negatively affect your health. Don't eat too often <3) ```")
    @bot.command()
    async def savory(ctx):
        await ctx.send("```" + random.choice(en_words()) + random.choice(en_savory()) + random.choice(sticker()) + "```")
    @bot.command()
    async def buffet(ctx):
        await ctx.send("```" + random.choice(en_words()) + random.choice(en_fbuffet()) + random.choice(sticker()) + "```")
    @bot.command()
    async def sweets(ctx):
        await ctx.send('```' + random.choice(en_words()) + random.choice(en_sweets('sweet')) + random.choice(sticker()) + '```')
    @bot.command()
    async def drinks(ctx):
        await ctx.send('```' + random.choice(en_words()) + random.choice(en_sweets('drinks')) + random.choice(sticker()) + "```")

    bot.run(token)

main()
