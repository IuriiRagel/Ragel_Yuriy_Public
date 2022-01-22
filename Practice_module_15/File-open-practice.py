a = input('Enter filename')

with open(a, encoding='utf8') as f:
# open the file (hamlet.txt), read it, and split itnto list of words
# here we look at both EN and RU text
    data = f.read()
    words = data.split()

    v = {}
# create empty dictionary where we will record count of each word in text

    for word in words:
        if len(word) > 3:
            if word in v.keys():
                v[word] = v[word] + 1
            else:
                v[word]=1
 
# now we have a dictionary which has words as keys and their frequency as values

    max_key = max(v, key=v.get)

    all_values = v.values()
    max_value = max(all_values)

    print('Наиболее часто встречающееся слово размером более трех символов: ', max_key,', оно встречается ',  max_value, ' раз' )
    
# this is where we find max key and max value in the dictionary

with open(a, encoding='ascii', errors='ignore') as f2:
    data2 = f2.read()
    words2 = data2.split()
    # here we also open the same file, but now we use the american standard encoding
    # and we ignore all errors (ignore Russian characters)
    # we read the file and split it into list of words in the same manner
    
    max_engl_len = 0
    # this is the variable which will store the max length of item in the list
    for i in range(len(words2)):
        if len(words2[i]) > max_engl_len:
            max_engl_len = len(words2[i])
            max_word = words2[i]
    # this loop iterates over each item, compares its length with max_eng_len
    # and if reassigns the length and value if it is greater than stored value
    
    print('Наиболее длинное слово на английском языке: ', max_word, 'его длина = ', max_engl_len, ' символов')