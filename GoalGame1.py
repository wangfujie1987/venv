from random import choice
score_you = 0
score_com = 0
print ('Choose one side to shoot:')
print ('left, center, right')
for i in range(5):
   print('---------------Round%d-You kick---------------'%(i+1))
   you = input() #you =str(input())
   print ('You kicked ' + you)
   direction = ['left', 'center', 'right']
   com = choice(direction)
   print ('Computer saved ' + com)
   if you != com:
       print('Goal!')
       score_you +=1
   else:
       print('Oops...')
   print('---------------Round%d-You save---------------' % (i + 1))
   you = input()  # you =str(input())
   print('You save ' + you)
   direction = ['left', 'center', 'right']
   com = choice(direction)
   print('Computer kick ' + com)
   if you == com:
       print('sved!')
       #score_you += 1
   else:
    print('Oops...')
    score_com += 1
    print('-------------Game over : Your score :%d Computer Score:%d'%(score_you,score_com))
