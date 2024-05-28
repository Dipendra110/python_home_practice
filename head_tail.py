import random
head_tail=[1,0]
print("Flip the coin:")
coin_flip=random.choice(head_tail)
print(coin_flip)
if coin_flip==1:
    print("Heads")
else:
    print("Tails")