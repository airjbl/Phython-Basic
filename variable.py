# 변수(variable)
# 변수(variable)=값
# 위 형식으로 변수(variable)에 값을저장
# = 기호의 뜻과 다르게 단순학[ 값이 변수(variable)에 저장됨
# 변수(variable) 는 아래의 규칙을 지키면 원하는 대로 가능
# 1. 숫자 롯 시작 불가능
# 2. 기호 "_" 를 제외한 특수문자 불가능
# 3. 띄어쓰기 불가능
# 4. 예약어 불가능


# my_name = "Jebin"


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# 자료형(Data type)     
# str   -> String   문자 => 따음표로 이루어져 있음 (따음표가 있으면 무조건) " " ' '    
# float -> float    실수 => 따음표가 없고 소수점이 있으면 실수
# int   -> Integer  정수 => 따음표가 없고 소수점도 없으면 정수
#- 일상적으로 사용하는 말들(영어, 중국어, 한국어)이 따음표가 없다 => 오류

# a = 10 # a라는 변수에 int 자료형인 10 저장
# b = 'cit' # b라는 변수에 str 자료형인 'cit' 저장


# name = '파이썬'
# age = 20
# height = 178

# print(name)

# name ='파이리'
# print(name)


# name ='파이팅'
# print=(name)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# print('문자' or 변수 or 숫자)
# print('문지' or 변수 or 숫자) 함수는 괄호안에 있는 '문자', 숫자 또는  변수의 값을 출력한 후 엔터한다.
# 한줄에 여러개를 출력하고 싶으면 콤마(,)를 사용
# 만약 print()를 사용할 경우 빈 한줄이 출력

# name = '파이썬'
# age = 28
# height = 188
# print(name)
# print()   # 빈 한줄 출력
# print(age)
# print(height)
# print('hi')
# print()
# print(5)
# print(5*10)
# print(name, age, height, "hello")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# 자료형을 확인하는 방법
# type()=> 괄호안에 있는 변수 또는 값의 자료형을 가지고 옴
# type(변수) <=이렇게 사용하는 경우 프로그램으로 동작은 하지만 자료형을 눈으로 볼수없음
# print(type(변수))    <=command
# 위 형식으로 print() 안에 넣어서 주로 사용

# int0=1
# float0=3.14
# str0='test'
# type(int0)
# print(type(int0))   #int0라는 변수에 int  자료형인 1 저장
# print(type(float0))  # 동작을 하지만 자료형은 눈으로 볼 수 없음
# print(type(str0))    #type()을 사용하여 int0의 자료형 출력



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# 형 변환(casting)
# str (변수or값)=> 변수or 값을 str 자료형으로 변환
# float(변수or값)=> 변수 or 값을 float 자료형으로 변환
# int(변수or값)=>변수 or 값을 int 자료형으로 변환
# 단순히 연산할때만 사용하면 원본의 값은 변하지 않음
# 원본에 자료형을 변환 시키기 위해서는 변수에값을 다시 넣어야함 [ex. a = int(a)]

# var1=2
# var2='31'
# result=var1+int(var2)       # result 변수에 var1 변수 + int 자료형을 변환한 var2변수 저장
# print(result)               # 실제 변수의 자료형은 변환 안됨
# print(type(var2))           # var2 변수에 int 자료형으로 변환한 var2변수 저장
# var2=int(var2)              # 변수 var2 자료형을 출력
# print(type(var2))



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# input('문자' or 변수)
# '문자' 또는 변수를 출력한 후 엔터키 누르기 전까지 키보드 입력을 밭음
#'문자' 또는 변수는 생략가능 
# 변수=input('문자or변수)
#위 형식을 주로 사용, input()만 사용했을 경우 입력 값을 저장하지 못함
#input()은 무조건 str 자료형으로 값을 저장함

# var1=2
# var2=input("insert anything: ")
# print(var2)
# print(type(var2))

# var2=int(var2)
# print(type(var2))

# sum=var1+var2
# print(sum)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# print("안녕하세요, 이름을 입력해주세요.")
# name=input()

# print("환영합니다", name," 님 나이를입력해주세요.")    # ,=YOU NEED THIS COMMA TO PUT THE NAME 
# age=input()                                            # input() is always 문자 so convert it to 숫자 by using int() and chnage it by put a=in(a)
# age=int(age)                                        # always put name 
# year=2024-age                                                 # 콤마 무조건 사용하기, 문자와숫자를혼합 "  " 를 같이씀
                                                  

# print(year,"년에 태어나셧네요!키를 입력해주세요.")   
# height=int(input())               #or you can use height=int(input())
# total=200-height

# print("2m까지",total,"cm 남았네요.")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


# + 더하기
# - 빼기
# * 곱하기
# / 나누기
# // 몫(정수로 나옴 for example 10/2=5.0 and you only get the result no 나머지)
# % 나머지(only 나머지)
# ** 제곱

# a=10
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#



