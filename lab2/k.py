s = str(input())
import re  #module re that we use to remove punctuation from the sentence

sentence = re.findall(r'\w+', s) 

sentence1 = sorted(set(sentence))

print(len(sentence1))
for i in sentence1:
    print(i)