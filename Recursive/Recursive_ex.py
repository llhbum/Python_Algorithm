# 피보나치
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# 팩토리얼
def factorial(n):
    if n <= 1 :
        return n
    else:
        return  n * factorial(n-1)

#최대공약수
def gcd(p,q):
    if (q == 0):
        return p
    else:
        return gcd(q,p%q)

#문자열 길이 계산
def length(str):
    if str == "":
        return 0
    else:
        # print(str)
        return 1 + length(str[1:])

# 순차 탐색 암시적 매개변수
def search(list, n, target):
    if n<=0:
        return -1;
    elif target == list[n-1]:
        return f'Index : {n-1}'
    else: return search(list,n-1,target)

# 순차탐색 명시적 매개변수로 바꿔서 표현
def search2(list, begin, end, target):
    if begin>end:
        return -1
    elif target == list[begin]:
        return f'Index : {begin}'
    else:
        return search2(list, begin+1, end, target)


#최대값 찾기
def findMax(n, list):
    if n == 0:
        return list[0]
    else:
        return max(list[n-1],findMax(n-1,list))

# 이진탐색 Recursion
def binarySearch(list, target, begin, end):
    if begin > end:
        return -1
    else:
        middle = end + begin // 2
        if list[middle] == target:
            return f'Index : {middle-1}'
        elif list[middle] > target:
            return binarySearch(list,target,begin,middle-1)
        else:
            return binarySearch(list,target,middle+1,end)


if __name__ == '__main__':
    # 피보나치
    print(fibo(3))
    # 2

    # 팩토리얼
    print(factorial(4))
    # 24

    # 최대공약수
    print(gcd(55,30))
    # 5

    # 문자열 길이 계산
    print(length('ace'))
    # 3

    # 순차 탐색 암시적 매개변수
    list = [1,2,3,4,5]
    print(search(list,5,3))
    # Index : 2

    # 순차탐색 명시적 매개변수로 바꿔서 표현
    list = [1,2,3,4,5]
    print(search2(list,0,5,3))
    # Index : 2

    # 최대값 찾기
    list = [7,6,3,4,5,9]
    print(findMax(6,list))
    # 9

    # 이진탐색 Recursion
    list = [7,6,3,4,5,9,10,2,15,16,7,3]
    #이진탐색은 데이터의 크기가 정렬되었다는 가정하에 접근이 가능함
    list.sort()
    # [2, 3, 3, 4, 5, 6, 7, 7, 9, 10, 15, 16]
    print(binarySearch(list,10,0,10))
    # Index : 8


