"""
Album: Write a function called make_album() that builds a dictionary describing a music album . The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information . Use the function to make three dictionaries representing different albums . Print each return value to show that the dictionaries are storing the album information correctly .
Add an optional parameter to make_album() that allows you to store the number of tracks on an album . If the calling line includes a value for the num- ber of tracks, add that value to the album’s dictionary . Make at least one new function call that includes the number of tracks on an album . 

"""

def make_album(artist_name,album_name,num_of_Songs=''):
    music_album={'artist_name':artist_name,'album_name':album_name}
    
    if num_of_Songs:
        music_album['Total_Songs']=num_of_Songs
        
    return music_album

# Second Part
""" User Albums: Start with your program from Exercise 8-7 . Write a while loop that allows users to enter an album’s artist and title . Once you have that information, call make_album() with the user’s input and print the dictionary that’s created . Be sure to include a quit value in the while loop . """


while True:
    print('Enter the Album Details',end=' ')
    print('(Enter q to exit anytime)')
    
    Artist_Name =input('Enter Artist Name: ')
    if Artist_Name == 'q':
        break
    
    Album_title=input('enter Album Name: ')
    
    if Album_title=='q':
        break
    
    Album_Details=make_album(Artist_Name,Album_title)
    print(Album_Details)