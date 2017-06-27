# USE python 2.7

import os




def read_data(data_file_name):
    prob_data = []
    
    for line in open(data_file_name):
        line = line.split("|user ",1)

        ad = []
        for i in line[0].split():
            ad += [i]

        user = []
        for i in line[1].split():
            user += [int(i)]

        prob_data += [[ad, user]]
        

    return prob_data


root = 'release1/'

testdata = ['test_half_8', 'test_half_9', 'test_half_10', 'test_half_11', 'test_half_12', 'test_half_13', 'test_half_14']

trainfulldata = ['train_full_0', 'train_full_1', 'train_full_2', 'train_full_3', 'train_full_4', 'train_full_5', 'train_full_6', 'train_full_7']

trainhalfdata = ['train_half_8', 'train_half_9', 'train_half_10', 'train_half_11', 'train_half_12', 'train_half_13', 'train_half_14']


output_root = ['id-8/', 'id-9/', 'id-10/', 'id-11/', 'id-12/', 'id-13/', 'id-14/']
#output_index_suffix = '_index'


used_data = trainfulldata

appeared_id = []

for n in range(len(output_root)):
	appeared_id = []
	print "Peek data until " + trainhalfdata[n]
	used_data.append(trainhalfdata[n])

	for filename in used_data:
		path = root + filename

		print "Processing: " + path

		prob_data = read_data(path)

		for i in range(len(prob_data)):
			output_file = output_root[n] + prob_data[i][0][1]
			f1 = open(output_file, 'a')

			f1.write(str(prob_data[i][0][2]) + ' ')

			for j in range(len(prob_data[i][1])):
				f1.write(str(prob_data[i][1][j]) + ':1 ')
			if prob_data[i][0][1] not in appeared_id and str(prob_data[i][1][len(prob_data[i][1]) - 1]) != '136':
				f1.write('136:0 ')
				if prob_data[i][0][1] not in appeared_id:
					appeared_id.append(prob_data[i][0][1])
			f1.write('\n')

			f1.close()

	#print cnt, prob_data
