import cv2
from getpass import getpass
import hashlib
import os
import csv
import numpy as np

def data(hashkey,text):
    file = open('data.csv','r',newline='')
    row = (hashkey,text)
    writer = csv.writer(file)
    writer.writerow(row)
    file.close()

d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)

img = str(input("Enter image location : "))
h = cv2.imread(img)

i=h.shape[0]
j=h.shape[1]

key=""
ckey=""
def encrypt():
    global key
    global ckey
    key=hashlib.md5(getpass("Enter Steganography key : ").encode()).hexdigest()
    ckey=hashlib.md5(getpass("Re-enter Steganography key : ").encode()).hexdigest()
    if ckey==key:
        print("Steganography key entered correctly. You are all set to encrypt!")
    else:
        print("Steganography key entered incorrectly. Please try again.")
        encrypt()

encrypt()

text = input("Enter secret message : ")

l=len(text)
kl=0
x=0
y=0
z=0

for i in range(l):
    h[x,y,z]=d[text[i]]^d[key[kl]] 
    x=x+1
    y=y+1
    y=(y+1)%3
    kl=(kl+1)%len(key)

arr=np.array(h)
np.save('img.npy',arr)
data(key,l)

cv2.imwrite("encrypted_img.jpg",h)
