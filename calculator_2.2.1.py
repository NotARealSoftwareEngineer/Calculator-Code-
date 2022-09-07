from math import *

def gcdCalcFunc(a,b): # this was written to support the factoring function, but stands alone as well.
	if (b==0): return a #if b is zero than it can no longer have any common factors
	else:return gcdCalcFunc(b,a%b) #returns the b value and the remainder until there is no longer a remainder, then returns the GCD

def x_to_less(v,xP):
	x = xP - v  #subtracts whatever v is, somewhere between .1 and .00001
	return x #returns new x value to run f(x)

def x_to_more(v, xP):
	x = xP + v #adds whatever v is, somewhere between .1 and .00001
	return x   #returns new x value to run f(x)

def simple_calculator():
	x= eval(input('Enter x: ')) #Determines x variable
	y = eval(input('enter equation: ')) #runs f(x)
	print(y) #prints f(x)


def instant_velocity():
	xP = eval(input('Enter x: ')) #determines Parent x variable
	yP = input('enter a string: ') #determines Parent y variable
	print(yP) #prints the long hand equation from line above

	y= yP
	x=xP #ensures variables match their parents to call function
	x=eval('x_to_less(.0001, xP)') # calls function with x .0001 removed to the left
	print(eval(y), x) #evaluates the function with the new x
	y0 = eval(y)
	x0 = x #captures x and y values for first slots in list

	y= yP
	x=xP  #ensures variables match their parents to call function
	x=eval('x_to_more(.0001, xP)') # calls function with x .0001 removed to the right
	print(eval(y), x)#evaluates the function with the new x
	y1 = eval(y)
	x1 = x  #captures x and y values for second slots in list

	yvalues = [y0,y1] #defines list 
	xvalues = [x0,x1] #defines list 
	m = (y1-y0)/(x1-x0) #calculates slope using deltaY/deltaX formula, pulling from lists
	for z in range(2): print("x = %.6f, y = %.6f"%(xvalues[z],yvalues[z])) #prints both sets of x and y values
	print("Instant Velocity: %.6f"%m) #provides answer

def slope_at_point():# most of this could be done with a loop, using a variable to the power of negative ten to drop the x value by that many, but this was my first function in my first program
	px = eval(input('Point P x value: '))
	py = eval(input('Point P y value: '))

	xP = eval(input('Enter x: ')) #determines Parent x variable
	yP = input('enter a string: ') #determines Parent y variable
	print(yP) #prints the long hand equation from line above

	y= yP
	x=xP #ensures variables match their parents to call function
	x=eval('x_to_less(.1, xP)') # calls function with x .1 removed to the left
	print(eval(y), x) #evaluates the function with the new x
	y0 = y
	x0 = x #captures x and y values for first slots in lists

	y= yP
	x=xP #ensures variables match their parents to call function
	x=eval('x_to_less(.01, xP)') # calls function with x .01 removed to the left
	print(eval(y), x) #evaluates the function with the new x
	y1 = y
	x1 = x #captures x and y values for second slots in lists

	y= yP
	x=xP #ensures variables match their parents to call function
	x=eval('x_to_less(.001, xP)') # calls function with x .001 removed to the left
	print(eval(y), x) #evaluates the function with the new x
	y2 = y
	x2 = x #captures x and y values for third slots in lists

	y= yP
	x=xP #ensures variables match their parents to call function
	x=eval('x_to_less(.0001, xP)') # calls function with x .0001 removed to the left
	print(eval(y), x) #evaluates the function with the new x
	y3 = y
	x3 = x #captures x and y values for fourth slots in lists

	y= yP
	x=xP  #ensures variables match their parents to call function
	x=eval('x_to_more(.0001, xP)') # calls function with x .0001 removed to the right
	print(eval(y), x)#evaluates the function with the new x
	y4 = y
	x4 = x  #captures x and y values for second slots in list

	y= yP
	x=xP  #ensures variables match their parents to call function
	x=eval('x_to_more(.001, xP)') # calls function with x .001 removed to the right
	print(eval(y), x)#evaluates the function with the new x
	y5 = y
	x5 = x  #captures x and y values for second slots in list

	y= yP
	x=xP  #ensures variables match their parents to call function
	x=eval('x_to_more(.01, xP)') # calls function with x .01 removed to the right
	print(eval(y), x)#evaluates the function with the new x
	y6 = y
	x6 = x  #captures x and y values for second slots in list

	y= yP
	x=xP  #ensures variables match their parents to call function
	x=eval('x_to_more(.1, xP)') # calls function with x .1 removed to the right
	print(eval(y), x)#evaluates the function with the new x
	y7 = y
	x7 = x  #captures x and y values for second slots in list

	m0 = (py-y0)/(px-x0)#generating the various slopes using the (y2-y1)/(x2-x1) formula, and assigning them to the slope list
	m1 = (py-y1)/(px-x1) #sometimes python doesnt like the variable py, might change in future
	m2 = (py-y2)/(px-x2)
	m3 = (py-y3)/(px-x3)
	m4 = (y4-py)/(x4-px)
	m5 = (y5-py)/(x5-px)
	m6 = (y6-py)/(x6-px)
	m7 = (y7-py)/(x7-px)

	yvalues = [y0,y1,y2,y3,y4,y5,y6,y7]#  List of y values
	xvalues = [x0,x1,x2,x3,x4,x5,x6,x7] #  List of X values
	mvalues= [m0,m1,m2,m3,m4,m5,m6,m7]# list of slopes between each point(q) and the original (p)

	for z in range(8):print('x: %.6f'%xvalues[z], ', slope: %.6f'%mvalues[z]) #loop to print off the x values and slopes, to six decimal places like the homework required
	avg_m = (m0+m1+m2+m3+m4+m5+m6+m7)/8 #finding the average slope
	print('avg slope = %.6f'%avg_m) #printing average slope to 6 decimal places

