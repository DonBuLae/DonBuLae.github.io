input = input()

clone = []

for i in range(len(input)):
    clone.append(input[len(input) -i -1])

count = 0
for i in range(len(input)):
    if input[i] == clone[i]:
        count += 1

if count == len(input):
    print(1)
else:
    print(0)