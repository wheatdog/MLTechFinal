from collections import Counter

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

def scan(data_file_name):
    n, data = read_data(data_file_name)
    ads = [{}, {}]
    max_dim = 0
    for i in data:
        for j in range(2):
            if i[0][j] in ads:
                ads[j][i[0][j]] = ads[j][i[0][j]] + 1
            else:
                ads[j][i[0][j]] = 1

        for j in i[1]:
            if j > max_dim:
                max_dim = j
    print(data_file_name, n, max_dim, len(ads[0]), len(ads[1]))
    return [data_file_name, n, max_dim, ads]

print("[Filename] [Number of data] [Largest User Feature Dim] [Number of timestamp] [Number of ad id]")

data = []

data += [scan("release1/test_half_10")]
data += [scan("release1/test_half_11")]
data += [scan("release1/test_half_12")]
data += [scan("release1/test_half_13")]
data += [scan("release1/test_half_14")]
data += [scan("release1/test_half_8")]
data += [scan("release1/test_half_9")]
data += [scan("release1/train_full_0")]
data += [scan("release1/train_full_1")]
data += [scan("release1/train_full_2")]
data += [scan("release1/train_full_3")]
data += [scan("release1/train_full_4")]
data += [scan("release1/train_full_5")]
data += [scan("release1/train_full_6")]
data += [scan("release1/train_full_7")]
data += [scan("release1/train_half_10")]
data += [scan("release1/train_half_11")]
data += [scan("release1/train_half_12")]
data += [scan("release1/train_half_13")]
data += [scan("release1/train_half_14")]
data += [scan("release1/train_half_8")]
data += [scan("release1/train_half_9")]

total = [Counter({}), Counter({})]
for i in data:
    for j in range(2):
        total[j] = total[j] + Counter(i[3][j])
    
print("timestamp: {:d}, ad_ids: {:d}".format(len(total[0]), len(total[1])))
