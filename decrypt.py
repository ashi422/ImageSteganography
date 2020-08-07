import cv2
from getpass import getpass
import hashlib
import os
import numpy as np
import csv

m = input("Enter location of img.npy : ")
h = np.load(m)

t=[]
p=input("Enter location of data.csv file : ")
with open(p, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        t.append(row)
    file.close()

key=t[0][0]
l=int(t[0][1])

d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)

img = str(input("Enter encrypted image location : "))
q = cv2.imread(img)

dkey=""
def decrypt():
    global dkey
    dkey=hashlib.md5(getpass("Enter Steganography key : ").encode()).hexdigest()
    if dkey==key:
        print("Steganography key entered correctly. You are all set to decrypt!")
    else:
        print("Steganography key entered incorrectly. Please try again.")
        decrypt()

decrypt()

kl=0
x=0
y=0
z=0


hiddnmsg=""
for i in range(l-1):
    global dkey
    hiddnmsg+=c[h[x,y,z]^d[dkey[kl]]]
    x=x+1
    y=y+1
    y=(y+1)%3
    kl=(kl+1)%len(dkey)

os.remove(p)
print("The Hidden Message is : ", hiddnmsg)
