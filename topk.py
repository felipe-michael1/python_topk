# Função que traz os números mais frequentes, ou seja os que mais se repetem
def solution(numbers, k):
    hash_map = {}

    for num in numbers:
        if num not in hash_map:
            hash_map[num] = 0
        else:
            hash_map[num] += 1

    pairs = sorted(hash_map.items(), key=lambda x:x[1], reverse=True)
    result = []

    for pair in pairs[:k]:
        result.append(pair[0])
    return result
    
k = 2
numbers = [1,1,1,2,2,3,4,5,6,9,10,11]
result = solution(numbers,k)
print(result)
