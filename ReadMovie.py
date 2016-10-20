file='movies.csv'

categories_list={}
categories_list['action']=0
categories_list['adventure']=1
categories_list['animation']=2
categories_list["children"]=3
categories_list['comedy']=4
categories_list['crime']=5
categories_list['documentary']=6
categories_list['drama']=7
categories_list['fantasy']=8
categories_list['film-noir']=9
categories_list['horror']=10
categories_list['musical']=11
categories_list['mystery']=12
categories_list['romance']=13
categories_list['sci-fi']=14
categories_list['thriller']=15
categories_list['war']=16
categories_list['western']=17


def ReadMovie():
    movie_dic={}
    movies=open(file).readlines()
    for movie in movies[1:]:
        tokens=movie.split(',')
        categories=tokens[2].split('|')
        categories=[x.strip().lower() for x in categories if x.strip().lower() in categories_list.keys() ]
        array=[0]*len(categories_list)
        for category in categories:
            array[categories_list[category]]=1
        movie_dic[int(tokens[0])]=array
    return  movie_dic
