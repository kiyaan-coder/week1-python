#reversing the two digit number
#  number = 45
#  output = 54

number = 65 
ones = number % 10
tens = number / 10
reverseNumber = int(ones*10 + tens)
print (reverseNumber)