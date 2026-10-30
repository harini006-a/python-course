str=input()
vowel="aeiouAEIOU"
for char in str: 
  for char in vowel:
    str =str.replace (char,"")
print(str)
