import os
import re
from collections import Counter
from nltk.corpus import stopwords
import csv

filedir = os.getcwd() + '/articles'  # 用os合并5个txt
filenames = os.listdir(filedir)
articles = open('result.txt', 'w')

for filename in filenames:
    filepath = filedir + '/'
    filepath = filepath + filename
    for line in open(filepath):
        articles.writelines(line)
    articles.write('\n')
filename = 'result.txt'
file = open(filename, 'rt')
text = file.read()

words = re.split(r'\W+', text)  # 把标点去了
words = text.split(" ")  # 单词以空格为区分
words_in_articles = [word.lower() for word in words]  # 单词全部变为小写
stoplist = stopwords.words('english')  # 引入nltk的stopwords
cleanwords = [word for word in words if word not in stoplist]  # 导出有用单词

word_counts = Counter(cleanwords)  # 用counter算出前15个频繁词
top_fifteen = word_counts.most_common(15)
print(top_fifteen)

with open('result.csv', mode='w') as f:  # 导出csv
    mywriter = csv.writer(f)
    header = ['keyword', 'frequency']
    mywriter.writerow(header)
    mywriter.writerows(top_fifteen)
