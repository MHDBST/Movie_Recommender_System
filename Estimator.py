import  pickle
import ReadMovie
import operator

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)


Pusers=load_obj('Puser')
Pmovies=load_obj('Pmovie')
PGenres=load_obj('PGenre')
genres=ReadMovie.ReadMovie()
suc=0
counter=0
file='test.csv'

sum = 0;
with open(file) as votes:
    for i,vote in enumerate(votes):
        if i==0: continue
        tokens=vote.split(',')
        userID=int(tokens[0])
        movieID=int(tokens[1])
        rate=float(tokens[2])


        Puser=Pusers[userID]
        try:
            Pmovie=Pmovies[movieID]
        except KeyError:
            #print movieID,'not found in training set'
            Pmovie=[0.0000007]*11
        genre=genres[movieID]

        Probs=[1]*11
        for rate_class in range(0,11):
            for g_index,g in enumerate(genre):
                if g:
                    Probs[rate_class]*=PGenres[rate_class][userID][g_index]
            Probs[rate_class]=float(Probs[rate_class]+0.5*Puser[rate_class])+float(Pmovie[rate_class])
            Probs[rate_class] =  float(Puser[rate_class])
        index, value = max(enumerate(Probs), key=operator.itemgetter(1))
        #print index,value,rate*2.0
        sum += pow(float(index)/float(2)-rate, 2)
        if (index==rate*2.0):
            suc+=1
        counter+=1




print suc,counter,float(suc)/float(counter)
print float(sum)/float(counter)
