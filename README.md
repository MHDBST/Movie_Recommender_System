# Movie_Recommender_System
This Project is a Movie Recommender System by using Baysian Classifier

In this project I aim to recommend a movie to a user based on previous points to movies. The points are numbers between 0 and 5, which 5 means absuloutly satisfied and 0 means completly disatisfied.
The dataset here is MovieLenz20M which contains 20M records from 138000 users about 27000 movies. This dataset has two groups of data, first data about users and second data about movies.
For movies, it contains movie name and movie genre. 18 different genres are in the dataset. Some movies are not mapped to special genres and also some have noisy genres.
For users, it contains Userid, Movieid, rating of the user to that movie and timestamp of the rating. 
To solve this problem, I use 4 groups of data. First which user is interested in which genres. Which shows which genre/genres is/are in favor of a user. Second, which film is popular for all users. It is calculated by the mean ratings of different users to a movie. It shows may be a movie independent of its genre is popular for most of the people. Another feature is a user rating. Some people rate very low and some rate very high. Whether a user is strict on rating can be found by calculating the mean of his ratings to all movies. The timestamp is another feature which is not used in this project.
I developed a classifier with 10 classes for this question. Also a baysian classifier is used because it is a statistical method and it matches this question. Also it is interpretable and easy to understand. Another point is that some feature are independent so the baysian can fit this question well enough. I model different feature like this:
Pr(U): The probability which User U give vote r
Pr(M): The probability which Movie M gains vote r
Pr(G1,...,G18|U): The probability that user U give vote r to  genre G1,...,G18.
For the last probability, I use Baysian Classifier, because the data is sparse and also it can be said that genres are independent features. 

At the end, I create two models using these features.
First a model by combining these feature all together to model the last probability. Each feature has its own weight. The weight can be found in different method like gf method.
Another is by using Naive Bayse method and multiplying them to find out the last probability.

For more information on the formula and methods contact the author.
