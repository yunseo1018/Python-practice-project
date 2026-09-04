# 정수형
print(-15)
print(15)

#실수형
print(3.14)
print(-2.5)

# 문자열
print("z"*9)
print("hello python")

#불린형
print(True)
print(False)
print(5>3)
print(not 5>3)

# 애완동물을 소개해 주세요~!
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "입니다.")
hobby = "공놀이"

# "+"를 이용한 문자열 연결
print(name + "는 " + str(age) + "살입니다.")

#  ","를 이용한 문자열 연결 띄어쓰기 차이
print(name, "는 ", str(age), "살입니다.")
print(name + "는 " + hobby + "을 좋아합니다.")
print(name + "는 성년입니까? " + str(is_adult))