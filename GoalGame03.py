from random import choice

score_you = 0
score_com = 0
score = [0, 0]
print('Choose one side to shoot:')
print('left, center, right')

def kick():
    global score_you  #如果普通变量，则需要声明为全局变量 用list则不用(??)
    global score_com  #如果普通变量，则需要声明为全局变量 用list则不用(??)
    print('---------------You kick---------------' )
    you = input()  # you =str(input())
    print('You kicked ' + you)
    direction = ['left', 'center', 'right']
    com = choice(direction)
    print('Computer saved ' + com)
    if you != com:
        print('Goal!')
        score_you = score_you+1
        #score[0]+=1
    else:
        print('Oops...')
    print('---------------You save---------------')
    you = input()  # you =str(input())
    print('You save ' + you)
    direction = ['left', 'center', 'right']
    com = choice(direction)
    print('Computer kick ' + com)
    if you == com:
        print('sved!')
        # score_you += 1
    else:
        print('Oops...')
        score_com += 1
        #score[1]+=1
    print('-------------Game over : Your score :%d Computer Score:%d' % (score_you, score_com))
for i in range(5):
    print('---------------Round%d---------------' % (i + 1))
    kick()
while score_com==score_you:#score_com==score_you:
    print('---------------Round%d---------------' % (i + 1))
    kick()
if score_you>score_com:
    print("Congratulations! You win!")
else:
    print("Oops... You lose")


