# Çizim yapılacak kütüğhaneyi tanımlayalım.
from turtle import *


speed(100) # çizim hızı.
color('green') # rengi seçeneği ben burda yeşil seçtim.
bgcolor('black') # arka plan rengi ben siyah seçtim

b = 200

while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1

# Bitti !
