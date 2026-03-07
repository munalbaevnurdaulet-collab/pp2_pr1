import re


#a = re.compile("^x$")
#print(bool(a.search("x")))
#print(bool(a.search("xx")))

"""fish = re.compile(r"^(bir|eki) balyq$")
for i in ["bir balyq",'eki balyq','qyzyl balyq','qara balyq']:
    print(f"{i}: {bool(fish.search(i))}")"""

book = re.compile(r"^(Book|Mattress|Grocery) (store|supplier)$")
print(bool(re.search(book,"Mattress supplier")))





