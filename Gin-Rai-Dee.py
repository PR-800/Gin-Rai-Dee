"""Gin-Rai-Dee : Waiter bot"""
def savory(order):
    """สุ่มอาหารคาว"""
    if order == "rice":
        ans = ['ข้าวผัดทะล', 'ข้าวมันไก่', 'ข้าวขาหมู', \
        'ข้าวผัดกะเพรา', 'ข้าวหมูแดง', 'ข้าวคลุกกะปิ', 'ข้าวไข่ข้น', 'ข้าวยำไก่แซ่บ', \
        'ข้าวหน้าหมูทอด', 'ข้าวแกงกะหรี่หมูไข่ข้น', 'หอยทอด', 'ข้าวหน้าเนื้อ', 'ข้าวไข่เจียว', \
        'ข้าวน้ำพริกปลาทู', 'ข้าวผัดกระเทียม', 'ข้าวผัดกุนเชียง', 'ข้าวผัดต้มยำกุ้ง', 'ส้มตำ', \
        'ข้าวหมูกะเทียม', 'ข้าวต้มปลา', 'ข้าวยำ', 'ข้าวผัดปลาสลิด', 'ข้าวผัดเบคอน']
    elif order == "noodles":
        ans = ['ก๋วยเตี๋ยวหมูนำตก', 'สปาเก็ตตี้คาโบนาร่า', \
        'ราดหน้าเส้นใหญ่', 'ข้าวซอย', 'ผัดซีอิ๊ว', 'ขนมจีนแกงไก่', 'เย็นตาโฟ', \
        'ก๋วยจั๋บน้ำข้น', 'หมี่ผัดกระเฉดกุ้ง', 'ผัดมักกะโรนี', 'มาม่าผัดขี้เมา', 'ผัดไท', \
        'ก๋วยเตี๋ยวต้มยำ', 'ยำวุ้นเส้นรวมมิตร', 'ขนมจีนน้ำยาปู']
    return ans

def main():
    """Function Gin-Rai-Dee : Waiter bot"""
    import random
    import discord
    from discord.ext import commands

    token = input()
    bot = commands.Bot(command_prefix='-gin')

    @bot.event
    async def on_ready():
        print("Let's go!")

    @bot.event
    async def on_message(message):
        if message.content == '-gin อาหารจานเดียว':
            await message.channel.send('เลือกแบบไหนดี ข้าว / เส้น')
        if message.content == '-gin ข้าว':
            await message.channel.send(random.choice(words()) + random.choice(savory('rice')))
        if message.content == '-gin เส้น':
            await message.channel.send(random.choice(words()) + random.choice(savory('noodles')))

    bot.run(token)
main()
