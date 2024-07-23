import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
# 카카오톡 내용 정제
# ㅋ : ? , ㅎ : ?, ㅠ : ?, ? : ? , ! : ? => pie차트로 나타내기
c = {'ㅋ' : 0, 'ㅎ' : 0, 'ㅠ' : 0, '?' : 0, '!' : 0}
result =""
with open("C:/Users/sdedu/Desktop/data/kakao.txt","r",encoding="UTF-8") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        line = line.split(" ")
        
        result =''.join(line[7:])
        print(result)
        
        if result.find("ㅋ") != -1:
            c["ㅋ"]+=1
        if result.find("ㅎ") != -1:
            c["ㅎ"]+=1
        if result.find("ㅠ") != -1:
            c["ㅠ"]+=1
        if result.find("?") != -1:
            c["?"]+=1
        if result.find("!") != -1:
            c["!"]+=1

print('---------')
print(f"ㅋ : {c['ㅋ']} 번")
print(f"ㅎ : {c['ㅎ']} 번")
print(f"ㅠ : {c['ㅠ']} 번")
print(f"? : {c['?']} 번")
print(f"! : {c['!']} 번")

clist = [f'ㅋ : {c["ㅋ"]}',f'ㅎ: {c["ㅎ"]}',f'ㅠ: {c["ㅠ"]}',f'?: {c["?"]}',f'!: {c["!"]}']
cntlist = [c['ㅋ'], c['ㅎ'],c['ㅠ'], c['?'],c['!']]
# clist = []
# cntlist = []
# for k,v in c.items():
    # clist.append(k)
    # cntlist.append(v)

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=50).get_name()
plt.rc('font',family = fontName)

c = ['#BBDDCC', '#B2CCFF', '#FFA7A7', '#E5DDFF', '#DDFFFF']
w = {'width' : 0.8, 'edgecolor' : 'black', 'linewidth' : 3}
plt.pie(cntlist,labels=clist, colors = c, autopct = "%.2f%%",wedgeprops=w,explode=(0.05,0.05,0.05,0.05,0.05)) # wedgeprops : 테두리
plt.title('단어 조회')
plt.show()

f.close()