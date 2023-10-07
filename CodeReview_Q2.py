'''
2번 이모티콘 할인행사
'''
from itertools import product

def solution(users, emoticons):
    answer = []

    discountR=[40,30,20,10]

    # 이모티콘 모든 할인 조합
    combs=product(discountR,repeat=len(emoticons))

    for comb in combs:
        per_comb=[0,0]
        for user in users:
            paid=0
            for i,r in enumerate(comb):
                if user[0]<=r:
                    paid+=int((100-r)*0.01*emoticons[i])
            if paid>=user[1]:
                per_comb[0]+=1
            else:
                per_comb[1]+=paid
        answer.append(per_comb)
    
    answer.sort(key=lambda x: (x[0],x[1]))

    return answer[-1]