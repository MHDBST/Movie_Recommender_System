import random
import math

file='ratings.csv'
train_list=[]
test_list=[]
temp_list=[]
preID=-1


with open(file) as votes:
    for i,vote in enumerate(votes):
        if i==0: continue
        tokens=vote.split(',')
        userID=int(tokens[0])
        movieID=int(tokens[1])
        rate=float(tokens[2])

        if(userID==preID):
            temp_list.append(vote)
        else:
            preID=userID
            size=int(math.floor(len(temp_list)/10))
            test=random.sample(range(0, len(temp_list)), size)
            for i,item in enumerate(temp_list):
                if i in test:
                    test_list.append(item)
                else:
                    train_list.append(item)
            #print  len(train_list),len(test_list)
            temp_list=[]
            temp_list.append(vote)

output=open('train.csv','w')
for item in train_list:
    output.write(item)
output=open('test.csv','w')
for item in test_list:
    output.write(item)
