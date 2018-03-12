num = 10
print('Guess A Number')
a = int(input())
while a!=num:
 if a > num:
  print('too big')
  a = int(input())
 if a < num:
  print('too small')
  a = int(input())
# if a == num:
print('BINGO')

#
# print('too small?')
# print(a<num)
#
# print('equal?')
# print(a==num)
# print(a)