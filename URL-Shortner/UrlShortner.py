import pyshorteners

url = input("Enter the URL: ")
short_url = pyshorteners.Shortener().tinyurl.short(url)
print(" Shortened URL Is: ",short_url)
