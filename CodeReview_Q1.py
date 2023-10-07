'''
1번 개인정보 수집 유효기간
'''
def solution(today, terms, privacies):
    answer=[]

    termsdict={term[0]:int(term[2:]) for term in terms}

    # 한 달 28일 기준
    def to_days(date):
        year,month,day=date.split('.')
        return int(year)*12*28 + int(month)*28 + int(day)
    
    today=to_days(today)
    
    for i,privacy in enumerate(privacies):
        if to_days(privacy[:-2]) + (termsdict[privacy[-1]]*28) <= today:
            answer.append(i+1)

    return answer        

'''
    # 오답 : datetime library 사용
    # 한 달을 28일로 계산하지 않음.
    
    today=datetime.strptime(today,'%Y.%m.%d')
    for i,privacy in enumerate(privacies):
        collect_date=datetime.strptime(privacy[:-2],'%Y.%m.%d')
        expired_date=collect_date+relativedelta(months=termsdict[privacy[-1]])
        
        if today_date>=expired_date:
            answer.append(i+1)

    return answer
'''