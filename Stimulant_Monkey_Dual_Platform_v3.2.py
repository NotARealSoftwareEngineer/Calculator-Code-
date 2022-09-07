from math import *
from tkinter import *

def terminal():
	

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
		x= x_to_less(.0001, xP) # calls function with x .0001 removed to the left
		print(eval(y), x) #evaluates the function with the new x
		y0 = eval(y)
		x0 = x #captures x and y values for first slots in list

		y= yP
		x=xP  #ensures variables match their parents to call function
		x= x_to_more(.0001, xP) # calls function with x .0001 removed to the right
		print(eval(y), x)#evaluates the function with the new x
		y1 = eval(y)
		x1 = x  #captures x and y values for second slots in list

		yvalues = [y0,y1] #defines list 
		xvalues = [x0,x1] #defines list 
		m = (y1-y0)/(x1-x0) #calculates slope using deltaY/deltaX formula, pulling from lists
		for z in range(2): print("x = %.6f, y = %.6f"%(xvalues[z],yvalues[z])) #prints both sets of x and y values
		print("Instant Velocity: %.6f"%m) #provides answer

	def slope_at_point():# most of this could be done with a loop, using a variable to the power of negative ten to drop the x value by that many, but this was my first function in my first program
		px = float(input('Point P x value: '))
		py = float(input('Point P y value: '))

		xP = float(input('Enter x: ')) #determines Parent x variable
		yP = input('enter a string: ') #determines Parent y variable
		print(yP) #prints the long hand equation from line above

		y= yP
		x=xP #ensures variables match their parents to call function
		x= x_to_less(.1, xP) # calls function with x .1 removed to the left
		print(eval(y), x) #evaluates the function with the new x
		y0 = eval(y)
		x0 = x #captures x and y values for first slots in lists

		y= yP
		x=xP #ensures variables match their parents to call function
		x=x_to_less(.01, xP) # calls function with x .01 removed to the left
		print(eval(y), x) #evaluates the function with the new x
		y1 = eval(y)
		x1 = x #captures x and y values for second slots in lists

		y= yP
		x=xP #ensures variables match their parents to call function
		x=x_to_less(.001, xP) # calls function with x .001 removed to the left
		print(eval(y), x) #evaluates the function with the new x
		y2 = eval(y)
		x2 = x #captures x and y values for third slots in lists

		y= yP
		x=xP #ensures variables match their parents to call function
		x=x_to_less(.0001, xP) # calls function with x .0001 removed to the left
		print(eval(y), x) #evaluates the function with the new x
		y3 = eval(y)
		x3 = x #captures x and y values for fourth slots in lists

		y= yP
		x=xP  #ensures variables match their parents to call function
		x=x_to_more(.0001, xP) # calls function with x .0001 removed to the right
		print(eval(y), x)#evaluates the function with the new x
		y4 = eval(y)
		x4 = x  #captures x and y values for second slots in list

		y= yP
		x=xP  #ensures variables match their parents to call function
		x=x_to_more(.001, xP) # calls function with x .001 removed to the right
		print(eval(y), x)#evaluates the function with the new x
		y5 = eval(y)
		x5 = x  #captures x and y values for second slots in list

		y= yP
		x=xP  #ensures variables match their parents to call function
		x=x_to_more(.01, xP) # calls function with x .01 removed to the right
		print(eval(y), x)#evaluates the function with the new x
		y6 = eval(y)
		x6 = x  #captures x and y values for second slots in list

		y= yP
		x=xP  #ensures variables match their parents to call function
		x=x_to_more(.1, xP) # calls function with x .1 removed to the right
		print(eval(y), x)#evaluates the function with the new x
		y7 = eval(y)
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
		print('Example problem for factoring: \n1.) 7x^2+12x-27\n2.) x^2+15x+54')
	
	def patch_notes():
		print('\nPatch Notes:\n')
		print('1.0 : taught myself how to code python', anchor = "e")
		print('1.1 : function to determine instant velocity', anchor = "e")
		print('1.2 : added function to determin slope of a line through a single point', anchor = "e")
		print('2.0 : changed the way inputs were added from variable by variable to string equations', anchor = "e")
		print('2.0.1 : made the program mobile compatible through pythonista', anchor = "e")
		print('2.2 : redesigned the layout of the selection menu')
		print('2.2.1 : went live, patched to be downloaded by colleagues as a .py executable')
		print('2.2.2 : patched an issue with the way selections were made which crashed the program')
		print('	 (changed selection = eval(input()) to selection = int(input())')
		print('2.3 : began rewriting my c++ trig calculator as a single function')
		print('2.3.1 : minor bug fixes')
		print('2.3.2 : Finally got the meth monkey to calculate SAS triangles correctly, after many many hours of frustration')
		print('2.4 : added ASA and SSS triangles. Also added some dependant functions')
		print('2.4.1 : added some example problems to entry_guide, as well as some notes on trig calculator')
		print('2.4.2 : fixed issue preventing trig calculator from working')
	
	def gcd_standalone():# this keeps the main function clean by requesting inputs for the GCD calculator from a function instead 
		a = eval(input('First Number: '))
		b = eval(input('Second Number: '))
		gcd_standalone_sol = gcdCalcFunc(a,b)
		print('The GCD/GCF of '+str(a)+' and '+str(b)+' is '+str(gcd_standalone_sol))#orchestrates the answer in an inteligible way

	def sas_side_cos_law(angle_1,side_2,side_3):
		# I hate that I had to break it up like this but, if the math is written in a single or two strings, it gets all messed up 
		# the meth monkey with the abacus  is not as smart as I thought it was, you have to tell it exactly what to do
		f = cos(angle_1) # I used variables that cannot be confused with a triangle, but they could be anything
		g = side_2*side_3 # I never do more than one type of operation per variable
		h = -2
		j = side_2*side_2
		k = side_3*side_3
		l = (f*g*h) # this one only multiplies variables
		p = j+k+l # this one only adds them
		side_1 = sqrt(p)
		return side_1

	def angle_sin_law(angle_1, side_1, side_2):
		f = sin(angle_1)
		g = side_2*f
		h = g/side_1
		angle_2 = asin(h)
		return angle_2 

	def side_sin_law(side_1,angle_1,angle_2):
		f = sin(angle_1)
		g = sin(angle_2)
		h = side_1*g
		side_2 = h/f
		return side_2

	def sss_angle_cos_law(side_1,side_2,side_3):
		f = side_1*side_1 # a^2
		g = side_2*side_2 # b^2
		h = side_3*side_3 # c^2
		j = side_2*side_3 # b*c
		k = (f-g-h) # numerator of fraction to get cosine(A) by itself on the right side of the equation
		l = (-2*j) # denominator of fraction to get cosine(A) by itself on the right side of the equation
		m = (k/l)  # (a^2 - b^2 - c^2)/(-2 * b*c)
		angle_1 = acos(m) 
		return angle_1

	def trig_calculator():# this is the translation of my c++ trig calculator. Brace for Impact. 
	
		trig_input_choice = 1 # old code I didnt need: eval(input('\nChoose input method:\n1.) Shape Specific\n2.) Input Values\nSelection: '))
		if (trig_input_choice == 1): 
			print('\n1.) Side-Angle-Side (SAS)\n2.) Side-Side-Side (SSS)\n3.) Angle-Side-Angle (ASA)\n4.) Angle-Angle-Side (AAS)\n5.) Hypotenuse-Leg (HL) [warning: only for right angle triangles]\n')
			trig_shape_input_choice = eval(input('Selection: '))

			if (trig_shape_input_choice == 1):
				ParentAngle, angle_2, angle_3, ParentSide, side_2, side_3 = 0,0,0,0,0,0
				sas_trig_values = [ParentAngle, angle_2, angle_3,ParentSide,side_2,side_3]

				trig_sas_angleSelect = input('SAS: Which angle were you given? ') # the math is the same regardless, but this helps print out the correct triangle, not just a congruent triangle.
				if (trig_sas_angleSelect.upper()=='A'): 
					angle_1 = eval(input('\nenter angle A: ')) #eval to allow for funky inputs, assumes that inputs are in degrees
					side_2 = eval(input('enter side b: ')) #doesnt accept units, just values
					side_3 = eval(input('enter side c: ')) 
					angle_1 = radians(angle_1) # converts the degrees input into radians, ALL MATH PERFORMED WITH RADIANS
					side_1 = sas_side_cos_law(angle_1,side_2,side_3) # Generates the opposite side from the angle given
					angle_2 = angle_sin_law(angle_1,side_1,side_2) # generates the second angle 
					A= round(degrees(angle_1),3) #converts back to degrees
					B= round(degrees(angle_2),3) #converts back to degrees
					C = 180-(A+B) # only angle math done with degrees instead of radians
				
					print('\nA = '+str(A)+'  a = '+str(round(side_1,3))) #this block prints the angle and side of same name. I could probably code a gui, however
					print('B = '+str(B)+'  b = '+str(round(side_2,3)))
					print('C = '+str(C)+'  c = '+str(round(side_3,3)))


				elif (trig_sas_angleSelect.upper()== 'B'): #this segment and the one below it are the same as the 'A' version but with the names moved around.
					angle_1 = eval(input('\nenter angle B: ')) # angle 1 is always the input angle, side 1 is always the inputs opposite side.
					side_2 = eval(input('enter side a: ')) #side 2 is the second input, etc
					side_3 = eval(input('enter side c: '))
					angle_1 = radians(angle_1)
					side_1 = sas_side_cos_law(angle_1,side_2,side_3)
					angle_2 = angle_sin_law(angle_1,side_1,side_2)
					A= round(degrees(angle_2),3)
					B= round(degrees(angle_1),3)
					C = 180-(A+B)
					print('\nA = '+str(A)+'  a = '+str(round(side_2,3)))
					print('B = '+str(B)+'  b = '+str(round(side_1,3)))
					print('C = '+str(C)+'  c = '+str(round(side_3,3)))

				elif (trig_sas_angleSelect.upper() == 'C'): 
					angle_1 = eval(input('\nenter angle C: '))
					side_2 = eval(input('enter side b: '))
					side_3 = eval(input('enter side a: '))
					angle_1 = radians(angle_1)
					side_1 = sas_side_cos_law(angle_1,side_2,side_3)
					angle_2 = angle_sin_law(angle_1,side_1,side_2)
					C= round(degrees(angle_1),3)
					B= round(degrees(angle_2),3)
					A = 180-(B + C)
					print('\nA = '+str(A)+'  a = '+str(round(side_3,3)))
					print('B = '+str(B)+'  b = '+str(round(side_2,3)))
					print('C = '+str(C)+'  c = '+str(round(side_1,3)))

			elif(trig_shape_input_choice == 2): 
			
				side_1 = eval(input('\nEnter Side \'a\': '))
				side_2 = eval(input('Enter Side \'b\': '))
				side_3 = eval(input('Enter Side \'c\': '))
				angle_1 = sss_angle_cos_law(side_1,side_2,side_3)
				angle_2 = sss_angle_cos_law(side_2,side_1,side_3)
				angle_3 = sss_angle_cos_law(side_3,side_2,side_1)
				A= round(degrees(angle_1),3)
				B= round(degrees(angle_2),3)
				C= round(degrees(angle_3),3)
				print('A = '+str(A)+'  a = '+str(round(side_1,3)))
				print('B = '+str(B)+'  b = '+str(round(side_2,3)))
				print('C = '+str(C)+'  c = '+str(round(side_3,3)))

			elif(trig_shape_input_choice == 3): 
				asa_selection = input('Which side do you have? ')
				asa_selection = asa_selection.lower()
				if asa_selection == 'a':
					side_1 = eval(input('enter side \'a\':'))
					angle_2 = eval(input('Angle B: '))
					angle_3 = eval(input('Angle C: '))
					angle_1 = radians((180-(angle_2+angle_3)))
					angle_2 = radians(angle_2)
					angle_3 = radians(angle_3)
					side_2 = side_sin_law(side_1,angle_1,angle_2)
					side_3 = side_sin_law(side_1,angle_1,angle_3)
					A= round(degrees(angle_1),3)
					B= round(degrees(angle_2),3)
					C= round(degrees(angle_3),3)
					print('A = '+str(A)+'  a = '+str(round(side_1,3)))
					print('B = '+str(B)+'  b = '+str(round(side_2,3)))
					print('C = '+str(C)+'  c = '+str(round(side_3,3)))
	

				elif asa_selection == 'b':
					side_1 = eval(input('enter side \'b\':'))
					angle_2 = eval(input('Angle A: '))
					angle_3 = eval(input('Angle C: '))
					angle_1 = radians((180-(angle_2+angle_3)))
					angle_2 = radians(angle_2)
					angle_3 = radians(angle_3)
					side_2 = side_sin_law(side_1,angle_1,angle_2)
					side_3 = side_sin_law(side_1,angle_1,angle_3)
					B= round(degrees(angle_1),3)
					A= round(degrees(angle_2),3)
					C= round(degrees(angle_3),3)
					print('A = '+str(A)+'  a = '+str(round(side_2,3)))
					print('B = '+str(B)+'  b = '+str(round(side_1,3)))
					print('C = '+str(C)+'  c = '+str(round(side_3,3)))


				elif asa_selection == 'c':
					side_1 = eval(input('enter side \'c\':'))
					angle_2 = eval(input('Angle A: '))
					angle_3 = eval(input('Angle B: '))
					angle_1 = radians((180-(angle_2+angle_3)))
					angle_2 = radians(angle_2)
					angle_3 = radians(angle_3)
					side_2 = side_sin_law(side_1,angle_1,angle_2)
					side_3 = side_sin_law(side_1,angle_1,angle_3)
					C= round(degrees(angle_1),3)
					A= round(degrees(angle_2),3)
					B= round(degrees(angle_3),3)
					print('A = '+str(A)+'  a = '+str(round(side_2,3)))
					print('B = '+str(B)+'  b = '+str(round(side_3,3)))
					print('C = '+str(C)+'  c = '+str(round(side_1,3)))

			elif(trig_shape_input_choice == 4):
				print('Under Construction')
			

			elif(trig_shape_input_choice == 5):
				print('HL.) placeholder: trig_shape_input_choice == 5')

	def x_to_ift():
		x = 1 # gives x a non zero value
		pos_x = [0] * 8 # this line and next three store values generated by loops
		pos_y = [0] * 8
		neg_x = [0] * 8
		neg_y = [0] * 8
		eq = input('Enter Equation: ') # user inputs equation they want the y limits of.

		for z in range(8): # this function drives the x to positive ift, ending value is often more than sufficient
			pos_y[z] = eval(eq)
			pos_x[z] = x
			x= x*20

		x = -1

		for z in range(8):# drives x to neg ift
			neg_y[z] = eval(eq)
			neg_x[z] = x
			x= x*20

		print("x-> pos ift")
		for z in range(8):
			print(str(pos_x[z])+", "+str(pos_y[z]))
		print('\n')
		for z in range(8):
			print(str(neg_x[z])+", "+str(neg_y[z]))

	for z in range(100):# this just keeps it going, I will change this if I often need to run the calculator more than 100 times in a row.
		if (z!=0): print ('\n\n')#this breaks up the different iterations, but not on the first. 
		print("0.) Patch Notes\n1.) Entry Guide\n2.) Simple Function Calculator\n3.) Simple Calculator without Variables\n4.) Instant Velocity\n5.) Continuity Through Point\n6.) Factor a Polynomial\n7.) Greatest Common Factor/Denominator\n8.) Trig Calculator\n9.) Limit as x -> +/- ift")
		function_select = int(input('Selection: '))
		if (function_select == 1): entry_guide()
		elif (function_select == 0): patch_notes()
		elif (function_select == 2): simple_calculator()
		elif (function_select == 3): calc_easy()
		elif (function_select == 4): instant_velocity()
		elif (function_select == 5): slope_at_point()
		elif (function_select == 6): factoring_function()
		elif (function_select == 7): gcd_standalone()
		elif (function_select == 8): trig_calculator()
		elif (function_select == 9): x_to_ift()
		elif (function_select == 999) or (function_select == -999): break #hold over from my procedural programming course
		else: print('Invalid Input')

