import string
from threading import Thread
from hashlib import sha256
import time
import itertools
import random
print('Введите количество потоков:')
n = int(input())
print('Введите хэш-функцию:')
hashFunc = str(input())
alfabit = 'abcdefghijklmnopqrstuvwxyz'
password=''
pswrd = []
password = list(itertools.product(alfabit, repeat=5))

#74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f
#1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad zyzzx#
#3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b #apple
#74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f #mmmmm

start_time = time.time()
def generator(hashFunc):
    for word in password:
        word1 = str(word)
        word1 = str(word1).translate(str.maketrans('', '', string.punctuation))
        word1 = word1.replace(' ', '')
        if sha256(str(word1).encode()).hexdigest() == hashFunc:
            print(word)
            return word
            exit()


for i in range(n):
    thread = Thread(target=generator, args=(hashFunc,))
    thread.start()
    thread.join()
    break
print("--- %s seconds ---" % (time.time() - start_time))
