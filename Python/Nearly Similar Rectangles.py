def nealy(sides):
    Long_INETGER=0
    for i in range(0,len(sides)-1):
        x=sides[i]
        for j in range(i+1, len(sides)):
            y=sides[j]
            if x[0]/y[0]==x[1]/y[1]:
                Long_INETGER+=1
    return Long_INETGER

nealy([[4,8],[15,30],[25,30]])