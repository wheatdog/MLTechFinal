import sys

# Usage:
# python convert.py filed.map feature.map input.train

# If using all data,
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

def print_map(m, fname):
    f = open(fname, 'w')
    for i in m:
        print(i, m[i], file=f)
    f.close()

filed_file = sys.argv[1]
feature_file = sys.argv[2]
train_file = sys.argv[3]

n, data = read_data(train_file)
    
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

print_map(filed, filed_file)
print_map(mapping, feature_file)

for i in data:
    print(i[0][2], end=' ')
    print("0:{:d}:1".format(mapping[i[0][1]]), end=' ')
    for j in i[1]:
        print("{:d}:{:d}:1".format(filed[j], mapping[j]), end = ' ')
    print("")

