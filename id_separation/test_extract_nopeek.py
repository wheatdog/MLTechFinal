# USE python 2.7

import os




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


root = 'release1/'

testdata = ['test_half_8', 'test_half_9', 'test_half_10', 'test_half_11', 'test_half_12', 'test_half_13', 'test_half_14']


glob_cnt = 0

output_root = ['test_indexed-8/', 'test_indexed-9/', 'test_indexed-10/', 'test_indexed-11/', 'test_indexed-12/', 'test_indexed-13/', 'test_indexed-14/']
output_index_suffix = '_index'

for n in range(len(testdata)):
	appeared_id = []
	path = root + testdata[n]

	print "Processing: " + path

	cnt, prob_data = read_data(path)

	for i in range(len(prob_data)):
		output_file = output_root[n] + prob_data[i][0][1]
		output_index_file = output_root[n] + prob_data[i][0][1] + output_index_suffix
		f1 = open(output_file, 'a')
		f2 = open(output_index_file, 'a')

		for j in range(len(prob_data[i][1])):
			f1.write(str(prob_data[i][1][j]) + ':1 ')
		if prob_data[i][0][1] not in appeared_id and str(prob_data[i][1][len(prob_data[i][1]) - 1]) != '136':
			f1.write('136:0 ')
			if prob_data[i][0][1] not in appeared_id:
				appeared_id.append(prob_data[i][0][1])
		f1.write('\n')
		f2.write(str(glob_cnt + i) + '\n')

		f1.close()
		f2.close()



	glob_cnt = glob_cnt + cnt
	#print cnt, prob_data
