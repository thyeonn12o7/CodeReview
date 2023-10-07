'''
3번 택배 배달과 수거하기
'''
def solution(cap, n, deliveries, pickups):

    deliveries=deliveries[::-1]
    pickups=pickups[::-1]
    distances=0
    
    delivery=0
    pickup=0
    
    for i in range(n):
        delivery+=deliveries[i]
        pickup+=pickups[i]

        while (delivery>0) or (pickup>0):
            delivery-=cap
            pickup-=cap

            distances+=(n-i)*2

    return distances

'''
# 오답

# 재귀함수를 생각했지만
# 구현하는 과정에서 완성하지 못함.

def getDistance(deliveries,cap):
    if deliveries[-1]==0:
        deliveries.pop()
        getDistance(deliveries,cap)
    elif deliveries[-1]<=cap:
        cap-=deliveries[-1]
        distance+=len(deliveries)
        deliveries.pop()
        # ...
    else:
        deliveries[-1]-=cap
        distance+=len(deliveries)
        getDistance(deliveries,cap)

    return distance
'''