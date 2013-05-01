import urllib
import re
import sys

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "37278"

while True:
    try:
        source = urllib.urlopen(uri+nothing).read()
        #print re.search("next nothing is (\S+)", source).group(1)
        print source
        nothing = re.search("next nothing is (\S+)", source).group(1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        break