## 남이 작업한거 잘 갖다쓰자
## -> 이름 중복 -> package로 해결
## -> package명까지 중복되면 -> 망
## -> package명은 세계적으로 중복 안되게지어야
## 자바 : com.회사명.프로젝트명.주제
#
## python : 하이브리드한 객체지향언어
##  package(필수x) > module(.py) > class(객체지향 하기싫으면 없어도)
#
## vscode에서 package만들려면 폴더 만들고
## 그 폴더 안에 __init__.py파일 만들기
## 외부파일에 있는거 가져오려면 필수
#
## import 패키지명.모듈명
## import 폴더이름.파일명

## 1st) animal이라는 폴더안에, __init__.py 파일명, pet.py파일명(내부에 class Dog)
## import animal.pet
# d = animal.pet.Dog("후추")
# d.bark()
# d.printInfo()

## 2st)
## import 패키지명.모듈명 as 별칭
# import animal.pet as ap
# d = ap.Dog("후추")
# d.bark()
# d.printInfo()

## 3st)
## from 패키지명.모듈명 import 가져올거
# from animal.pet import Dog
# Dog("후추").bark()

# 주로 3번쓰겠지만 1,2 활용해야
# Window에서 PYTHONPATH를 설정하면 프로젝트도 패키지처럼 인식
# 1) 실제 Linux서버에서 실행(on-premises)
# 2) MS에서 빌려온 Linux서버에서 실행(cloud(azure))