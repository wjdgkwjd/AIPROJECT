with open('data/text1.txt', 'a', encoding='utf-8') as f:#a=추가
    f.write("3.안녕하세요.\n")
    f.write("4.안녕하세요.\n")


text_list=[ "5.반갑습니다.\n", "6.반갑습니다.\n"]#배열로 추가

with open('data/text1.txt', 'a', encoding='utf-8') as f:
     f.writelines(text_list)


print( "완료!")