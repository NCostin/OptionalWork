n1 = int(input('Specify the start of the array: '))
n2 = int(input('Specify the end of the array: '))
x = int(input('Specify the searched value: '))

answer = "NOT-FOUND"

A=list(range(n1,n2))

for i in A:
    if (i == x):
        answer = A.index(i)
        print(A)
        print(f'The index is:{answer}')
        break
    else:
        print(answer)