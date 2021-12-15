import re
test_string = "THIS IS THE HAPPIEST NEURONS COMMUNITY "
# original string
print ("The original string is : " + test_string)
# using regex (findall()) function
res = len(re.findall(r'\w+', test_string))
# total no of words
print ("The number of words in string are : " + str(res))
