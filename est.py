with open("lenght.txt") as f:
    lenght_whole=f.read().split("\n")
for i in range(len(lenght_whole)):
    lenght_whole[i] = float(lenght_whole[i])
length_average = sum(lenght_whole)/len(lenght_whole)
print("length ",length_average)

with open("pep.txt") as f:
    perpl_whole=f.read().split("\n")
for i in range(len(perpl_whole)):
    perpl_whole[i] = float(perpl_whole[i])
perpl_average = sum(perpl_whole)/len(perpl_whole)
print("perpl ",perpl_average)

with open("burst.txt") as f:
    burst_whole=f.read().split("\n")
for i in range(len(burst_whole)):
    burst_whole[i] = float(burst_whole[i])
burst_average = sum(burst_whole)/len(burst_whole)
print("burst ",burst_average)

with open("read.txt") as f:
    read_whole=f.read().split("\n")
for i in range(len(read_whole)):
    read_whole[i] = float(read_whole[i])
read_average = sum(read_whole)/len(read_whole)
print("read ",read_average)

