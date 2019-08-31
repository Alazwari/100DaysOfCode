#Day 12

sentence = 'Please, I want {} sandwishes and {} donutes'
# 1. Replace I to we
# 2. Fill in the curly brackets 5 then 7
# 3. Replace all a letters to be capital A 
new_sentence1 = sentence.format(5, 7).replace('I', 'we').replace('a','A',len(sentence))
print(new_sentence1)
