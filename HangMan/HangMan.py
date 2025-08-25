import random
list=['hassan','shoaib','zohaib']
word=random.choice(list)
letters=[]
for i in range(10):
    print('You have',7-i,'guesses left')
    letter=input('Guess a letter:').lower()
    disp=''
    for i in word:
        if i == letter or i in letters:
            disp+=i
        else:
            disp+='_'
    if letter not in letters:
        letters.append(letter)
    print(disp)
    if '_' not in disp:
        game=True
        print('You Win')
        break
if '_' in disp:
    print('You Lose')
    print('The word was',word)
