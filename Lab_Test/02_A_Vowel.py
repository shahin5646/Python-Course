# Check Vowels or Not 

def count_vowels(sentence):
  
  vowels = "aeiouAEIOU"
  vowel_count = 0
  for word in sentence:
    if word in vowels:
      vowel_count += 1
  return vowel_count


sentence = input("Enter a sentence: ")
vowel_count = count_vowels(sentence)
print(f"The number of vowels in the sentence is {vowel_count}")
