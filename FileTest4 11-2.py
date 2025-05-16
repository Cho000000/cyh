inFp = None
inList, inStr = [],""
count = 1

inFp = open("C:\\Users\\yongh\\OneDrive\\바탕 화면\\python\\FileTest\\text1.txt", "r", encoding='UTF8')

inList = inFp.readlines()
for inStr in inList:
    print(f"{count} : {inStr}", end="")
    count +=1
    
inFp.close()