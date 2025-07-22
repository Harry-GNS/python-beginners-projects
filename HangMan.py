import random
list=['hassan','shoaib','zohaib']
word=random.choice(list)
print(word)
letters=[]
for i in range(10):
    letter=input('Guess a letter').lower()

    disp=''
    for i in word:

        if i == letter:
            disp+=i
            letters.append(letter)
        elif i in letters:
            disp+=i
        else:
            disp+='_'

    print(disp)
    if '_' not in disp:
        game=True
        print('You Win')