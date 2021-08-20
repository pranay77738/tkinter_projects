from textblob import TextBlob

words = ['redy','papr','mov','atack']
new_words = []
for i in words:
    new_words.append(TextBlob(i))

print("old worde :",words)
for j in new_words:
     print(j.correct(),end=", ")