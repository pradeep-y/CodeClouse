import pyshorteners   


url= input('Enter the url: ')   # take input from the user i.e. the url which is to be converted into short url



def shortenurl(url):     
    s = pyshorteners.Shortener()  # using shortener function of pyshortners
    print(s.tinyurl.short(url))

shortenurl(url) 

