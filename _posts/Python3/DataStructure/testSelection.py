def selection_sort(a):
    for i in range(0, len(a)-1):
        minimum = i
        for j in range(i, len(a)):
            if a[minimum] > a[j]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]

a = [54, 88, 77,23,52,12,6,53,234,56,342,43,94]
print(a)
selection_sort(a)
print(a)
