# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]


name = "Dick Face"

first_name = name[0:4]
# this gives first name / [inclusive:exclusive]
last_name = name[5:]
# this gives last name / index: gives all after 
funk_name = name[::2]
# this incremented the index by 2 over name which gives "Dc ae"
reversed_name = name[::-1]
# this basically counts backwards giving "ecaF kciD"


website = "http://google.com"

slice = slice(7,-4)
# cuts out "http://" and ".com" and gives website name / this will happen regardless of the string size due to -index
# print(website[slice])
# a way of printing by reassigning website to contain slice





















