import sys

# Usage:
# python convert_with_map.py filed.map feature.map input.train

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

def read_map(fname):
    m = {}
    for line in open(fname):
        line = line.split()
        m[line[0]] = int(line[1])
    return m

filed_file = sys.argv[1]
feature_file = sys.argv[2]
train_file = sys.argv[3]

n, data = read_data(train_file)
    
filed = read_map(filed_file)
mapping = read_map(feature_file)

for i in data:
    if len(i[0]) == 3:
        print(i[0][2], end=' ')
    print("0:{:d}:1".format(mapping[i[0][1]]), end=' ')
    for j in i[1]:
        print("{:d}:{:d}:1".format(filed[str(j)], mapping[str(j)]), end = ' ')
    print("")

