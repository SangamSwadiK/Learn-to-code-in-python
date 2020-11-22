## This method is used for merging 2 dictionaries

employee_sal = {

    "Gi" : 10000,
    "James" : 50000,
    'Brandon' : 90000
}


employee_sal2 = {

    "shyam" : 10000,
    "ram" : 50000,
 
}

print( employee_sal2)

employee_sal2.update( employee_sal )

print( employee_sal2 )