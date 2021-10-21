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

def words():
    """สุ่มคำพูด"""
    words = ['ลองนี่ดูไหม? : ', 'อันนี้น่าอร่อยสุดๆ! : ', 'เคยลองเมนูนี้หรือยัง? :', 'เมนูนี้เลย! : ', \
            'เราว่านอกจากเราแล้วเมนูนี้ก็อร่อยนะ >_< : ', 'เห้ยเตง เมนูนี้ต้องลองแล้ว : ', \
            'กินก๋วยเตี๋ยว กินเกาเหลา กินเรา เอ้ย! กินนี่ดีกว่าไหม : ', 'นอกจากน้ำเกลือโรงบาลก็ยังมีเมนูนี้ที่น่ากิน : ',\
            'เธอว่าจะมีอะไรน่ากินมากกว่าเรา เอ๊ะหรือว่าจะเป็นเมนูนี้นะ แบร่ : ', 'หึ้ยๆ เมนูนี้ก็น่ากินน้า : ',\
            'วันนี้อากาศดีนะ งั้นลองหาอะไรอร่อยๆทานไหมคะ เมนูนี้เลย : ', 'วันนี้ขอเสนอเมนู : ',\
            'รักป่ารักเขา รักเราต้องคู่กับอาหารอร่อยๆอย่างนี้ --> ', 'แซ่บกว่ากระเพรา ก็เมนูตรงหน้าเรานี่แหละ : ',
            'กินๆไปเถอะ อ้วนแค่ไหนเธอก็น่ารัก : ', 'กินๆไปเถอะ อ้วนแค่ไหนก็เป็นแฟนเรา : ']
    return words

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
