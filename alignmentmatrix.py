s1 = 'AGAGCTATCATG'
s2 = 'ATACCTCTAGCG'
Arr = [[0 for i in range(13)]for i in range(13)]
def convert(string):
    l1 = []
    l1[:0] = string
    return l1
l1 = convert(s1)
l2 = convert(s2)
for k in range(len(l1)):
    for l in range(len(l2)):
        for i in Arr:
            for j in Arr:
                if l1[k] == l2[l]:
                    Arr[i][j] = (Arr[i-1][j-1]) + 2
                else:
                    Arr[i][j] = (Arr[i-1[j-1]]) - 1
print(Arr)