def factoring_function(): #written to support factoring for calculus chapter 2
	print('Enter the following in the form ax^2+bx+c') #guides the user for how information should be input
	a=float(input('a = ')) #float ensures the computer doesnt recognize it as an int. alternatively I might use Eval for the same purpose
	b= float(input('b = '))
	c = float(input('c = '))


	gcdTemp = gcdCalcFunc(a,b) #finds the GCD of a and b
	gcd = gcdCalcFunc(gcdTemp,c)# finds the GCD of (a and b) and c

	if c==0:
		print(str(gcd)+"x("+str(a/gcd)+"x + "+str(b/gcd)+")") # if c = 0, this will still output a factored equation without quadratic formula

	else:
		sol1Num = -b+((b**2)-(4*a*c))**(1/2) #used to affect the positive of +- in quadratic formula, derives first square
		sol2Num = -b-((b**2)-(4*a*c))**(1/2) #used to affect the negative of +- in quadratic formula, derives second square
		denom = 2*a

		if not (sol1Num.is_integer() and sol2Num.is_integer()) or not denom.is_integer(): print('Does Not factor cleanly)') # ensures that the factorization is possible. might need to be amended for fractions

		else:
			sol1GCD = gcdCalcFunc(sol1Num, denom) #pulls the gcd out of first solution
			sol2GCD = gcdCalcFunc(sol2Num, denom) #pulls the gcd out of the second solution

			sol1Num = -sol1Num/sol1GCD #removes the negative sign from the answer, and reconciles pulling GCD out
			sol1Denom = denom/sol1GCD #reconciles pulling gcd out
			sol2Num = -sol2Num/sol2GCD #removes the negative sign from the answer, and reconciles pulling GCD out 
			sol2Denom = denom/sol2GCD
			print(str(gcd*a/abs(a))+"("+str(sol1Denom)+"x + "+str(sol1Num)+")("+str(sol2Denom)+"x + "+str(sol2Num)+")") 
			# ive had some issues with the computer pulling out non intuitive, but correct, answers. Has difficulty with distributing negatives.
			# 1*(x-5) is the same as -1(5-x), limitation of the way I output answers.


def calc_easy():   #stupid simple, it just evaluates and prints the input. Useful for quick calculations
	y=eval(input('enter math: '))
	print(y)
	
def entry_guide():
	print('Under Construction: Sorry for the inconvinience!')

def gcd_standalone():# this keeps the main function clean by requesting inputs for the GCD calculator from a function instead 
	a = eval(input('First Number: '))
	b = eval(input('Second Number: '))
	gcd_standalone_sol = gcdCalcFunc(a,b)
	print('The GCD/GCF of '+str(a)+' and '+str(b)+' is '+str(gcd_standalone_sol))#orchestrates the answer in an inteligible way
	

def trig_calculator():# this is the translation of my c++ trig calculator. Brace for Impact. 
	trig_input_choice = eval(input('Choose input method:\n1.) Shape Specific\n2.) Input Values\nSelection: '))# since its short, I just eval the input instead of printing the options then eval
	if (trig_input_choice == 1): 
		print('1.) Side-Angle-Side (SAS)\n2.) Side-Side-Side (SSS)\n3.) Angle-Side-Angle (ASA)\n4.) Angle-Angle-Side (AAS)\n5.) Hypotenuse-Leg (HL) [warning: only for right angle triangles]\n')
		trig_shape_input_choice = eval(input('Selection: '))
		if (trig_shape_input_choice != 0):
			trig_sas_angleSelect = input('Which angle were you given? ')
			
			if (trig_sas_angleSelect.upper()=='A'): print('cool')


for z in range(100):# this just keeps it going, I will change this if I often need to run the calculator more than 100 times in a row.
	if (z!=0): print ('\n\n\n')
	print("Seneca Red Calculator v2.2\nSean Gunther, 2021\n\"...Look on my Works, ye Mighty, and despair!\"\n")
	print("1.) Entry Guide\n2.) Simple Function Calculator\n3.) Simple Calculator without Variables\n4.) Instant Velocity\n5.) Slope of Line Through Point\n6.) Factor a Polynomial\n7.) Greatest Common Factor/Denominator\n8.) Trig Calculator\n")
	function_select = int(input('Selection: '))
	if (function_select == 1): entry_guide()
	elif (function_select == 2): simple_calculator()
	elif (function_select == 3): calc_easy()
	elif (function_select == 4): instant_velocity()
	elif (function_select == 5): slope_at_point()
	elif (function_select == 6): factoring_function()
	elif (function_select == 7): gcd_standalone()
	elif (function_select == 8): trig_calculator()
	elif (function_select == 999) or (function_select == -999): break #hold over from my procedural programming course
	else: print('Invalid Input')


	#the below is the 2.0 variant
	#print("1.) Simple function calculator\n2.) Slope of line at point\n3.) Instant velocity at a time\n4.) Factoring\n5.) Simple Calculator without variables")
	#function_select = eval(input('Selection: '))
	#if (function_select==1): simple_calculator()
	#elif (function_select ==3): instant_velocity()
	#elif (function_select == 2): slope_at_point()
	#elif (function_select == 4): factoring_function()
	#elif (function_select == 5):calc_easy()

