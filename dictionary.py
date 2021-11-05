#key value pair
#ordered data type
"""

marks = {"Avinash":90,"Ramu":80,"Suresh":70}

key = Avinash
Value = 90
item = Avinash:90
new = "ritheesh"


#method 1
print(marks["Ramu"])
print(marks["Avinash"])
#print(marks["ritheesh"])

#Method 2
print(marks.get("Ramu"))
print(marks.get("Ritheesh","null"))#505, error 200(success) , page not fou


#updating the dict
marks.update({"kiran":40,"parag":100})
print("print all the content in dict",marks)

#printing only keys
print("printing only keys",marks.keys())
print("printing only values",marks.values())
print("printing items",marks.items())

#deleting
del marks["Avinash"]
print(marks)

#Zip
key = [1,2,3,4]
values = [5,6,7,8]

zipping = dict(zip(key,values))
print(zipping)

"""


employee = {"empid":2543,"name":"raju","department":[1,2,3]}
print(employee["department"])

employee1 = {1:"Ritheesh",2:"Avinash",3:{4:"deekshith",5:"sravan",6:"Mohan"},7:"subbu"}

print(employee1[3])






