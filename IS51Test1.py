

"""
The program is trying to determine which payment option is better.
First program option is 100 dollars per day for 10 days. The second option 1 dollar 
the first day with it being doubled each day for the next 10 days, ie: $2 the second day and $4 the third day. There will be two functions to calculate the pay rate.
Function1 will calculate the amount for the first option, function2 will calculate the second option.

function1 will output 100 * 10 days.
function2 will loop 10 times, with each time, doubling the amount and add the amount to the total.

if the amount is equal, we output to the user "option1 and option2 pays the same"
if option1 is better, we output to the user "option1 is better"
if option2 is better, we output to the user "option2 is better"

"""

"""
# option1
return 100 * 10

# option2
amount = 1
list1=[]
loop 10 times
  add mount to list1
  amount *=2
 sum = add all items in loop
 return sum
# main
 var1 = option1
 var2 = option1

 if var1 = var2
   "Option 1 and Option 2 pays the same"
 if var1 < var2
   "Option 2 is better"
 else
   "Option 1 is better"

main
"""

def option1():
  return 100 * 10

def option2():
 amount = 1
 list1= []
 for i in range(0, 10):
  list1.append(amount)
  amount *=2
 print("list1", list1)
 total = sum(list1)
 return total
   
def main():
 answer = ""
 var1 = option1() 
 var2 = option2() 
 print("from main : var1", var1, "var2", var2)
 if var1 == var2:
   answer = "Option 1 and Option 2 pays the same"
 if var1 < var2:
   answer = "Option 2 is better"
 else:
   answer = "Option 1 is better"
 print(answer)

main()