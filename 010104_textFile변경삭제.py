with open('data/text1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()#배열로 저장

new_lines=[]
for line in lines:
  if line.strip() != "2.안녕하세요.":#strip 앞뒤 공백, 특수문자 제거
     line=line.replace("반갑습니다.","hello.")#replace 바꾸기
     new_lines.append( line)


with open('data/text1.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)


print( "완료!")