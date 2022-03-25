def solution(number, k):
    answer = []
    
    for num in number:
        if not answer:
            answer.append(num)
            continue
            
        if k > 0:
            while answer[-1] < num:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(num)
    
    if k > 0:
        for i in range(k):
            answer.pop()
            
    print(answer)

    return ''.join(answer)
    