inFp = None
inStr = ""
count = 1

inFp = open("C:\\Users\\yongh\\OneDrive\\바탕 화면\\python\\FileTest\\text1.txt","r", encoding='UTF8')

while True:
    inStr = inFp.readline()
    if inStr =="":
        break
    print("%d : %s" % (count, inStr), end="")
    count +=1
    
inFp.close()