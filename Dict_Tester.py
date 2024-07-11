from PyDictionary import PyDictionary
dict = PyDictionary()

meanings = dict.meaning('run')
'''print('Meanings as a noun:')
for f in meanings['Noun']:
    f = f.title()
    print(f)

print('Meanings as a verb:')
for f in meanings['Verb']:
    f = f.title()
    print(f)'''

print(dict.synonym('life'))