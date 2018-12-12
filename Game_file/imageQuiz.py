import csv
import random
import time
import os
import quizclass
from . import Gamemenu
from PIL import Image

with open('imagequiz.csv', 'r', encoding='utf-8') as csv_file5:
    photo_list = dict(filter(None, csv.reader(csv_file5))) # 문제, 답 딕셔너리

# 이미지 퀴즈 함수
def quiz_four():
    print('\n')
    print('빠밤~! 이미지 퀴즈입니다.')
    time.sleep(2)
    print('주어진 이미지에 해당하는 인물을 입력해주시면 됩니다.')
    time.sleep(2)
    print('문제는 총 8개가 주어지며 답을 입력할 시간은 5초 주어집니다.')
    time.sleep(3)
    print('이미지 확인 후 오른쪽 상단에 \'ㅡ\' or \'X\' 버튼을 누르시고 답을 입력하세요.')
    time.sleep(2)
    print('그럼 시작~!')

    p_contents = []  # 문제 리스트
    c = 0 # 맞춘 횟수

    for p in photo_list.keys():
        p_contents.append(p)

    del p_contents[0] # data 분류 값 삭제
    question_c = len(p_contents) # 문제 개수

    number = random.sample(range(0, question_c), question_c) # 문제 랜덤을 위한 랜덤 변수

    for i in range(1, 9):
        print(i,'번째 문제')
        img = Image.open(p_contents[number[i]]) # 문제 이미지 변수
        img.show() # 이미지 출력
        start = time.time() # 시작 시간
        answer = input('입력: ') # 사용자 답
        end = time.time() # 종료 시간
        t = end - start # 소요 시간

        if t <= 5 and answer == photo_list[p_contents[number[i]]]:
            print('통과~!')
            c += 1 # 점수 증가
            img.close()

        elif answer != photo_list[p_contents[number[i]]]:
            img.close()
            print('땡! 아쉽지만 다음에 다시 시도해주세요^^')
            time.sleep(2)
            os.system('cls')
            Gamemenu.game_menu(-1)

        elif t > 5:
            img.close()
            print('시간초과 입니다.! 아쉽지만 다음에 다시 시도해주세요^^')
            time.sleep(2)
            os.system('cls')
            Gamemenu.game_menu(-1)

        print('\n')

    if c == 8:
        print('이미지 퀴즈 통과~! 1성구를 획득하셨습니다.')
        score_image = quizclass.Quiz()
        score_image.score()
        time.sleep(2)
        os.system('cls')
        Gamemenu.game_menu(0)




