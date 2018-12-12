from . import Moviequiz as A_game
from . import three_six_nine as B_game
from . import capitalquiz as C_game
from . import imageQuiz as D_game
from . import roulette as E_game
import quizclass
import os
import sys
import time

total_score = -1 # 스코어 변수

# 게임 메뉴
def game_menu (i):

    f = open('C:/Users/김효진/PycharmProjects/개인프로젝트/phone_number.txt',mode='a', encoding='utf-8')
    global total_score
    score_sum = quizclass.Quiz()
    total_score = total_score + score_sum.score() + i


    if total_score == 5:
        print('축하드립니다. 손오공이 되셨습니다~! 짝짝짝~!')
        p_number = input(' 전화번호를 입력해주시면 추첨을 통해 스타벅스 커피 상품권을 드립니다.'
                         ' 입력하시겠습니까?(Y/N) ')
        if p_number == 'Y':
            p_num = input('입력: ') # 사용자 전화번호
            f.write(p_num)
            f.write('\n')
            f.close()
            print('입력완료~!, 번호는 추첨용도로만 사용 후 폐기됩니다. 감사합니다^^.')
            time.sleep(2)
            print('게임 종료.')
            time.sleep(1.5)
            sys.exit()
        else:
            print('게임 종료.')
            time.sleep(1.5)
            sys.exit()


    time.sleep(0.5)
    print('겜유기를 선택한 당신~! 손오공이 되고 싶지 않습니까?')
    print('아래 5가지게임을 통해 5성구를 얻으면 당신은 손오공이 될 수 있습니다. '
          '현재 스코어(', total_score, '/ 5)')
    print('게임을 선택하세요.')

    game_choice = input("(A) 영화 명대사 퀴즈 (B) 3,6,9 게임 (C) 수도 퀴즈 "
                        "(D) 이미지 퀴즈 (E) 해적 룰렛 ? ") # 게임선택목록

    if game_choice == 'A' or game_choice == 'a' or game_choice == '영화':
        A_game.quiz_one()  # 영화 퀴즈 실행
    elif game_choice == 'B' or game_choice == 'b' or game_choice == '3,6,9':
        B_game.quiz_two()  # 3,6,9 게임 실행
    elif game_choice == 'C' or game_choice == 'c' or game_choice == '수도':
        C_game.quiz_three()  # 수도 퀴즈 실행
    elif game_choice == 'D' or game_choice == 'd' or game_choice == '이미지':
        D_game.quiz_four()  # 이미지 퀴즈 실행
    elif game_choice == 'E' or game_choice == 'e' or game_choice == '해적':
        E_game.quiz_five()  # 해적 룰렛 실행



print("겜유기에 오신 것을 환영합니다")

game_start = input('메뉴로 가시려면 시작을 입력해주세요. : ')
print('\n')

if game_start == '시작':
    time.sleep(1.5)
    os.system('cls')
    game_menu(0)














