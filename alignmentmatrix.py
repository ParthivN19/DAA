s1 = 'AGAGCTATCATG'
s2 = 'ATACCTCTAGCG'
arr = [[0 for i in range(13)]for i in range(13)]
for i in range(1,len(arr)):
    for j in range(1,len(arr[0])):
		if s1[i]==s2[j]:
			arr[i][j]=arr[i-1][j-1]+2
		else:
			arr[i][j]=max([ arr[i-1][j], arr[i-1][j-1], arr[i][j-1] ]) - 1
            
print(arr)

            
            






