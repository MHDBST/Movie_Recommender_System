import pickle
import time
def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

file='train.csv'
#[userID,movieID]=rate
user_movie={}
#[userID]=list (movieID,rate)
#for speed reason
#[movieID]=list (userID,rate)
movie_votes={}
user_votes={}
start=time.clock()
with open(file) as votes:
    for i,vote in enumerate(votes):

        if i%100000==0:
            print i,time.clock()-start
            start=time.clock()

        if i==0: continue

        tokens=vote.split(',')
        userID=int(tokens[0])
        movieID=int(tokens[1])
        rate=float(tokens[2])
        user_movie[userID,movieID]=rate
        try:
            user_votes[userID].append((movieID,rate))
        except:
            user_votes[userID]=[]
            user_votes[userID].append((movieID,rate))

        try:
            movie_votes[movieID].append((userID,rate))

        except:
            movie_votes[movieID]=[]
            movie_votes[movieID].append((userID,rate))

print 'saving 1'
save_obj(user_votes,'user-votes')
print 'saving 2'
save_obj(movie_votes,'movie-votes')
print 'saving 3'
save_obj(user_movie,'user-movie')