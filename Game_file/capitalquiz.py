import csv
import time
import quizclass

with open('capital.csv', 'r', encoding='utf-8') as csv_file3:
    capital_list = dict(filter(None, csv.reader(csv_file3))) # 문제, 답 딕셔너리

# 수도 퀴즈 함수
def quiz_three():
    print('\n')
    print('빠밤~! 수도 퀴즈입니다.')
    time.sleep(2)
    print('주어지는 나라에 해당하는 수도를 맞춰주세요.')
    time.sleep(2)
    print('문제는 총 8개가 주어지며 답을 입력할 시간은 10초 주어집니다.')
    time.sleep(3)
    print('그럼 시작~!')

    c_contents = []  # 문제 리스트

    for country in capital_list.keys():
        c_contents.append(country)

    question_c = len(c_contents)  # 문제 개수

    contents_capital = quizclass.Quiz()  # 수도문제 클래스 객체
    contents_capital.quiz_content(capital_list, c_contents, question_c) # 수도문제 출력












