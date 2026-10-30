str=input()
vowel="aeiouAEIOU"
vowelcount=0
concount=0
for i in str:
  if i.isalpha():
    if i in vowel:
      vowelcount += 1
    else:
      concount += 1
print(vowelcount)
print(concount)
