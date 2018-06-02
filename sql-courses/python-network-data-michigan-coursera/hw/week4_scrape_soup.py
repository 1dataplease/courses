from BeautifulSoup import *
import urllib

url = raw_input('Enter url - ')
#url = 'http://python-data.dr-chuck.net/comments_42.html'
#url = 'http://python-data.dr-chuck.net/comments_292934.html'

html_string = urllib.urlopen(url).read()
souped_it = BeautifulSoup(html_string)

## get list of anchor/a tags or span tags
## each tag is like a dictionary of html attributes

tags = souped_it('tr')
nums = []

for tag in tags:
    tag_str = str(tag)
    if 'span' in tag_str:
        end_pt = tag_str.find("</span>")
        start_pt = tag_str.find('comments">')+10
#    print end_pt
        num = tag_str[start_pt:end_pt]
        nums.append(int(num))
        
print sum(nums)