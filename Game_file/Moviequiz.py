import csv
import time
import quizclass

with open('quiz.csv', 'r', encoding='utf-8') as csv_file1:
    movie_list = dict(filter(None, csv.reader(csv_file1))) # 문제, 답 딕셔너리

# 영화 명대사 퀴즈 함수
def quiz_one():
    print('\n')
    print('빠밤~! 영화 명대사 퀴즈입니다.')
    time.sleep(2)
    print('주어진 영화 명대사 질문에 영화제목을 맞춰주시면 됩니다.')
    time.sleep(2)
    print('문제는 총 8개가 주어지며 답을 입력할 시간은 10초 주어집니다.')
    time.sleep(3)
    print('그럼 시작~!')

    m_contents = []  # 문제 리스트

    for m in movie_list.keys():
        m_contents.append(m)

    question_c = len(m_contents) # 문제 개수

    contents_movie = quizclass.Quiz()  # 영화문제 클래스 객체
    contents_movie.quiz_content(movie_list, m_contents, question_c) # 영화문제 출력









