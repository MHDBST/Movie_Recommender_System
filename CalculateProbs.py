import pickle
import ReadMovie

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)
'''
print 'loading movie'
movie_votes={}
movie_votes=load_obj('movie-votes')
Pmovie ={}
print 'calculating movies'
for item in movie_votes:
    if Pmovie.has_key(item):
        continue
    list=movie_votes[item]
    list2=[x[1]*2 for x in list ]
    Pmovie[item]=[0.0]*11
    for i in range(0,11):
       try:
        Pmovie[item][i]= float(list2.count(i))/float(len(list2))+0.0000001
       except KeyError:
           print item,i
           exit()
print 'saving movies'
movie_votes=0
save_obj(Pmovie,'Pmovie')
Pmovie=0

print 'loading users'
user_votes=load_obj('user-votes')
Puser = [[0.0 for x in range(11)] for x in range(len(user_votes)+1)]
Cuser = [[0.0 for x in range(11)] for x in range(len(user_votes)+1)]
print 'calculating user'
numberOfUsers=len(user_votes.keys())
print numberOfUsers
for item in user_votes:
    list=user_votes[item]
    list2=[x[1]*2 for x in list ]
    for i in range(0,11):
       try:
        Puser[item][i]= float(list2.count(i))/float(len(list2))+0.0000001
        Cuser[item][i]= float(list2.count(i))

       except:
           print 'user',item,i
           exit()
print'saving user'
save_obj(Puser,'Puser')
save_obj(Cuser,'Cuser')
Puser=0
user_votes=0
'''
print 'loading genres'
Cuser=load_obj('Cuser')
genres=ReadMovie.ReadMovie()
PGenres=[]

for i in range(0,11):
    numberOfUsers=138492
    P1Genres=[[0.0 for x in range(18)] for x in range(numberOfUsers+1)]
    PGenres.append(P1Genres)

user_movie=load_obj('user-movie')
print 'calculating genres'
for item in sorted(user_movie):
    try:
        genre=genres[item[1]]
        for g_index,g in enumerate(genre):
                #print int(user_movie[item]*2),int(item[0]),g_index
                PGenres[int(user_movie[item]*2)][int(item[0])][g_index]+=g
    except:
        print 'error',item

    #normalizing
for rate,item in enumerate(PGenres):
    for user,item2 in enumerate(item):
        for genre,item3 in enumerate(item2):
            try:
                PGenres[rate][user][genre]=float(item3)/float(sum(item2))
            except:
                 PGenres[rate][user][genre]=10^-7
save_obj(PGenres,'PGenre')
