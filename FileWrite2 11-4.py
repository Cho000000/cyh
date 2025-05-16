inFp, outFp = None, None
inStr = ""
inFileName, outFileName = "", ""

inFileName = input("소스 파일명을 입력하세요 : ")
outFileName = input("타깃 파일명을 입력하세요 : ")

inFp = open(inFileName, "r")
outFp = open(outFileName, "w", encoding='UTF8') # 타깃 파일은 UTF-8로 저장하는 것을 권장

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

print(f"---{inFileName} 파일이 {outFileName} 파일로 복사되었음---")



inFp.close()
outFp.close()