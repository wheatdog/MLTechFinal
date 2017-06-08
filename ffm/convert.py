from collections import Counter
import sys

# field: 136 (0 or 1) + 1 (ad_id)
# feature: 136 + ad_ids

def read_data(data_file_name):
    prob_data = []
    cnt = 0
    for line in open(data_file_name):
        line = line.split("|user ",1)

        ad = []
        for i in line[0].split():
            ad += [i]

        user = []
        for i in line[1].split():
            user += [int(i)]

        prob_data += [[ad, user]]
        cnt = cnt + 1

    return cnt, prob_data

n, data = read_data("../train")
    
filed = {}
filed[0] = 0

mapping = {}
for i in data:
    if i[0][1] not in mapping:
        mapping[i[0][1]] = len(mapping)
    for j in i[1]:
        if j not in filed:
            filed[j] = len(filed)
        if j not in mapping:
            mapping[j] = len(mapping)

print("filed:", file=sys.stderr)
for i in filed:
    print(i, filed[i], file=sys.stderr)

print("mapping:", file=sys.stderr)
for i in mapping:
    print(i, mapping[i], file=sys.stderr)

for i in data:
    print(i[0][2], end=' ')
    print("0:{:d}:1".format(mapping[i[0][1]]), end=' ')
    for j in i[1]:
        print("{:d}:{:d}:1".format(filed[j], mapping[j]), end = ' ')
    print("")

