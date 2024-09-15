""" 
Suppose you have a plan for travelling different countries in year 2022 with your
friends. The country that you have listed are following: ['India', 'Thailand', 'Bhutan',
'China', 'Nepal', 'Myanmar']. But one of your friends tells you that we cannot travel
Myanmar due to the political unrest. Therefore, the country name will be removed
from the list. Write program to display the entire countries name except Myanmar
using Loop in python program.Now check this answer country_list =['India','Thailand','Bhutan','China','Nepal','Myanmar']
 """
 
 
country_list = ['India', 'Thailand', 'Bhutan', 'Myanmar', 'China', 'Nepal']
updated_country_list = []

for country in country_list:
    if country != 'Myanmar':
        updated_country_list.append(country)

print(updated_country_list)
