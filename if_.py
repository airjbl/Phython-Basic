# 비교 연산자
# 비교 연산의 결과는 무조건 true or false로 나옴
# == :같다, 같으면 true, 다르면 false
# != : 다르다, 같으면 false, 다르면 true
# <
# >
# <= 작거나 같다
# >=  크거나 같다

# print(5 != 2) # true
# print(5<2) # false
# print(5+2<8)  # true
# print( 4 != 4) # false


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# 조건식 종류

# [가장 일반적인 형식]
# if(조건식) :
#      if의 조건식이 true일 경우 실행할 코드
# elif(조건식) :
#      elif의 조건식이 true일 경우 실행할 코드
#else(조건식) :
#       위의 모든 조건식이 False일 경우 실행할 코드


#[if만 사용할경우]
#if(조건식) :
#      if의 조건식이 true일 경우 실행할 코드


#[if랑 elif만 사용한경우]
#if(조건식)
#      if의 조건식이 true일 경우 실행할 코드
# elif(조건식) :
#      elif의 조건식이 true일 경우 실행할 코드

#[if랑 else만 사용한경우]
#if(조건식) :
#      if의 조건식이 true일 경우 실행할 코드
#else(조건식) :
#       위의 모든 조건식이 False일 경우 실행할 코드


#위 형식들의 조건식이 있으며
#if는 무조건 1개,
#elif는 0개 부터 무한대,
#else는 0개 또는 1개를 사용하여 조건문을 구성할 수 있음
#조건문은 조건문 안에 중첩해서 사용할수 있다.


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# score는 숫자로 입력받기
# 100~90 : A
# 89~70  : B
# 69~60  : C
# 59~0   : D
# 조건식으로 표현해보자

# score=int(input())          #숫자로 입력받음
# if(100>= score >=90):
#     print("A")              #조건문이 true여서 실행될 경우 아래의 조건은 더보지 않고 if 종료,즉 조건문은 한개만 등장함
# elif(89>= score >= 70):
#     print("B")
# elif(69>= score >= 60):
#     print("C")
# elif(59>= score >= 0):
#     print("D")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# print("나이가 12세 이상만 영화관람이 가능합니다.")
# var2=input("나이를 입력해주세요. ")               #always remember you can't put input next to print 
#                                                 #so if you want user to write something NEXT to the question write the questioon inside the inpput command.
# age=int(var2)
# if(age >= 12):
#      print("즐거운 관람되세요")
# elif(0 < age < 12):
#      print("죄송합니다")
# elif(age <=0 ):
#      print("잘못입력했습니다")

#쌤 코드
# print("나이가 12세 이상만 영화관람이 가능합니다.")
# age=int(input("나이를 입력해주세요. "))

# if(age>=12):
#   print('즐거운 관람되세요.')
# else:
#   print('죄송합니다.')


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#



# print("수를 입력해주세요.")
# number = int(input())

# if(number % 2==0) :                 #must remember to PUT "==" instead of "=" so like this 10/2==5
#     print("짝수입니다")
# else:
#     print("홀수입니다")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# not       : True면 false, False면 True로 결과를뒤집음
# and       : 양옆이 전부 True면 True 하나라도 false면 False
# or        : 양옆이 전부 false면 false 하나라도 True면 true
# 실행순서는 not, and, or 순서로 실행 됨

# a = 10
# b = 2
# if((a == 10) and (b == 2)):
#     print("a는10, b는 2입니다")

# if((a == 10) or (b == 2)):
#     print("a와 b 둘중 한개 이상은 10입니다")

# if(not(a == 5)):            #(a != 5) 와 같음)
#     print("a는 5가 아닙니다")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


#중첩 if
# if의 경우 중첩해서 사용가능

# age=int(input("나이를 입력하세요:"))
# is_member = input("회원 여부를 입력하세요(yes 또는 no): " )

# if(age >= 18):
#     print("회원님 안녕하세요")

#     if(is_member == "yes"):
#         print("성인 회원님, 환영합니다!")
#     else:
#         print("성인 비회원님, 회원가입을 해주세요.") 
# else:   
#     if(is_member == "yes"):
#         print("청소년 회원님 환영합니다!")
#     else:
#         print("청소년 비회원님, 회원가입을 해주세요.")
