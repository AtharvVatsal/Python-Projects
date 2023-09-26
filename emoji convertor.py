message = str(input(">>>"))
words = message.split(' ')           #uses space as message spliter to diff between diff words
emoji = {":)": "😊",
         ":(": "😒",
         ":t": "👍"}
out = ''
for word in words:
    
    out += emoji.get(word, word) + " "
print(out)