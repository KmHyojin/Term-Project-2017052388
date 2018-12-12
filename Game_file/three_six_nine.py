import time
import random
import quizclass

# 3,6,9 게임 함수
def quiz_two() :
    print('\n')
    print('빠밤~! 3,6,9 게임입니다.')
    time.sleep(2)
    print('시작 순서는 랜덤이며 3, 6, 9가 들어간 순번에는 a를 입력해주시고')
    time.sleep(3)
    print('그 외는 해당하는 숫자를 입력해주시면 됩니다.')
    time.sleep(2)
    print('숫자는 30까지 주어지며 답을 입력할 시간은 3초 주어집니다.')
    time.sleep(2)
    print('그럼 시작~!')

    n_list = [3, 6, 9, 13, 16, 19, 23, 26, 29, 30]  # 입력하면 안되는 값 리스트
    check_1 = [5, 15, 25, 29]
    check_2 = [3, 9, 13, 19, 23 ,29]

    computer = random.randint(1, 10)  # 시작 랜덤
    user = random.randint(1, 10)  # 시작 랜덤

    if computer > user:
        for number in range(1, 31, 2):
            if number not in n_list:
                print('컴퓨터:', number)
            else:
                print('컴퓨터: a ')

            answer_chk = quizclass.Quiz()
            answer_chk.answer_check(number, n_list, check_1)

    else:
        for number in range(1, 31, 2):

            answer_chk = quizclass.Quiz()
            answer_chk.answer_check(number, n_list, check_2)

            if number in check_1:
                print('컴퓨터: a')
            else:
                print('컴퓨터: ', number + 1)









