

# Given list of country names
# Given list of country names
countries = ['India', 'Thailand', 'Bhutan', 'China', 'Nepal', 'Myanmar','Oman']

# Function to check if a string starts with a vowel
def starts_with_vowel(country):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return country[0].lower() in vowels

# Use map() to apply starts_with_vowel() function to each country
vowel_flags = map(starts_with_vowel, countries)

# Filter countries based on the flag
vowel_countries = [country for country, is_vowel in zip(countries, vowel_flags) if is_vowel]

# Print the new list
print(vowel_countries)
