#ref1: http://sahandsaba.com/static/presentations/it-from-bit.html#/10
#ref2: https://www.explainxkcd.com/wiki/index.php/1266:_Halting_Problem

#Assume this is another program called programB
programB= raw_input("Get input: ") 

#assume the function 'DoesItHalt' is a procedure that solves the halting problem
if DoesItHalt(programB):  
	print "No but it actually loops"  
 	while True:  #performs as infinite loop
		pass 
else:
	print "Yes but it actually halts" #program terminates
