from firebase import firebase
firebase = firebase.FirebaseApplication("https://pythondatabase-7cf3e-default-rtdb.firebaseio.com/", None)
def buffet():
    """สุ่ม Buffet"""
    buffet = ['หมูกะทะ', 'MK', 'ย่างเนย', 'ชาบูชิ', 'ชาบูนางใน', 'มานีมีหม้อ', ' ชาบูเพนกวิน',\
                'โคขุนโพนยางคำ', 'คิงคอง ยากินิกุ บุฟเฟต์', 'ร้านโซกริลล์', 'ฮอท พอท บุฟเฟต์', \
                'ไดโมอน', 'โออิชิ อีทเทอเรียม','บาร์บีคิว พลาซ่า', 'Japaness Buffet', 'ลาวา',\
                'สุกี้ตี๋น้อย', 'CP-Harbour Resaurant', 'Copper Buffet', 'Daruma',\
                'MOMO Paradise']
    return buffet
result = firebase.post('/TEST DATABASE/FIREBASE', buffet())
print(result)