def window():
	root = Tk()
	root.title("Stimulant Monkey v3")
	width= root.winfo_screenwidth()               
	height= root.winfo_screenheight()               
	root.geometry("%dx%d" % (width, height))

	def simple_calculator():
		def close_wind(event):
			simple_calculator.destroy()
		def run_calculator(event):
			x = eval(input.get())
			output.delete('1.0',END)
			output.insert("end", str(x))

		simple_calculator = Tk()
		simple_calculator.title("Simple Calculator")
		intro = Label(simple_calculator, text = 'Input:')
		output_intro = Label(simple_calculator, text = 'Output:')
		input = Entry(simple_calculator, width = 35, borderwidth = 5)
		output  = Text(simple_calculator, width = 26, borderwidth = 5, height = 1)
		outro = Label(simple_calculator, text = 'Enter/return to run.    ESC to close window.')

		simple_calculator.bind('<Return>', run_calculator)
		simple_calculator.bind('<Escape>', close_wind)
		intro.grid(row = 0, column = 0)
		input.grid(row=0,column=1)
		output_intro.grid(row = 3, column = 0)
		output.grid(row = 3, column = 1)
		outro.grid(row = 4, column = 1)
		simple_calculator.mainloop()

	def equation_calculator():
		def close_wind(event):
			equation_calculator.destroy()
		def run_calculator(event):
			x = eval(x_input.get())
			y = eval(y_input.get())
			output.delete('1.0',END)
			output.insert("end", str(y))

		equation_calculator = Tk()
		equation_calculator.title("equation Calculator")
		x_intro = Label(equation_calculator, text = 'X Input:')
		y_intro = Label(equation_calculator, text = 'String Input:')
		output_intro = Label(equation_calculator, text = 'Output:')
		x_input = Entry(equation_calculator, width = 5, borderwidth = 5)
		y_input = Entry(equation_calculator, width = 35, borderwidth = 5)
		output  = Text(equation_calculator, width = 26, borderwidth = 5, height = 1)
		outro = Label(equation_calculator, text = 'Enter/return to run.    ESC to close window.')
		equation_calculator.bind('<Return>', run_calculator)
		equation_calculator.bind('<Escape>', close_wind)
		x_intro.grid(row = 0, column = 0)
		x_input.grid(row=0,column=1)
		y_intro.grid(row = 1, column = 0)
		y_input.grid(row=1,column=1)
		outro.grid(row=4,column=1)
		output_intro.grid(row = 3, column = 0)
		output.grid(row = 3, column = 1)
		equation_calculator.mainloop()

	def patch_notes():

		def close_wind(event):
			patch_notes.destroy()

		patch_notes = Tk()
		patch_notes.title("Patch Notes")
		L1=Label(patch_notes, text = '1.0 : taught myself how to code python', anchor = "w")
		L2=Label(patch_notes, text = '1.1 : function to determine instant velocity')
		L3=Label(patch_notes, text = '1.2 : added function to determin slope of a line through a single point')
		L4=Label(patch_notes, text = '2.0 : changed the way inputs were added from variable by variable to string equations')
		L5=Label(patch_notes, text = '2.0.1 : made the program mobile compatible through pythonista')
		L6=Label(patch_notes, text = '2.2 : redesigned the layout of the selection menu')
		L7=Label(patch_notes, text = '2.2.1 : went live, patched to be downloaded by colleagues as a .py executable')
		L8=Label(patch_notes, text = '2.2.2 : patched an issue with the way selections were made which crashed the program')
		L9=Label(patch_notes, text = '	 (changed selection = eval(input()) to selection = int(input())')
		L10=Label(patch_notes, text = '2.3 : began rewriting my c++ trig calculator as a single function')
		L11=Label(patch_notes, text = '2.3.1 : minor bug fixes')
		L12=Label(patch_notes, text = '2.3.2 : Finally got the meth monkey to calculate SAS triangles correctly, after many many hours of frustration')
		L13=Label(patch_notes, text = '2.4 : added ASA and SSS triangles. Also added some dependant functions')
		L14=Label(patch_notes, text = '2.4.1 : added some example problems to entry_guide, as well as some notes on trig calculator')
		L15=Label(patch_notes, text = '2.4.2 : fixed issue preventing trig calculator from working')
		L16=Label(patch_notes, text = '3.0 : Began the process of building a GUI, completed \'simple calculator\' \'equation calculator\' and \'patch notes\'')
		L17=Label(patch_notes, text = '3.2 : implemented choice of running the program in terminal or in window.')
		L18=Label(patch_notes, text = '	 ( Allows for cross-platform use, doubles the amount of code. )')
		patch_notes.bind('<Escape>', close_wind)
		L1.pack(side= TOP, anchor="w")
		L2.pack(side= TOP, anchor="w")
		L3.pack(side= TOP, anchor="w")
		L4.pack(side= TOP, anchor="w")
		L5.pack(side= TOP, anchor="w")
		L6.pack(side= TOP, anchor="w")
		L7.pack(side= TOP, anchor="w")
		L8.pack(side= TOP, anchor="w")
		L9.pack(side= TOP, anchor="w")
		L10.pack(side= TOP, anchor="w")
		L11.pack(side= TOP, anchor="w")
		L12.pack(side= TOP, anchor="w")
		L13.pack(side= TOP, anchor="w")
		L14.pack(side= TOP, anchor="w")
		L15.pack(side= TOP, anchor="w")
		L16.pack(side= TOP, anchor="w")
		L17.pack(side= TOP, anchor="w")
		L18.pack(side= TOP, anchor="w")

	def instant_velocity():
		def close_wind(event):
			instant_velocity.destroy()

		def run_instant_velocity(event):
			def x_to_less(x):
				x= x-.0001
				return x
			def x_to_more(x):
				x=x+.0001
				return x
			xP = eval(x_input.get())
			yP = y_input.get()

			x = xP
			y = yP
			x = x_to_less(xP)
			y = eval(y)
			first_x_output.delete('1.0',END)
			first_x_output.insert("end", str(x))
			first_y_output.delete('1.0',END)
			first_y_output.insert("end", str(y))
			y0 = y
			x0 = x

			x = xP
			y = yP
			x = x_to_more(xP)
			y = eval(y)
			second_x_output.delete('1.0',END)
			second_x_output.insert("end", str(x))
			second_y_output.delete('1.0',END)
			second_y_output.insert("end", str(y))
			y1 = y
			x1 = x

			m = (y1-y0)/(x1-x0)
			slope_output.delete('1.0',END)
			slope_output.insert("end", str(m))

		instant_velocity = Tk()
		instant_velocity.title("Instant Velocity")

		x_intro = Label(instant_velocity, text = 'X Input:')
		x_intro.grid(row = 0, column = 0, sticky = 'E')

		x_input = Entry(instant_velocity, width = 5, borderwidth = 5)
		x_input.grid(row=0,column=1,sticky = 'W')

		y_intro = Label(instant_velocity, text = 'String Input:')
		y_intro.grid(row = 1, column = 0, sticky = 'E')

		y_input = Entry(instant_velocity, width = 15, borderwidth = 5)
		y_input.grid(row=1,column=1,sticky = 'W')

		line_space = Label(instant_velocity, text = '	')
		line_space.grid(row = 2, column = 5)

		second_line_space= Label(instant_velocity, text = '')
		second_line_space.grid(row = 5, column = 0)

		first_x_output_intro = Label(instant_velocity, text = 'x1:')
		first_x_output_intro.grid(row = 3, column = 0, sticky = 'E')

		first_x_output  = Text(instant_velocity, width = 12, borderwidth = 5, height = 1)
		first_x_output.grid(row = 3, column = 1, sticky = 'W')

		first_y_output_intro = Label(instant_velocity, text = 'y1:')
		first_y_output_intro.grid(row = 3, column = 2)

		first_y_output  = Text(instant_velocity, width = 12, borderwidth = 5, height = 1)
		first_y_output.grid(row = 3, column = 3)

		second_x_output_intro = Label(instant_velocity, text = 'x2:')
		second_x_output_intro.grid(row = 4, column = 0, sticky = 'E')

		second_x_output  = Text(instant_velocity, width = 12, borderwidth = 5, height = 1)
		second_x_output.grid(row = 4, column = 1, sticky = 'W')

		second_y_output_intro = Label(instant_velocity, text = 'y2:')
		second_y_output_intro.grid(row = 4, column = 2)

		second_y_output  = Text(instant_velocity, width = 12, borderwidth = 5, height = 1)
		second_y_output.grid(row = 4, column = 3)

		slope_output_intro = Label(instant_velocity, text = 'Instant Velocity:')
		slope_output_intro.grid(row = 6, column = 0, sticky = 'E')

		slope_output  = Text(instant_velocity, width = 5, borderwidth = 5, height = 1)
		slope_output.grid(row = 6, column = 1,sticky = 'W')

		instant_velocity.bind('<Return>', run_instant_velocity)
		instant_velocity.bind('<Escape>', close_wind)
		#outro = Label(instant_velocity, text = 'Enter/return to run.    ESC to close window.')
		#outro.grid(row=7,column=0)
		
		
		instant_velocity.mainloop()


	def continuity_point():
		def close_wind(event):
			continuity_point.destroy()

		def run_continuity_point(event):
			def x_to_less(x,v):
				x= x-v
				return x
			def x_to_more(x,v):
				x=x+v
				return x
			xP = eval(x_input.get())
			yP = y_input.get()

			x= xP
			px = xP
			py = eval(yP)
			
			v = .1
			x = xP
			y = yP
			x = x_to_less(xP,v)
			y = eval(str(y))
			first_x_output.delete('1.0',END)
			first_x_output.insert("end", str(x))
			first_y_output.delete('1.0',END)
			first_y_output.insert("end", str(round(y,6)))
			y0 = y
			x0 = x

			x = xP
			y = yP
			v = v/10
			x = x_to_less(xP,v)
			y = eval(str(y))
			second_x_output.delete('1.0',END)
			second_x_output.insert("end", str(x))
			second_y_output.delete('1.0',END)
			second_y_output.insert("end", str(round(y,6)))
			y1 = y
			x1 = x

			
			x = xP
			y = yP
			v = v/10
			x = x_to_less(xP,v)
			y = eval(str(y))
			third_x_output.delete('1.0',END)
			third_x_output.insert("end", str(x))
			third_y_output.delete('1.0',END)
			third_y_output.insert("end", str(round(y,6)))
			y2 = y
			x2 = x

			x = xP
			y = yP
			v = v/10
			x = x_to_less(xP,v)
			y = eval(str(y))
			fourth_x_output.delete('1.0',END)
			fourth_x_output.insert("end", str(x))
			fourth_y_output.delete('1.0',END)
			fourth_y_output.insert("end", str(round(y,6)))
			y3 = y
			x3 = x

			x = xP
			y = yP
			v = v/10
			x = x_to_less(xP,v)
			y = eval(str(y))
			fifth_x_output.delete('1.0',END)
			fifth_x_output.insert("end", str(x))
			fifth_y_output.delete('1.0',END)
			fifth_y_output.insert("end", str(round(y,6)))
			y4 = y
			x4 = x

			v = .1
			x = xP
			y = yP
			x = x_to_more(xP,v)
			y = eval(str(y))
			neg_first_x_output.delete('1.0',END)
			neg_first_x_output.insert("end", str(x))
			neg_first_y_output.delete('1.0',END)
			neg_first_y_output.insert("end", str(round(y,6)))
			y5 = y
			x5 = x

			x = xP
			y = yP
			v = v/10
			x = x_to_more(xP,v)
			y = eval(str(y))
			neg_second_x_output.delete('1.0',END)
			neg_second_x_output.insert("end", str(x))
			neg_second_y_output.delete('1.0',END)
			neg_second_y_output.insert("end", str(round(y,6)))
			y6 = y
			x6 = x

			
			x = xP
			y = yP
			v = v/10
			x = x_to_more(xP,v)
			y = eval(str(y))
			neg_third_x_output.delete('1.0',END)
			neg_third_x_output.insert("end", str(x))
			neg_third_y_output.delete('1.0',END)
			neg_third_y_output.insert("end", str(round(y,6)))
			y7 = y
			x7 = x

			x = xP
			y = yP
			v = v/10
			x = x_to_more(xP,v)
			y = eval(str(y))
			neg_fourth_x_output.delete('1.0',END)
			neg_fourth_x_output.insert("end", str(x))
			neg_fourth_y_output.delete('1.0',END)
			neg_fourth_y_output.insert("end", str(round(y,6)))
			y8 = y
			x8 = x

			x = xP
			y = yP
			v = v/10
			x = x_to_more(xP,v)
			y = eval(str(y))
			neg_fifth_x_output.delete('1.0',END)
			neg_fifth_x_output.insert("end", str(x))
			neg_fifth_y_output.delete('1.0',END)
			neg_fifth_y_output.insert("end", str(round(y,6)))
			y9 = y
			x9 = x

			m0 = (py-y0)/(px-x0)#generating the various slopes using the (y2-y1)/(x2-x1) formula, and assigning them to the slope list
			m1 = (py-y1)/(px-x1) #sometimes python doesnt like the variable py, might change in future
			m2 = (py-y2)/(px-x2)
			m3 = (py-y3)/(px-x3)
			m4 = (y4-py)/(x4-px)
			m5 = (y5-py)/(x5-px)
			m6 = (y6-py)/(x6-px)
			m7 = (y7-py)/(x7-px)

			m = (y9-y4)/(x9-x4)
			slope_output.delete('1.0',END)
			slope_output.insert("end", str(round(m,6)))
			
			first_slope_output.delete('1.0',END)
			first_slope_output.insert("end", str(round(m,6)))

			second_slope_output.delete('1.0',END)
			second_slope_output.insert("end", str(round(m1,6)))

			third_slope_output.delete('1.0',END)
			third_slope_output.insert("end", str(round(m2,6)))

			fourth_slope_output.delete('1.0',END)
			fourth_slope_output.insert("end", str(round(m3,6)))

			fifth_slope_output.delete('1.0',END)
			fifth_slope_output.insert("end", str(round(m4,6)))

			if(abs(y9-y4)<.01): 
				continuity_output.delete('1.0',END)
				continuity_output.insert("end", 'TRUE')
			else : 
				continuity_output.delete('1.0',END)
				continuity_output.insert("end", 'FALSE')
				
		continuity_point = Tk()
		continuity_point.title("Continuity at Point")

		x_intro = Label(continuity_point, text = 'X Input:')
		x_intro.grid(row = 0, column = 0, sticky = 'E')

		x_input = Entry(continuity_point, width = 5, borderwidth = 5)
		x_input.grid(row=0,column=1,sticky = 'W')

		y_intro = Label(continuity_point, text = 'String Input:')
		y_intro.grid(row = 1, column = 0, sticky = 'E')

		y_input = Entry(continuity_point, width = 35, borderwidth = 5)
		y_input.grid(row=1,column=1,sticky = 'W')

		line_space = Label(continuity_point, text = '	')
		line_space.grid(row = 2, column = 5)

		first_x_output_intro = Label(continuity_point, text = 'x1:')
		first_x_output_intro.grid(row = 3, column = 0, sticky = 'E')

		first_x_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		first_x_output.grid(row = 3, column = 1, sticky = 'W')

		first_y_output_intro = Label(continuity_point, text = 'y1:')
		first_y_output_intro.grid(row = 3, column = 2)

		first_y_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		first_y_output.grid(row = 3, column = 3)

		first_slope_output_intro = Label(continuity_point, text = ' slope at point:')
		first_slope_output_intro.grid(row = 3, column = 4, sticky = 'E')

		first_slope_output = Text(continuity_point, width = 5, borderwidth = 5, height = 1)
		first_slope_output.grid(row=3,column=5,sticky = 'W')

		second_x_output_intro = Label(continuity_point, text = 'x2:')
		second_x_output_intro.grid(row = 4, column = 0, sticky = 'E')

		second_x_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		second_x_output.grid(row = 4, column = 1, sticky = 'W')

		second_y_output_intro = Label(continuity_point, text = 'y2:')
		second_y_output_intro.grid(row = 4, column = 2)

		second_y_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		second_y_output.grid(row = 4, column = 3)

		second_slope_output_intro = Label(continuity_point, text = ' slope at point:')
		second_slope_output_intro.grid(row = 4, column = 4, sticky = 'E')

		second_slope_output = Text(continuity_point, width = 5, borderwidth = 5, height = 1)
		second_slope_output.grid(row=4,column=5,sticky = 'W')
		
		third_x_output_intro = Label(continuity_point, text = 'x3:')
		third_x_output_intro.grid(row = 5, column = 0, sticky = 'E')
		
		third_x_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		third_x_output.grid(row = 5, column = 1, sticky = 'W')

		third_y_output_intro = Label(continuity_point, text = 'y3:')
		third_y_output_intro.grid(row = 5, column = 2)

		third_y_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		third_y_output.grid(row = 5, column = 3)
		
		third_slope_output_intro = Label(continuity_point, text = ' slope at point:')
		third_slope_output_intro.grid(row = 5, column = 4, sticky = 'E')

		third_slope_output = Text(continuity_point, width = 5, borderwidth = 5, height = 1)
		third_slope_output.grid(row=5,column=5,sticky = 'W')
		
		fourth_x_output_intro = Label(continuity_point, text = 'x4:')
		fourth_x_output_intro.grid(row = 6, column = 0, sticky = 'E')

		fourth_x_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		fourth_x_output.grid(row = 6, column = 1, sticky = 'W')

		fourth_y_output_intro = Label(continuity_point, text = 'y4:')
		fourth_y_output_intro.grid(row = 6, column = 2)

		fourth_y_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		fourth_y_output.grid(row = 6, column = 3)

		fourth_slope_output_intro = Label(continuity_point, text = ' slope at point:')
		fourth_slope_output_intro.grid(row = 6, column = 4, sticky = 'E')

		fourth_slope_output = Text(continuity_point, width = 5, borderwidth = 5, height = 1)
		fourth_slope_output.grid(row=6,column=5,sticky = 'W')
		
		fifth_x_output_intro = Label(continuity_point, text = 'x5:')
		fifth_x_output_intro.grid(row = 7, column = 0, sticky = 'E')

		fifth_x_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		fifth_x_output.grid(row = 7, column = 1, sticky = 'W')

		fifth_y_output_intro = Label(continuity_point, text = 'y5:')
		fifth_y_output_intro.grid(row = 7, column = 2)

		fifth_y_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		fifth_y_output.grid(row = 7, column = 3)

		fifth_slope_output_intro = Label(continuity_point, text = ' slope at point:')
		fifth_slope_output_intro.grid(row = 7, column = 4, sticky = 'E')

		fifth_slope_output = Text(continuity_point, width = 5, borderwidth = 5, height = 1)
		fifth_slope_output.grid(row=7,column=5,sticky = 'W')

		line_space = Label(continuity_point, text = '	')
		line_space.grid(row = 8, column = 5)
		
		neg_first_x_output_intro = Label(continuity_point, text = 'x1:')
		neg_first_x_output_intro.grid(row = 9, column = 0, sticky = 'E')

		neg_first_x_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		neg_first_x_output.grid(row = 9, column = 1, sticky = 'W')

		neg_first_y_output_intro = Label(continuity_point, text = 'y1:')
		neg_first_y_output_intro.grid(row = 9, column = 2)

		neg_first_y_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		neg_first_y_output.grid(row = 9, column = 3)

		neg_second_x_output_intro = Label(continuity_point, text = 'x2:')
		neg_second_x_output_intro.grid(row = 10, column = 0, sticky = 'E')

		neg_second_x_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		neg_second_x_output.grid(row = 10, column = 1, sticky = 'W')

		neg_second_y_output_intro = Label(continuity_point, text = 'y2:')
		neg_second_y_output_intro.grid(row = 10, column = 2)

		neg_second_y_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		neg_second_y_output.grid(row = 10, column = 3)
		
		neg_third_x_output_intro = Label(continuity_point, text = 'x3:')
		neg_third_x_output_intro.grid(row = 11, column = 0, sticky = 'E')
		
		neg_third_x_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		neg_third_x_output.grid(row = 11, column = 1, sticky = 'W')

		neg_third_y_output_intro = Label(continuity_point, text = 'y3:')
		neg_third_y_output_intro.grid(row = 11, column = 2)

		neg_third_y_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		neg_third_y_output.grid(row = 11, column = 3)
		
		neg_fourth_x_output_intro = Label(continuity_point, text = 'x4:')
		neg_fourth_x_output_intro.grid(row = 12, column = 0, sticky = 'E')

		neg_fourth_x_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		neg_fourth_x_output.grid(row = 12, column = 1, sticky = 'W')

		neg_fourth_y_output_intro = Label(continuity_point, text = 'y4:')
		neg_fourth_y_output_intro.grid(row = 12, column = 2)

		neg_fourth_y_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		neg_fourth_y_output.grid(row = 12, column = 3)
		
		neg_fifth_x_output_intro = Label(continuity_point, text = 'x5:')
		neg_fifth_x_output_intro.grid(row = 13, column = 0, sticky = 'E')

		neg_fifth_x_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		neg_fifth_x_output.grid(row = 13, column = 1, sticky = 'W')

		neg_fifth_y_output_intro = Label(continuity_point, text = 'y5:')
		neg_fifth_y_output_intro.grid(row = 13, column = 2)

		neg_fifth_y_output  = Text(continuity_point, width = 12, borderwidth = 5, height = 1)
		neg_fifth_y_output.grid(row = 13, column = 3)

		neg_line_space = Label(continuity_point, text = '	')
		neg_line_space.grid(row = 14, column = 5)
		
		slope_output_intro = Label(continuity_point, text = 'Instant Velocity:')
		slope_output_intro.grid(row = 15, column = 0, sticky = 'E')

		slope_output  = Text(continuity_point, width = 5, borderwidth = 5, height = 1)
		slope_output.grid(row = 15, column = 1,sticky = 'W')

		continuity_intro = Label(continuity_point, text = 'Continuous: ')
		continuity_intro.grid(row = 16, column = 0, sticky = 'E')

		continuity_output  = Text(continuity_point, width = 5, borderwidth = 5, height = 1)
		continuity_output.grid(row = 16, column = 1,sticky = 'W')
		
		continuity_point.bind('<Return>', run_continuity_point)
		continuity_point.bind('<Escape>', close_wind)
		
		continuity_point.mainloop()

	def trig_calculator():

		def close_wind(event):
			trig_calculator.destroy()

		def SAS():
			def sas_side_cos_law(angle_1,side_2,side_3):
				# I hate that I had to break it up like this but, if the math is written in a single or two strings, it gets all messed up 
				# the meth monkey with the abacus  is not as smart as I thought it was, you have to tell it exactly what to do
				f = cos(angle_1) # I used variables that cannot be confused with a triangle, but they could be anything
				g = side_2*side_3 # I never do more than one type of operation per variable
				h = -2
				j = side_2*side_2
				k = side_3*side_3
				l = (f*g*h) # this one only multiplies variables
				p = j+k+l # this one only adds them
				side_1 = sqrt(p)
				return side_1

			def angle_sin_law(angle_1, side_1, side_2):
				f = sin(angle_1)
				g = side_2*f
				h = g/side_1
				angle_2 = asin(h)
				return angle_2 

			angle_intro = Label(trig_calculator, text = 'Angle: ')
			angle_intro.grid(row = 2, column = 0,sticky = 'W')
			
			
			angles_menu = Entry(trig_calculator, width = 5, borderwidth = 5)
			angles_menu.grid(row = 2, column = 1,sticky = 'E')
			angle_select = 'NULL'
			def angle_select_func(event):
				angles_select = angles_menu.get()
				angles_select = angles_select.upper()
				
				if (angles_select == "A"):
					angle_1_input_intro = Label(trig_calculator, text = 'Angle A: ')
					angle_1_input_intro.grid(row = 3, column = 1, sticky = 'W')
					angle_1_input = Entry(trig_calculator, width = 5, borderwidth = 5)
					angle_1_input.grid(row = 3, column = 2, sticky = 'E')

					side_2_input_intro = Label(trig_calculator, text = 'Side b: ')
					side_2_input_intro.grid(row = 3, column = 3, sticky = 'W')
					side_2_input = Entry(trig_calculator, width = 5, borderwidth = 5)
					side_2_input.grid(row = 3, column = 4, sticky = 'E')

					side_3_input_intro = Label(trig_calculator, text = 'Side c: ')
					side_3_input_intro.grid(row = 3, column = 5, sticky = 'W')
					side_3_input = Entry(trig_calculator, width = 5, borderwidth = 5)
					side_3_input.grid(row = 3, column = 6, sticky = 'E')
					def run_calculator(event):
						angle_1 = eval(angle_1_input.get())
						side_2 = eval(side_2_input.get())
						side_3 = eval(side_3_input.get()) 
						angle_1 = radians(angle_1)
						side_1 = sas_side_cos_law(angle_1,side_2,side_3) 
						angle_2 = angle_sin_law(angle_1,side_1,side_2) 
						a= round(degrees(angle_1),3) 
						b= round(degrees(angle_2),3) 
						c = 180-(a+b)
						
						side_1_output_intro = Label(trig_calculator, text = 'Side a:')
						side_1_output_intro.grid(row = 4, column = 1, sticky = 'W')

						side_1_output = Text(trig_calculator, width = 5, borderwidth = 5, height = 1)
						side_1_output.grid(row = 4, column = 2)

						side_1_output.delete('1.0',END)
						side_1_output.insert("end", str(side_1))

						angle_2_output_intro = Label(trig_calculator, text = 'Angle B:')
						angle_2_output_intro.grid(row = 4, column = 3, sticky = 'W')

						angle_2_output = Text(trig_calculator, width = 5, borderwidth = 5, height = 1)
						angle_2_output.grid(row = 4, column = 4)

						angle_2_output.delete('1.0',END)
						angle_2_output.insert("end", str(degrees(angle_2)))

						angle_3_output_intro = Label(trig_calculator, text = 'Angle B:')
						angle_3_output_intro.grid(row = 4, column = 5, sticky = 'W')

						angle_3_output = Text(trig_calculator, width = 5, borderwidth = 5, height = 1)
						angle_3_output.grid(row = 4, column = 6)

						angle_3_output.delete('1.0',END)
						angle_3_output.insert("end", str(c))

						
					trig_calculator.bind('<Return>', run_calculator)
					trig_calculator.bind('<Escape>', close_wind)

				elif (angles_select == "B"):
					side_2_input_intro = Label(trig_calculator, text = 'Side a: ')
					side_2_input_intro.grid(row = 2, column = 3, sticky = 'W')
					side_2_input = Entry(trig_calculator, width = 5, borderwidth = 5)
					side_2_input.grid(row = 2, column = 4, sticky = 'E')

					side_3_input_intro = Label(trig_calculator, text = 'Side c: ')
					side_3_input_intro.grid(row = 2, column = 5, sticky = 'W')
					side_3_input = Entry(trig_calculator, width = 5, borderwidth = 5)
					side_3_input.grid(row = 2, column = 6, sticky = 'E')

					def run_calculator(event):
						construct_label = Label(trig_calculator, text = ' SAS Under Construction')
						construct_label.grid(row = 10, column = 6)

					trig_calculator.bind('<Return>', run_calculator)
					trig_calculator.bind('<Escape>', close_wind)

				if (angles_select == "C"):
					side_2_input_intro = Label(trig_calculator, text = 'Side a: ')
					side_2_input_intro.grid(row = 2, column = 3, sticky = 'W')
					side_2_input = Entry(trig_calculator, width = 5, borderwidth = 5)
					side_2_input.grid(row = 2, column = 4, sticky = 'E')

					side_3_input_intro = Label(trig_calculator, text = 'Side b: ')
					side_3_input_intro.grid(row = 2, column = 5, sticky = 'W')
					side_3_input = Entry(trig_calculator, width = 5, borderwidth = 5)
					side_3_input.grid(row = 2, column = 6, sticky = 'E')
					def run_calculator(event):
						construct_label = Label(trig_calculator, text = ' SAS Under Construction')
						construct_label.grid(row = 10, column = 6)

					trig_calculator.bind('<Return>', run_calculator)
					trig_calculator.bind('<Escape>', close_wind)
					
			if (angle_select == 'NULL'): 
				trig_calculator.bind('<Return>', angle_select_func)
				
			

		def ASA():
			construct_label = Label(trig_calculator, text = ' ASA Under Construction')
			construct_label.grid(row = 10, column = 6)

		def SSS():
			construct_label = Label(trig_calculator, text = ' SSS Under Construction')
			construct_label.grid(row = 10, column = 6)

		def AAS():
			construct_label = Label(trig_calculator, text = ' AAS Under Construction')
			construct_label.grid(row = 10, column = 6)

		trig_calculator = Tk()
		trig_calculator.title("Trig Calculator")

		SAS_button = Button(trig_calculator, text = 'SAS', padx = 10, pady = 5,borderwidth=5,command=SAS)
		SAS_button.grid(row=0,column=0)

		ASA_button = Button(trig_calculator, text = 'ASA', padx = 10, pady = 5,borderwidth=5,command=ASA)
		ASA_button.grid(row=0,column=1)

		SSS_button = Button(trig_calculator, text = 'SSS', padx = 10, pady = 5,borderwidth=5,command=SSS)
		SSS_button.grid(row=0,column=2)

		AAS_button = Button(trig_calculator, text = 'AAS', padx = 10, pady = 5,borderwidth=5,command=AAS)
		AAS_button.grid(row=0,column=3)

		
		trig_calculator.bind('<Escape>', close_wind)
		
		trig_calculator.mainloop()

	#mainscreen_intro = Label(root, text = '"Stimulant Monkey v3.2\nSean Gunther, 2021\n\"...Look on my Works, ye Mighty, and despair!\"')
	button_0 = Button(root, text='Patch Notes', padx = 10, pady = 5,borderwidth=5,command=patch_notes)
	button_1 = Button(root, text='Simple Calculator', padx = 10, pady = 5,borderwidth=5,command=simple_calculator)
	button_2 = Button(root, text='Equation Calculator', padx = 10, pady = 5,borderwidth=5,command=equation_calculator)
	button_3 = Button(root, text='Instant Velocity', padx = 10, pady = 5,borderwidth=5,command=instant_velocity)
	button_4 = Button(root, text='Continuity at Point', padx = 10, pady = 5,borderwidth=5,command=continuity_point)
	button_5 = Button(root, text='Trig Calculator', padx = 10, pady = 5,borderwidth=5,command=trig_calculator)

	mainscreen_intro_line_1 = Label(root, text = '\nStimulant Monkey v3.2')
	mainscreen_intro_line_2 = Label(root, text = 'Sean Gunther, 2021')
	mainscreen_intro_line_3 = Label(root, text = '\"...Look on my Works, ye Mighty, and despair!\"')
	
	button_0.grid(row = 0,column = 1, sticky = 'w')
	button_1.grid(row = 1,column = 1, sticky = 'w')
	button_2.grid(row = 2,column = 1, sticky = 'w')
	button_3.grid(row = 3,column = 1, sticky = 'w')
	button_4.grid(row = 4,column = 1, sticky = 'w')
	button_5.grid(row = 5,column = 1, sticky = 'w')

	mainscreen_intro_line_1.grid(row = 10,column = 1, sticky = 'w')
	mainscreen_intro_line_2.grid(row = 11,column = 1, sticky = 'w')
	mainscreen_intro_line_3.grid(row = 12,column = 1, sticky = 'w')

	root.mainloop()

def window_terminal_choice():
	print("Stimulant Monkey v3.2\nSean Gunther, 2021\n\"...Look on my Works, ye Mighty, and despair!\"\n")
	print('Would you like to open program in Window or run in terminal?')
	terminal_window_selection = int(input('(1.) Terminal \n(2.) Window\nSelection: '))
	
	if (terminal_window_selection == 1) : 
		terminal()
	elif (terminal_window_selection == 2) : 
		window()
	else : 
		print('Invalid Selection')
		window_terminal_choice()

window_terminal_choice() #it is amusing that the first line of code to be run is the very last line of code