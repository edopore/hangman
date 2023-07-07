import random

print('-------------------------------')
print('Welcome To HANGMAN...')

list_of_words = ["sun","dice",'bat']
lives = 6
word = random.choice(list_of_words)
wordFind = ['_' for x in range(len(word))]
remaining =  len(wordFind)
letterlst = ''

while  lives > 0:
    print('Lives remaining: ',lives)
    print('Letters Used: ',letterlst)
    print('-------------------------------')
    letterSelected = input("Put a letter: ")
    letterlst += letterSelected + ' '
    counter = 0

    for letter in range(len(word)):
        if(letterSelected==word[letter]):
            wordFind[letter] = word[letter] 
            counter += 1
            remaining -= 1
            print('Word: ',wordFind)

    if(remaining==0):
        print('Congratulations, you find the word!!')
        print('GAME OVER!!')
        break
    
    if (counter == 0):
        lives -= 1

if lives == 0:
    print('Fail, the word was: ',word)
    print('GAME OVER!!')
