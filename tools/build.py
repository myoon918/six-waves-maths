# 아티팩트용 index.html(골격 없음)을 공개용 완전한 HTML 문서로 만든다. 사용: python3 tools/build.py <아티팩트 파일> <출력 파일>
import sys
src,dst=sys.argv[1],sys.argv[2]
s=open(src).read()
s=s.replace('<span class="draft">DRAFT</span>\n','')
s=s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
head='<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="description" content="Six Waves Maths · Sydney. One lesson a week, six days of follow-up. Daily iPad homework, every missed question back after 1, 3 and 7 days.">\n'
doc=head+s
i=doc.index('<header>'); doc=doc[:i]+'</head>\n<body>\n'+doc[i:]+'\n</body>\n</html>\n'
doc=doc.replace('<style>\n/* 레이아웃','<style>\nhtml{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}\n/* 레이아웃',1)
open(dst,'w').write(doc)
print('built',len(doc))
