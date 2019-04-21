def solution(prices):
    answer =[]
    for i in range(len(prices)):
        a=0
        for j in range(i+1,len(prices)):
            a+=1
            if prices[i] > prices[j]:
                break
        answer.append(a)
    return answer
    
