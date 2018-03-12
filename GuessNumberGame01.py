
from random import randint
f=open('game.txt')
score=f.read().split()  #读取文件内容
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:       #计算平均轮数
   avg_times = float(total_times) / game_times
else:
   avg_times = 0
print(score)
def repareNumber(input,number):
    if (input>number):
        print('%s is too big'%input)
        return False
    elif (input<number):
        print('%s too small'%input)
        return False
    else:
        print('Bingo')
        return True
num=randint(5,10)

print("你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案"%(game_times,min_times,avg_times))
print('Guess A Number')
#a = int(input())
bingo= False
times = 0
while bingo==False:
 times +=1#记录游戏的轮数 轮数+1
 a=int(input())
 bingo=repareNumber(a,num)

if game_times==0 or times<min_times:#第一次或者本次轮数比最小轮数还小
     min_times=times
total_times+=times
game_times+=1
result='%d %d %d'%(game_times,min_times,total_times)
f=open('game.txt','w')
f.write(result)
f.close()



