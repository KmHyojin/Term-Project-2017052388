import time
import random
import os
import quizclass
from . import Gamemenu

# 해적 룰렛 함수
def quiz_five():
    print('\n')
    print('빠밤~! 해적룰렛 게임~')
    print('|01||02||03||04||05||06||07||08||09||10|'
          '\n|11||12||13||14||15||16||17||18||19||20|')

    print('해적 룰렛에 총 20개의 구멍이 있습니다. '
          '당신은 총 8개의 공간에 칼을 꽂을 수 있고')
    print('20개의 구멍 중 하나는 폭탄이 설치되어있습니다.')
    print('폭탄을 피해 칼 8개를 꽂으면 성공이며 칼을 꽂을 수 있는 시간은 5초입니다.')
    time.sleep(5)
    print('그럼 시작.')
    time.sleep(1)

    bomb = random.randint(1, 20) # 폭탄 설치 번호
    c = 0  # 맞춘 횟수

    for i in range(1, 9):
        start = time.time()  # 시작 시간
        answer = input('몇 번째에 칼을 꽂으시나요? ') # 사용자 답
        end = time.time()  # 종료 시간
        t = end - start  # 소요 시간

        if int(answer) != bomb and int(answer) <= 20 and t <= 5:
            print('통과!')
            c += 1 # 점수 증가

        elif int(answer) == bomb:
            print('펑~!')
            print('아쉽지만 폭탄이 터졌네요.. 다음에 다시 시도해주세요^^')
            time.sleep(2)
            os.system('cls')
            Gamemenu.game_menu(-1)

        elif t > 5:
            print('시간 초과입니다. 다음에 다시 시도해주세요^^ ')
            time.sleep(2)
            os.system('cls')
            Gamemenu.game_menu(-1)

        elif int(answer) > 20:
            print('잘못 입력하셨습니다.')

            start = time.time()  # 시작 시간
            answer = input('몇 번째에 칼을 꽂으시나요?')
            end = time.time()  # 종료 시간
            t = end - start  # 소요 시간

            if int(answer) != bomb and int(answer) <= 20 and t <= 5:
                print('통과!')
                c += 1 # 점수 증가

            elif int(answer) == bomb:
                print('펑~!')
                print('아쉽지만 폭탄이 터졌네요.. 다음에 다시 시도해주세요^^')
                time.sleep(2)
                os.system('cls')
                Gamemenu.game_menu(-1)

            elif t > 5:
                print('시간 초과입니다. 다음에 다시 시도해주세요^^ ')
                time.sleep(2)
                os.system('cls')
                Gamemenu.game_menu(-1)

    if c == 8:
        print('\n')
        print('해적룰렛 통과~! 1성구를 획득하셨습니다.')
        score_roulette = quizclass.Quiz()
        score_roulette.score() # 스코어 누적
        time.sleep(2)
        os.system('cls')
        Gamemenu.game_menu(0)
