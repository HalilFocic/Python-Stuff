from pynput.keyboard import Key,Controller
keyboard = Controller()
import time

capital_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*("
simbols="!@#$%^&*(" 
def capital(slovo):

    
    with keyboard.pressed(Key.shift):
        keyboard.press(slovo.lower())
        keyboard.release(slovo.lower())

def play(znak):
    if znak==" ":
        return
    if znak in capital_letters:
        capital(znak)
    else:
        keyboard.press(znak)
        keyboard.release(znak)
def playFast(x,y):
    for i in range(x,y):
        if text[i+1]==" "and x!=y-1:
            play(text[i])
            time.sleep(0.09)
        else:
            play(text[i])



text="Gha Ghhh [hw] Gah Gpf Gpf Gp [0d] s Gha Ghhh [hw] Gah Gpf Gpf Gp [0d] s [a0]a a a a a [8a] p o o o o [9p] p p o I u 0 [0p] a a a a d d 8 s – o o [9p] a p o [0p] 0 a a d f 8 d a d d 9 d s a s [0a] p 0 a a p o p 9 a a p o 0 u 0 [9ey] p p d d p p d f [8wt] f d f f d f G h G G [9ey] p p d d [9ey] p p f f 8 z [lx] C [lzv] 8 u I o [wy] y y p [9e] o I [0ru] u u u I o 8 p o u I o [wy] – a p [9ep] o p [0a] a s a p [8o] a s [od] [ya] [yp] 2 [to] [yo] [3ud] [da] [1to] o o I y yassasassao"
time.sleep(2)
for i in range(0,len(text)):
    if text[i]==" " and text[i+1]==" ":
        time.sleep(0.5)
        i+=1
        continue
    if text[i]==" ":
        continue
    if text[i]=="[":
        counter =2
        for j in range(i,len(text)):
            if text[j]=="]":
               break
            counter+=1
        playFast(i+1,i+counter)
        i+=counter
        continue
    else:
        if i+1==len(text):
            break
        if text[i+1]==" " and i!=len(text)-1:
            play(text[i])
            time.sleep(0.35)
        else:
            play(text[i])
            time.sleep(0.15)
    
    
    
