import cv2
import os
import numpy as np
import psycopg2


def create_table():
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = '' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS dogimages(image TEXT, hash TEXT)")
    conn.commit()
    conn. close()

def insert(image,hash):
    conn = psycopg2.connect("dbname = 'database1' user = 'postgres' password = '' host = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO dogimages VALUES (%s, %s)", (image, hash))
    conn.commit()
    conn. close()

def view():
    conn= psycopg2.connect("dbname = 'database1' user = 'postgres' password = '' host = 'localhost' port = '5432'")
    cur = conn. cursor()
    cur.execute("SELECT DISTINCT dogimages.hash FROM  dogimages")
    rows = cur.fetchall()
    conn.close()
    return rows





create_table()

def hashing(filename):
    im=cv2.imread(filename,1)
    im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    small_img=cv2.resize(im,(8,8))      
    img_mean=np.mean(small_img)
    bits=""
    for i in small_img.flat:
        if(i>img_mean):
            bits=bits+'1'

        else:
                bits=bits+'0'

             
    print(bits)

    parts = [bits[i:i+4] for i in range(0, len(bits), 4)]
    x=""
    for i in parts:
       x=x+(hex(int(i,2)))[2:]
          
    return bits

os.chdir('E:\Programming\Projects\Web DEv\iosd\images')
for index, filename in enumerate(os.listdir('.')):
  if(os.path.isfile(filename)):
      filehash=hashing(filename)
      insert(filename,filehash)


count=0;
temp=0;
y=view()
print(len(y[8][0][1]))
for i in range(len(view())):
    for j in range (i):
        for x in range (64):
            if(y[i][0][x]!=y[j][0][x]):
                temp=temp+1

    if temp>10:
        count=count+1
        temp=0          


print(count)






