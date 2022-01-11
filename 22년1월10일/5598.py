# 배열 대조 순차검색 사용 string 모듈에서 ascii메서드 임포트
from string import ascii_uppercase

alphabet_list = list(ascii_uppercase)
password_list = 'D E F G H I J K L M N O P Q R S T U V W X Y Z A B C'.split()

for i in input().upper():
    idx = password_list.index(i)
    print(alphabet_list[idx] ,end='')
    
    
