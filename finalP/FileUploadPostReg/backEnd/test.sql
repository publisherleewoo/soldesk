-- db에 파일을 저장하는 blob이라는 것이 있지만
-- 비권장하는게 db와 통신 시간이 너무 길다


CREATE TABLE dec19_product(
	a_name varchar2(20 char) PRIMARY KEY,
	a_price varchar2(10 char) NOT NULL,   
	p_photo varchar2(100 char) NOT NULL 	--파일저장x, 파일명저장
);										-- 파일명 + 중복처리 -> 파일명은 길어짐						    
	

--TRUNCATE TABLE dec19_product;


SELECT * FROM dec19_product;

	

CREATE TABLE test_dec19(
	a_name varchar2(20 char) PRIMARY KEY,
	a_price varchar2(10 char) NOT NULL,   
	p_photo varchar2(100 char) NOT NULL 	--파일저장x, 파일명저장
);										-- 파일명 + 중복처리 -> 파일명은 길어짐						    
	


