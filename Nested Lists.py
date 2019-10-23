if __name__ == '__main__':
    name=[]
    score=[]
    lis3=[]
    for i in range(int(input())):
        name.append(input())
        score.append(eval(input()))
        score2=set(score)
        score2=list(score2)
        score2=sorted(score2)
    ctr=0
    lis2=[]   

    for i in score:
        
        if i == score2[1]:
            lis2.append(ctr)
        ctr+=1
    ctr=0

    for i in name :
        if ctr in lis2:
            lis3.append(i)
        ctr+=1
    lis3=sorted(lis3)
    for i in lis3:
        print(i)
    

