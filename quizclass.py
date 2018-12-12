import time
import random
import os
import Game_file.Gamemenu as menu

# 영화 명대사 퀴즈 및 3,6,9 게임 클래스
class Global(object):
    s = 0  # 맞춘 횟수

class Quiz:
    def quiz_content(self, list, c, quest_c):

        number = random.sample(range(0, quest_c), quest_c)  # 문제 랜덤을 위한 랜덤 변수
        ok = 0 # 맞춘 횟수

        for i in range(1, 9):
            print('문제', i, ': ', c[number[i]])  # 문제 출제
            start = time.time()  # 시작 시간
            answer = input('입력: ')  # 사용자 답
            end = time.time()  # 종료 시간
            t = end - start  # 소요 시간

            if t <= 10 and list[c[number[i]]] == answer:
                print('정답입니다.')
                ok += 1 # 점수 증가

            elif t > 10:
                print('시간초과 입니다.! 아쉽지만 다음에 다시 시도해주세요^^')
                time.sleep(2)
                os.system('cls')
                menu.game_menu(-1)

            elif list[c[number[i]]] != answer:
                print('땡! 아쉽지만 다음에 다시 시도해주세요^^')
                time.sleep(2)
                os.system('cls')
                menu.game_menu(-1)

            print('\n')

        if ok == 8:
            print('게임 통과~!, 1성구를 획득 하셨습니다.')
            self.score() # 스코어 누적
            time.sleep(2)
            os.system('cls')
            menu.game_menu(0)

    # 3,6,9 게임 함수
    Global.s = 0 # 맞춘 횟수
    def answer_check(self, num, list1, list2):
        start = time.time()  # 시작 시간
        answer = input('사용자: ')  # 사용자 입력

        Global.s += 2 # 점수 증가

        end = time.time()  # 종료 시간
        t = end - start  # 소요 시간

        if answer in list1:
            print('땡! 아쉽지만 다음에 다시 시도해주세요^^')
            Global.s = 0
            time.sleep(2)
            os.system('cls')
            menu.game_menu(-1)

        elif (num not in list2) and (answer == 'a'):
            print('땡! 아쉽지만 다음에 다시 시도해주세요^^')
            Global.s = 0
            time.sleep(2)
            os.system('cls')
            menu.game_menu(-1)

        elif t > 3:
            print('시간 초과입니다. 다음에 다시 시도해주세요^^ ')
            Global.s = 0
            time.sleep(2)
            os.system('cls')
            menu.game_menu(-1)

        if Global.s == 30:
            print('\n')
            print('게임 통과~!, 1성구를 획득 하셨습니다.')
            self.score() # 스코어 누적
            time.sleep(2)
            os.system('cls')
            menu.game_menu(0)

    # 누적 스코어 함수
    ball = 0
    def score(self):
        global ball
        self.ball = 1
        return self.ball






