import matplotlib.pyplot as plt
import nltk
import dateutil 
from wordcloud import WordCloud


f = open('stopwords.txt', 'r')
stopwords = f.read().splitlines()
f.close()

f = open('chat.txt', 'r')

lines = f.read().splitlines()

datesD = {}
runtext = " "

for line in lines:
    timestamp, message = line[:16], line[16+2:]
    # For timestamp
    try:
        date = dateutil.parser.parse(timestamp)
        date = date.date() 
        if date in datesD: 
            datesD[date]+=1
        else:
            datesD[date]=1
    except ValueError:
        print("No Date Format")

    # For messages 

    words = nltk.word_tokenize(message)   
    for word in words:
        word = word.lower()
        runtext+=" "
        runtext+=word   


# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(runtext)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# Plot nr of messages over time
x,y = zip(*sorted(datesD.items()))
plt.plot(x,y)
plt.show()


    