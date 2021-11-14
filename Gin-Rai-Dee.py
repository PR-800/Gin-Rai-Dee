"""Gin-Rai-Dee : Waiter bot"""

#THAI
def th_sweets(order):
    """สุ่มขนมหวาน"""
    ans = {'sweet' : ['เค้กไข่ไต้หวัน', 'ทองหยอด', 'ทองหยิบ', 'ฝอยทอง', 'ขนมชั้น', 'ขนมต้ม',\
            'ขนมเบื้อง', 'บัตเตอร์เค้ก', 'เค้กฝอยทองใบเตย', 'เค้กชาไทยหน้านิ่ม',\
            'เค้กชิฟฟ่อนช็อกโกแลต', 'เค้กชิฟฟ่อนใบเตย','เค้กทุเรียน', 'เค้กช็อกโกแลตหน้านิ่ม',\
            'เค้กฝอยทองลาวา', 'เค้กกล้วยหอม', 'เค้กมะพร้าวอ่อนครีมสด', 'เค้กกาแฟ',\
            'เครปเค้ก', 'คัพเค้กเรดเวลเวท', 'ทองม้วน', 'ขนมปลากริม', 'บัวลอย',\
            'ครองแครง', 'หม้อแกง', 'สังขยามะพร้าวอ่อน','ขนมฟักทอง', 'ขนมมันม่วง', \
            'ข้าวเหนียวมะม่วง', 'วุ้นมะพร้าว', 'ไอศกรีมกะทิสด'], \
            'drinks' : ['กาแฟ', 'ชาเย็น', 'ชานมเย็น', 'โกโก้', 'นมเปรี้ยว', 'ชาอูหลง',\
            'น้ำส้ม', 'น้ำมะนาว', 'แชมเปญ', 'ชาไข่มุก', 'Bahamas Punch', \
            'Spiced Pineapple Cooler', 'Lychee Spritzer',\
            'Pomegranate Sparkle', 'Blue Thyme', 'Life Hacker',
            'Upside Down Blue Lemonade', 'รัมเสาวรส',\
            'น้ำเสาวรส', 'น้ำทับทิม', 'น้ำมะพร้าว', 'น้ำเบอร์รี่', 'น้ำแครอท']}
    return ans[order]

def th_savory(order):
    """สุ่มอาหารจานเดียว"""
    ans = {'rice' : ['ข้าวผัดทะล', 'ข้าวมันไก่', 'ข้าวขาหมู', \
        'ข้าวผัดกะเพรา', 'ข้าวหมูแดง', 'ข้าวคลุกกะปิ', 'ข้าวไข่ข้น', 'ข้าวยำไก่แซ่บ', \
        'ข้าวหน้าหมูทอด', 'ข้าวแกงกะหรี่หมูไข่ข้น', 'หอยทอด', 'ข้าวหน้าเนื้อ', 'ข้าวไข่เจียว', \
        'ข้าวน้ำพริกปลาทู', 'ข้าวผัดกระเทียม', 'ข้าวผัดกุนเชียง', 'ข้าวผัดต้มยำกุ้ง', 'ส้มตำ', \
        'ข้าวหมูกะเทียม', 'ข้าวต้มปลา', 'ข้าวยำ', 'ข้าวผัดปลาสลิด', 'ข้าวผัดเบคอน'], \
        'noodles' : ['ก๋วยเตี๋ยวหมูนำตก', 'สปาเก็ตตี้คาโบนาร่า', \
        'ราดหน้าเส้นใหญ่', 'ข้าวซอย', 'ผัดซีอิ๊ว', 'ขนมจีนแกงไก่', 'เย็นตาโฟ', \
        'ก๋วยจั๋บน้ำข้น', 'หมี่ผัดกระเฉดกุ้ง', 'ผัดมักกะโรนี', 'มาม่าผัดขี้เมา', 'ผัดไท', \
        'ก๋วยเตี๋ยวต้มยำ', 'ยำวุ้นเส้นรวมมิตร', 'ขนมจีนน้ำยาปู']}
    return ans[order]

