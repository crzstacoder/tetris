#테트리스만들기
#11/6 시작


#import
import time
import random
import os
import keyboard
from pynput.keyboard import Listener, Key
import tkinter

key = 0

    
# #블럭 가시화
blocks = [ [ [0,1,0,0] , [1,1,1,0] , [0,0,0,0] , [0,0,0,0] ] ,                  #ㅗ자블럭
 [ [0,0,0,0] , [0,1,1,0] , [0,1,1,0] , [0,0,0,0] ],                             #ㅁ자블럭
 [ [0,0,0,0] , [1,0,0,0] , [1,1,1,0] , [0,0,0,0] ],                             #ㄴ자블럭
 [ [0,1,0,0] , [0,1,0,0] , [0,1,1,0] , [0,0,0,0] ],                             #L자블럭
 [ [0,0,1,0] , [0,0,1,0] , [0,0,1,0] , [0,0,1,0] ],                             #ㅣ자블럭
 [ [0,0,0,0] , [1,1,0,0] , [0,1,1,0] , [0,0,0,0] ],                             #z자블럭
 [ [0,0,0,0], [0,0,1,1] , [0,1,1,0] , [0,0,0,0] ] ]                             #5자블럭


# #스코어
# score = 0

# #시간에 따른 변화

#2차원배열 1값 -> 2로
def newblock(block) :
    for i in range(4) :
        for j in range(4) :
            if block[i][j] == 1 :
                block[i][j] = 2
            else :
                pass
    return block



#회전함수
def spin(blk_ori) :
    blk_spin = [[],[],[],[]]
    for i in range(4) :
        for j in range(4) :
            blk_spin[i].append(blk_ori[j][i])
    for i in range(4) :
        blk_spin[i].reverse()
    return blk_spin

#옆으로 옮기는 함수
#오른쪽
def right(tmp) :
    flag = False
    if tmp == 10:
        flag = True
    return flag

#왼쪽
def left(block_axis) :
    block_axis[1] -= 1
    return block_axis
    

score = 0
#줄 삭제

#레벨

#스크린 툴
#가로세로 최대길이
MAX_Y = 30
MAX_X = 20

bode = [[0 for _ in range(MAX_X)] for _ in range(MAX_Y)]                    #0으로 bode 맵핑
counter = 0                                                                 #프레임 수 조절 변수
block_axis = [2,7]                                                          #블럭이 내려오기 시작하는 좌표


#테두리 = 0 -> 1
bode[0] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]                         
bode[MAX_Y-1] = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
for i in range(MAX_Y) :
    bode[i][0] = 1
    bode[i][MAX_X-1] = 1


def keypress(e) :
    global key
    global block
    key = e.keysym
    if key == 't' :
        block = spin(block)
        
#블럭 랜덤선택  
block = random.choice(blocks)


block_axis[0] = 2                                                           #블럭 시작위치 y좌표 초기화

#단계
easy =0.8
normal = 0.5
hard = 0.2
super_hard=0.08
mode = easy
#동작
a = True
while  True :
    

    time.sleep(0.8)                                                      #time모듈사용 , 프레임 간격 0.0001
    counter+=1
    
    if counter ==1:                                                         
        counter =0                                                          #카운터 초기화
        
        
        block_axis[0]+=1                                                    #블럭 내림 (블럭의 프린팅 시작지점y좌표 + 1)
        
        # if right(block_axis[0]) == True:
        #     block_axis[1] +=1
        # if left() == True :
        #     block_axis[1] -=1
        
        tk = tkinter.Tk()
        tk.bind('t',keypress)
            
        flag = False                                                      #flag변수생성, False일때 걸리지 않음
        for i in range(4):
            for j in range(4):
                if block[i][j] == 1 and bode[block_axis[0] + i][block_axis[1] + j] == 1:    #블럭의 (i,j)가 1이고, 블럭 프린팅의 시작부분 x좌표 + i와 y좌표 + j 가 1이면 (블럭이 걸림)
                    block_axis[0] -=1
                    flag = True                                                             #블럭 걸림
                    break
            if flag == True:                                                                #이중 브레이크(일차for문)
                break
        
        #테스트용
        if block_axis[1] == 8 :
            block=spin(block)
            
            
        if flag == True:                                                                    #블럭이 걸렸다면
            for i in range(4):
                for j in range(4):
                    if block_axis[0] + i < MAX_Y and block_axis[1] + j < MAX_X and block[i][j] == 1:        #블럭배열이 1일때만 맵에 저장, 블럭 시작지점,x,y좌표 스크린 밖으로 나가지 않게
                        # block = newblock(block)                                                             #블럭배열 속 1값들을 2로 바꿈
                        bode[block_axis[0] + i][block_axis[1] + j] = block[i][j]
            block_axis[0] =2                                                                                #블럭 프린팅 시작지점 초기화
            block_axis[1] = 7
            block = random.choice(blocks)                                                                   #블럭 랜덤선택
            flag = False                                                                                    #루프 다시
                        
    
        tmp_blocK_list= [[block_axis[0]+i//4,block_axis[1]+i%4] for i in range(15)]                         #block배열의 좌표를 맵핑한 스크린에 맞춰서 좌표 다시지정
        os.system("cls")                                                                                    #제자리에서 프레임만 넘기게 하는...
        
        #프린팅
        for i in range(MAX_Y) :
            for j in range(MAX_X) :
                if [i,j] in tmp_blocK_list and block[i - block_axis[0]][j - block_axis[1]] == 2:
                    print("■", end="")
                elif [i,j] in tmp_blocK_list and block[i - block_axis[0]][j - block_axis[1]] == 1:
                    print("■", end="")   
                elif bode[i][j] == 1 :
                    print("■", end='')
                elif bode[i][j] == 2 :
                    print("■", end='')
                else :
                    print(" ", end='')
            print()
            
    
    for i in range(1,19) :
        if bode[3][i] == 2 :
            a = False
        else :
            pass
    if a == False :
        print("game over")
        break
    else :
        pass
    
#using laspberry Pi