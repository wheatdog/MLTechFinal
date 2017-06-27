
import xgboost as xgb 
import os


param = {'max_depth':5, 'eta':1, 'silent':1, 'objective':'binary:logistic' }

num_round = 4



result = {}

path = ['id/']

test_path = ['test_indexed/']


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

f = open('xgboost_predict', 'w')

for i in range(len(result)):
	f.write(str(result[i]) + '\n')

f.close()
