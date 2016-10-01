#ref1: http://sahandsaba.com/static/presentations/it-from-bit.html#/10
#ref2: https://www.explainxkcd.com/wiki/index.php/1266:_Halting_Problem

#Assume this is another program called programB
programB= raw_input("Get input: ") 

#assume the function 'DoesItHalt' is a procedure that solves the halting problem
if DoesItHalt(programB):  
	print "No"  
 	while True:  #performs as infinite loops i.e not halt
		pass 
else:
	print "Yes" #performs as an end i.e halt
