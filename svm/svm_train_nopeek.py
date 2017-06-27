import sys
sys.path.append('./libsvm/')
from svmutil import *
import xgboost as xgb 
import os



def svm_read_test(data_file_name):
	
	prob_x = []
	for line in open(data_file_name):
		xi = {}
		for e in line.split():
			ind, val = e.split(":")
			xi[int(ind)] = float(val)
		prob_x += [xi]
	return prob_x


param = {'max_depth':5, 'eta':1, 'silent':1, 'objective':'binary:logistic' }

num_round = 4

track2flag = False
threshold = 0.07
xgboost_blend_weight = 0.5


result = {}

path = ['id-8/', 'id-9/', 'id-10/', 'id-11/', 'id-12/', 'id-13/', 'id-14/']

test_path = ['test_indexed-8/','test_indexed-9/', 'test_indexed-10/', 'test_indexed-11/', 'test_indexed-12/', 'test_indexed-13/', 'test_indexed-14/']

for n in range(len(path)):
	for root, dirs, files in os.walk(path[n]):
		for file_ in files:
			print(os.path.join(root, file_))


			# if test file exists
			if os.path.isfile(test_path[n] + file_):

				#dtrain = xgb.DMatrix(os.path.join(root, file_))
				#dtest = xgb.DMatrix('test_svm_indexed/' + file_)

				#bst = xgb.train(param, dtrain, num_round)

				#xgpreds = bst.predict(dtest)

			

				#svm experiment
				y, x = svm_read_problem( os.path.join(root, file_) )
				testx = svm_read_test(test_path[n] + file_)

				prob  = svm_problem(y, x)
				svm_param = svm_parameter('-s 3 -t 1 -r 1 -h 0 -b 1')
				m = svm_train(prob, svm_param)
				p_labels, p_acc, p_vals = svm_predict(len(testx)* [1], testx, m)
				#print(p_labels)
				#break

				# read index file
				index = []
				for ind in open(test_path[n] + file_ + '_index'):
					index.append(int(ind))

				for i in range(len(p_labels)):
					#result[index[i]] = xgpreds[i] * xgboost_blend_weight + p_labels[i] * (1.0 - xgboost_blend_weight)
					result[index[i]] = p_labels[i]

f = open('svm_predict-nopeek', 'w')

threshold_count = 0
total_count = 0
for i in range(len(result)):

	if track2flag == True:
		if result[i] >= threshold:
			threshold_count = threshold_count + 1
			f.write('1\n')
		else:
			f.write('0\n')
		total_count = total_count + 1
	else:
		f.write(str(result[i]) + '\n')
	
f.close()

if track2flag == True:
	print(threshold_count / total_count)
