

import xgboost as xgb 



dtrain = xgb.DMatrix('id_svm/id-576772')
dtest = xgb.DMatrix('test_svm_indexed/id-576772')


param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'binary:logistic' }


num_round = 2

bst = xgb.train(param, dtrain, num_round)

preds = bst.predict(dtest)

print preds