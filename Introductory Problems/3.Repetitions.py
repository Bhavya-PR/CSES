seq = input()
#seq = "ATTCGGGA"
count = 1
max = 1
for i in range(len(seq) - 1):
    if seq[i] == seq[i+1]:
        count += 1
        if count > max:
            max = count
    else:
        count = 1
print(max)