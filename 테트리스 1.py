#import
import time
import random
import os
import keyboard


# #블럭 가시화
blocks = [ [ [0,1,0,0] , [1,1,1,0] , [0,0,0,0] , [0,0,0,0] ] , 
 [ [0,0,0,0] , [0,1,1,0] , [0,1,1,0] , [0,0,0,0] ], 
 [ [0,0,0,0] , [1,0,0,0] , [1,1,1,0] , [0,0,0,0] ], 
 [ [0,1,0,0] , [0,1,0,0] , [0,1,1,0] , [0,0,0,0] ], 
 [ [0,0,1,0] , [0,0,1,0] , [0,0,1,0] , [0,0,1,0] ],
 [ [0,0,0,0] , [1,1,0,0] , [0,1,1,0] , [0,0,0,0] ],
 [ [0,0,0,0], [0,0,1,1] , [0,1,1,0] , [0,0,0,0] ] ]

# #스코어
# score = 0

# #시간에 따른 변화

# #

#회전 함수
def spin(blk_ori) :
    blk_spin = [[],[],[],[]]
    for i in range(4) :
        for j in range(4) :
            blk_spin[i].append(blk_ori[j][i])
    for i in range(4) :
        blk_spin[i].reverse()
    return blk_spin


#블럭 랜덤선택

def reset(a) :
    a[0] = 2
    b = random.choice(blocks)
    return b

score = 0
#줄 삭제

#레벨

#스크린 툴
MAX_Y = 30
MAX_X = 20
bode = [[0 for _ in range(MAX_X)] for _ in range(MAX_Y)]
counter = 0
block_axis = [2,7]
bode[0] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
bode[MAX_Y-1] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
for i in range(MAX_Y) :
    bode[i][0] = 1
    bode[i][MAX_X-1] = 1
block = random.choice(blocks)

block = random.choice(blocks)
block_axis[0] = 2
while True :
    counter += 1
    
    time.sleep(0.0001)
           
    
    
    
    
    if counter ==10:
        counter =0
        
        
        block_axis[0]+=1
        flag = False
        for i in range(4):
            for j in range(4):
                if block[i][j] == 1 and bode[block_axis[0] + i][block_axis[1] + j] == 1:
                    block_axis[0] -=1
                    flag = True
                    break
            if flag == True:
                break
        
        if flag == True:
            for i in range(4):
                for j in range(4):
                    if block_axis[0] + i < MAX_Y and block_axis[1] + j < MAX_X and block[i][j] == 1:
                        bode[block_axis[0] + i][block_axis[1] + j] = block[i][j]
            block_axis[0] =2
            block = random.choice(blocks)
            flag = False
            
                    
            # if flag == False :
            #     break
                        
    
        tmp_blocK_list= [[block_axis[0]+i//4,block_axis[1]+i%4] for i in range(15)]
        os.system("cls")
        for i in range(MAX_Y) :
            for j in range(MAX_X) :
                if [i,j] in tmp_blocK_list and block[i - block_axis[0]][j - block_axis[1]] == 1:
                    print("■", end="")
                    
                elif bode[i][j] == 1 :
                    print("■", end='')
                else :
                    print(" ", end='')
            print()
            
