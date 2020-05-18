def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]

a = [54, 88, 77, 23, 52, 12, 6, 53, 234, 56, 342, 43, 94]
print(a)
insertion_sort(a)
print(a)


