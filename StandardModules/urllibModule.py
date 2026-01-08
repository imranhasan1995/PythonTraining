import urllib.request
request_url = urllib.request.urlopen('https://www.geeksforgeeks.org////')
# print(request_url.read())


from urllib.parse import * 

parse_url = urlparse('https://www.geeksforgeeks.org/// / python-langtons-ant/')
print(parse_url)
print("\n")

unparse_url = urlunparse(parse_url)
print(unparse_url)

# importing robot parser class
import urllib.robotparser as rb

bot = rb.RobotFileParser()

# checks where the website's robot.txt file reside
x = bot.set_url('https://www.geeksforgeeks.org/robot.txt')
print(x)

# reads the files
y = bot.read()
print(y)

# we can crawl the main site
z = bot.can_fetch('*', 'https://www.geeksforgeeks.org////')
print(z)

# but can not crawl the disallowed url
w = bot.can_fetch('*', 'https://www.geeksforgeeks.org/// / wp-admin/')
print(w)