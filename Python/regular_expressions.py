import re

patterns = ["term1", "term2"]

text = "This is a string with term1 but not the other"

for pattern in patterns:
    print("I'm searching for " + pattern)


    if re.search(pattern,text):
        print("MATCH!")
    else:
        print("NO MATCH!")

#  -----------------------------------------------------------------------------

import re

text = "This is a string with term1 but not the other"

match = re.search("term1",text)
print(match.start())

#  -----------------------------------------------------------------------------

import re

split_term = "@"
email = "user@gmail.com"

print(re.split(split_term,email))

#  -----------------------------------------------------------------------------

import re

print(re.findall("match","test phrase match in match middle"))

#  -----------------------------------------------------------------------------

import re

def multi_re_find(patterns,phrase):


    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "sdsd...sssddd...sdddsddd...dsds...dssssss...sdddd"

test_pattern = ["sd"]

multi_re_find(test_pattern,test_phrase)

# ------------------------------------------------------------------------------

import re

def multi_re_find(patterns,phrase):


    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "sdsd...sssddd...sdddsddd...dsds...dssssss...sdddd"

test_pattern = ["sd*"]

multi_re_find(test_pattern,test_phrase)

# ------------------------------------------------------------------------------

import re

def multi_re_find(patterns,phrase):


    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "sdsd...sssddd...sdddsddd...dsds...dssssss...sdddd"

test_pattern = ["sd+"]

multi_re_find(test_pattern,test_phrase)

#-------------------------------------------------------------------------------

import re

def multi_re_find(patterns,phrase):


    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "sdsd...sssddd...sdddsddd...dsds...dssssss...sdddd"

test_pattern = ["sd?"]

multi_re_find(test_pattern,test_phrase)

# ------------------------------------------------------------------------------

import re

def multi_re_find(patterns,phrase):


    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "sdsd...sssddd...sdddsddd...dsds...dssssss...sdddd"

test_pattern = ["sd{3}"]

multi_re_find(test_pattern,test_phrase)

# ------------------------------------------------------------------------------

import re

def multi_re_find(patterns,phrase):


    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "sdsd...sssddd...sdddsddd...dsds...dssssss...sdddd"

test_pattern = ["sd{1,3}"]

multi_re_find(test_pattern,test_phrase)

# ------------------------------------------------------------------------------

import re

def multi_re_find(patterns,phrase):


    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "sdsd...sssddd...sdddsddd...dsds...dssssss...sdddd"

test_pattern = ["s[sd]+"]

multi_re_find(test_pattern,test_phrase)








#   REMOVING ELEMENTS FROM A STRING --------------------------------------------

import re

def multi_re_find(patterns,phrase):


    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "This is a string! But it has a punctuation. How can we remove it?"

test_pattern = ["[^!.?]+"]              # [^] removes anything inside of a string

multi_re_find(test_pattern,test_phrase)

# ------------------------------------------------------------------------------

import re

def multi_re_find(patterns,phrase):


    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "This is a string! But it has a punctuation. How can we remove it?"

test_pattern = ["[a-z]+"]

multi_re_find(test_pattern,test_phrase)


# ------------------------------------------------------------------------------

import re

def multi_re_find(patterns,phrase):


    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "This is a string! But it has a punctuation. How can we remove it?"

test_pattern = ["[A-Z]+"]

multi_re_find(test_pattern,test_phrase)

# ------------------------------------------------------------------------------

import re

def multi_re_find(patterns,phrase):


    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"

test_pattern = [r"\d"]

multi_re_find(test_pattern,test_phrase)

# ------------------------------------------------------------------------------

import re

def multi_re_find(patterns,phrase):


    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "This is a string with numbers 12312 and a symbol #hashtag"

test_pattern = [r"\D"]

multi_re_find(test_pattern,test_phrase)
