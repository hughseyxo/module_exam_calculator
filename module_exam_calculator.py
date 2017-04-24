#!usr/bin/env python

#functions
def ca_worth_calc(ca_worth):
	ca_worth = raw_input("Please enter the CA worth: ")
	ca_worth = float(ca_worth)/100
	return ca_worth
	
def exam_worth_calc(exam_worth, ca_worth):
	exam_worth = 100 - ca_worth
	exam_worth = float(exam_worth)/100
	return exam_worth

def ca_percent_calc(ca_percent):	
	ca_percent = raw_input("Please enter your CA result: ")
	ca_percent = float(ca_percent)/100
	return ca_percent

def final_calc(ca_worth, ca_percent, exam_worth, final):
	final = (0.4-(ca_worth*ca_percent))/exam_worth
	final = final * 100
	return final
	
#variable set
ca_worth = 0
ca_percent = 0
exam_worth = 0
final = 0

#main
ca_worth = ca_worth_calc(ca_worth)

exam_worth = exam_worth_calc(exam_worth, ca_worth)

ca_percent = ca_percent_calc(ca_percent)

	
if (ca_worth*ca_percent) >= 0.4:
	print "You have already passed this module through CA"
	
else:
	final = final_calc(ca_worth, ca_percent, exam_worth, final)
	print "You will need " + str(round(final, 2)) + "% to pass."
