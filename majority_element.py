def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    a.sort()
    if right % 2 == 0:
        major = n // 2 + 1
    if right % 2 != 0:
        major = (n + 1) // 2
    for i in range((n // 2) + (n % 2)):
        if a[i] == a[i + major - 1]:
            return 1
    return -1
n = int(input())
a = list(map(int, input().split()))
if get_majority_element(a, 0, n) != -1:
    print(1)
else:
    print(0)