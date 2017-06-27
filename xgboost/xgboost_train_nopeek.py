
import xgboost as xgb 
import os


param = {'max_depth':5, 'eta':1, 'silent':1, 'objective':'binary:logistic' }

num_round = 4



result = {}

path = ['id-8/', 'id-9/', 'id-10/', 'id-11/', 'id-12/', 'id-13/', 'id-14/']

test_path = ['test_indexed-8/','test_indexed-9/', 'test_indexed-10/', 'test_indexed-11/', 'test_indexed-12/', 'test_indexed-13/', 'test_indexed-14/']


for n in range(len(path)):
	for root, dirs, files in os.walk(path[n]):
		for file_ in files:
			print (os.path.join(root, file_))


			# if test file exists
			if os.path.isfile(test_path[n] + file_):

				dtrain = xgb.DMatrix(os.path.join(root, file_))
				dtest = xgb.DMatrix(test_path[n] + file_)

				bst = xgb.train(param, dtrain, num_round)

				preds = bst.predict(dtest)

				# read index file
				index = []
				for ind in open(test_path[n] + file_ + '_index'):
					index.append(int(ind))

				for i in range(len(preds)):
					result[index[i]] = preds[i]

f = open('xgboost_predict-nopeek', 'w')

for i in range(len(result)):
	f.write(str(result[i]) + '\n')

f.close()