def th_fbuffet():
    """สุ่ม Buffet"""
    buffet = ['หมูกะทะ', 'MK', 'ย่างเนย', 'ชาบูชิ', 'ชาบูนางใน', 'มานีมีหม้อ', ' ชาบูเพนกวิน',\
                'โคขุนโพนยางคำ', 'คิงคอง ยากินิกุ บุฟเฟต์', 'ร้านโซกริลล์', 'ฮอท พอท บุฟเฟต์', \
                'ไดโมอน', 'โออิชิ อีทเทอเรียม','บาร์บีคิว พลาซ่า', 'Japaness Buffet', 'ลาวา',\
                'สุกี้ตี๋น้อย', 'CP-Harbour Resaurant', 'Copper Buffet', 'Daruma',\
                'MOMO Paradise']
    return buffet

def th_fast_food():
    """สุ่มอาหาร Fast_food"""
    fast_food = ['แฮมเบอร์เกอร์', 'ฮอทด็อก', 'เฟรนช์ฟราย', 'คุกกี้ช็อกโกแลต', 'พิซซ่า', 'น้ำอดลม',\
                'ไก่ทอดเนื้อไร้กระดูก', 'ไอศกรีม', 'โดนัท', 'ขนมขบเคี้ยว', 'แซนด์วิชแฮมชีส',\
                'แซนด์วิชฮาวายเอียน', 'เบอร์เกอร์สเต๊กไก่สไปซี่', 'ชีสเบอร์เกอร์หมู', 'ข้าวยำไก่แซ่บ',\
                'KFC', 'ข้าวหมูทอดหน้าแกงกะหรี่ญี่ปุ่น', 'สปาเกตตีซี่โครงหมูอบซอส', 'ชีสทอด',\
                'ไก่นิวออร์ลีนส์', 'เฟรนช์ฟรายส์ราดชีส', 'ไก่ทอดบอนชอน', 'ไก่เขย่า']
    return fast_food

def th_words():
    """สุ่มคำพูด"""
    words = ['ลองนี่ดูไหม? : ', 'อันนี้น่าอร่อยสุดๆ! : ', 'เคยลองเมนูนี้หรือยัง? :', 'เมนูนี้เลย! : ', \
            'เราว่านอกจากเราแล้วเมนูนี้ก็อร่อยนะ >_< : ', 'เห้ยเตง เมนูนี้ต้องลองแล้ว : ', \
            'กินก๋วยเตี๋ยว กินเกาเหลา กินเรา เอ้ย! กินนี่ดีกว่าไหม : ', 'นอกจากน้ำเกลือโรงบาลก็ยังมีเมนูนี้ที่น่ากิน : ',\
            'เธอว่าจะมีอะไรน่ากินมากกว่าเรา เอ๊ะหรือว่าจะเป็นเมนูนี้นะ แบร่ : ', 'หึ้ยๆ เมนูนี้ก็น่ากินน้า : ',\
            'วันนี้อากาศดีนะ งั้นลองหาอะไรอร่อยๆทานไหมคะ เมนูนี้เลย : ', 'วันนี้ขอเสนอเมนู : ',\
            'รักป่ารักเขา รักเราต้องคู่กับอาหารอร่อยๆอย่างนี้ --> ', 'แซ่บกว่ากระเพรา ก็เมนูตรงหน้าเรานี่แหละ : ',
            'กินๆไปเถอะ อ้วนแค่ไหนเธอก็น่ารัก : ', 'กินๆไปเถอะ อ้วนแค่ไหนก็เป็นแฟนเรา : ']
    return words

def th_healthfood():
    ans = ['สลัดผลไม้ + ไข่ต้ม', 'สลัดโรลปูอัด', 'ข้าวกล้อง + น้ำพริกเห็ดหอม', 'ข้าวอกไก่อบ', \
    'ก๋วยเตี๋ยวลุยสวน', 'สุกี้แห้ง', 'แซนวิชไข่คนทูน่า', 'ปลานึ่ง + ผักต้ม', 'ไข่ตุ๋นทรงเครื่อง', \
    'ปลานึ่งซีอิ๊ว', 'ข้าว + แกงจืดเต้าหู้']
    return ans

