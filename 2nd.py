from textblob import TextBlob
# testimonial = TextBlob('web/37.txt')
# print(testimonial.sentiment)
# print(testimonial.sentiment.polarity)
from textblob.sentiments import NaiveBayesAnalyzer
f=open('web/37.txt','r')
# zen = TextBlob(f.read())
# print(zen.word_counts['medical'])
polarity = f.sentiment.polarity

print(polarity)