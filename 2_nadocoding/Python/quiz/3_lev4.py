rows = ["A","B","C"]

for row in rows:
    for i in range(1,21):
        if i %2 == 1:
            print(row+str(i), end=" ")


for i in range(1,21)[::2]:
    print("A"+str(i), end=" ")