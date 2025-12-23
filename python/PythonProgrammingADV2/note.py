# 프로젝트가 커지면
# C/M/V가 여러개 생기고 -> C도 많아짐
# 프로그램의 진입점 역할을하는 첫 컨트롤러는 보통 homeController or mainController라고함
############
# guest.py : M - 계산(DAO)
# doctor.py : M - 데이터 표현용

# DAO/DTO 패턴 : MVC패턴인데, DB작업
#   MVC패턴
#       DAO(Data Access Object) : DB관련 작업하는 M
#       DTO(Data Transfer/Temp Object) : 데이터를 묶어다니는 M
#           DTO,VO(Value Object), Bean