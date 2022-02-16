#Now, will make a Parsec units convertor
#First should set the variables Parsec and Lightyears

parsec = 11                             #The valor of Parsec is equal to the number of Parsec to compar with Lightyears
lightyears =  + 3.26156 * parsec        #And the valor of Lightyears is equal to the formula to conver Lightyears to Parsec

#Finally justo will print a little message to accompany the resul, without forget convert the result (int) to (str) for a good concatenation 
print(str(parsec) + " parsec, is " + str(lightyears) + " lightyears")