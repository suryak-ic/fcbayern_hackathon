import json
from pprint import pprint
import numpy as np
from sklearn import preprocessing

data = json.load(open('file1.json'))
min = raw_input("minute %n")
sec = raw_input("second %n")

players = ['49431', '165687', '105046', '37793', '40691', '161450', '8533', '55634', '56764', '60025', '28559', '45015', '21227', '51184', '5058', '42565', '168568', '129508'] #list of Bayern playerIDs
hype = np.array([1, 1, 1, 1, 1,   1, 1, 1, 1, 1,   1, 1, 1, 1, 1,   1, 1, 1 ], dtype=np.float)
hype = hype*0.5
print hype

for player in players:
	hype1 = sum(1 for e in data['Games']['Game']['Event'] if e['@attributes']['type_id'] == '1' and e['@attributes']['min'] == min and e['@attributes']['player_id'] == player)
	print hype1
	
X_normalized = preprocessing.normalize(hype, norm='l2')
print X_normalized