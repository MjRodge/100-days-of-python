#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to the tip calc.")
bill_total = float(input("what was the total bill? $"))
tip_percentage = int(input("what percentage will you tip? "))
guests = int(input("how many to split between? "))
payment_per_person = (bill_total/guests)*(tip_percentage+100)/100
currency_formatted_payment = "{:.2f}".format(round(payment_per_person, 2))
print(f"each person owes: ${currency_formatted_payment}")