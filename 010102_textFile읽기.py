with open('data/text1.txt', 'r', encoding='utf-8') as f:#r->읽기
    text1=f.read()#str 변수

f=open('data/text2.txt', 'r', encoding='utf-8')
text2=f.read()

with open('data/text1.txt', 'r', encoding='utf-8') as f:#추천 방법
   lines = f.readlines()#리스트 변수,url 리스트로 저장

print("="*100)
print( text1)
print("-"*100)
print( text2)
print("-"*100)
print( lines)
print("="*100)