def sticker():
    """สุ่มสติ๊กเกอร์"""
    ans = [' ｡◕‿◕｡', ' ⊙ω⊙', ' 😝', ' 💝', ' 😊', ' 💞', ' 🤩', ' 🥰', ' 💟', ' 💕', \
        ' 😋', ' 😍', ' 😘', ' 🤪', ' 😳', ' 😻', ' 🥰', ' 😀', ' 😃', ' 😄', ' 😁',\
        ' 🧡', ' 💛', ' 💙', ' 💚', ' 💜', ' 💘', ' 💖', ' 🌈', ' ✨', ' 😺', ' 😸',\
        ' 😎', ' 🤗', ' 🥳', ' 😇', ' 😉', ' 😊', ' ≧０≦', ' ♡^_^♡', '  ◕‿◕✿']
    return ans

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
    import random
    import discord
    from discord.ext import commands

    token = input()
    bot = commands.Bot(command_prefix = 'g! ')
    bot.remove_command('help')

    @bot.event
    async def on_ready():
        print("Let's go!")

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)

    @bot.command()
    async def help(ctx):
        await ctx.send('```ชุดคำสั่งสำหรับเรียกใช้งานบอทจะขึ้นต้นด้วย g! เสมอ โดยจะมีหัวข้อหลักและย่อย ดังนี้\n🥗  g! อาหารคลีน\n🍔  g! ฟาสต์ฟู้ด\
            \n🍲  g! บุฟเฟ่ต์\n🍛  g! อาหารจานเดียว\n\t\t- g! ข้าว\n\t\t- g! เส้น\n🍰  g! ขนมหวาน\n☕  g! เครื่องดื่ม\n\
            \nBot commands for Gin-Rai-Dee always begin with g! as follows:\n🥗  g! cleanfood\n🍔  g! fastfood\n🍲  g! buffet\
            \n🍛  g! savory\n🍰  g! sweets\n☕  g! drinks```')

    #THAI
    @bot.command()
    async def อาหารคลีน(ctx):
        await ctx.send('```เราขอแนะนำเมนูเพื่อสุขภาพนี่เลย! : ' + random.choice(th_healthfood()) + random.choice(sticker()) + '```')
    @bot.command()
    async def ฟาสต์ฟู้ด(ctx):
        await ctx.send("```" + random.choice(th_words()) + random.choice(th_fast_food()) + random.choice(sticker()) + "\n" \
        + "(การกินอาหารประเภทนี้บ่อยๆ ส่งผลเสียต่อสุขภาพมากเลยนะ! อย่ากินบ่อยนักละ <3) ```")
    @bot.command()
    async def บุฟเฟ่ต์(ctx):
        await ctx.send("```" + random.choice(th_words()) + random.choice(th_fbuffet()) + random.choice(sticker()) + "```")
    @bot.command()
    async def อาหารจานเดียว(ctx):
        await ctx.send("```" + random.choice(th_words()) + random.choice(th_savory(random.choice(['rice', 'noodle']))) + random.choice(sticker()) + "```")
    @bot.command()
    async def ข้าว(ctx):
        await ctx.send("```" + random.choice(th_words()) + random.choice(th_savory('rice')) + random.choice(sticker()) + "```")
    @bot.command()
    async def เส้น(ctx):
        await ctx.send("```" + random.choice(th_words()) + random.choice(th_savory('noodles')) + random.choice(sticker()) + "```")
    @bot.command()
    async def ขนมหวาน(ctx):
        await ctx.send('```' + random.choice(th_words()) + random.choice(th_sweets('sweet')) + random.choice(sticker()) + '```')
    @bot.command()
    async def เครื่องดื่ม(ctx):
        await ctx.send('```' + random.choice(th_words()) + random.choice(th_sweets('drinks')) + random.choice(sticker()) + "```")

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
