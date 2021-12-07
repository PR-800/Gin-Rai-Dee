import random
from firebase import firebase
firebase = firebase.FirebaseApplication("https://pythondatabase-7cf3e-default-rtdb.firebaseio.com/", None)
result = firebase.get('/TEST DATABASE/FIREBASE', '')
print(random.choice(result['-MqI715kaS7gPULwULUN']))
