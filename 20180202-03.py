from random import randint

# num = 10
num=randint(5,10)
print('Guess A Number')
a = int(input())
while a!=num:
 if a > num:
  print (str(a)+' is too big') # print('%s is too big'%a)
  a = int(input())
 if a < num:
  print('%s is too small' % a)
  a = int(input())
 if a<0:
  print('Exit game')
  break
# if a == num:
print('BINGO')
