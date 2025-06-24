import webbrowser

user_term = input("Enter your search term : ")
webbrowser.open("https://www.google.com/search?q=" + user_term)
# it takes a url argument as parameter