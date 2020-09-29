word1 = input()
word2 = input()

# How many letters does the longest word contain?
s = list(word1)
s2 = list(word2)
c = 0
c2 = 0
#while c != s:
#    c += 1
if (len(word1) > len(word2)):
    l = len(word1)
else:
    l = len(word2)
print(l)
