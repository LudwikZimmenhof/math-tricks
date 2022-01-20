from datetime import datetime


year = datetime.now().year


def number():
	global num
	num=0
	while num<2 or num>10:
		try:
			num=int(input("Give number between 2 and 10: "))
			break
		except ValueError:
			print("Thats not even a number")
			number()

number()

num2=num*2

num3=num2+5

num4=num3*50

num13=int(year)-250

def cel():
	celebrated=input("Have you already celebrated birthday? (Y/N): ").upper()
	global num5
	if celebrated=='Y':
		num5=num4+num13
	elif celebrated=='N':
		num5=num4+num13-1
	else:
		print("Type 'Y'(Yes) or 'N'(No)")
		cel()

cel()

yearOfBirth=int(input("What is your year of birth?: "))

num6=num5-yearOfBirth


num9=[int(i) for i in str(num6)]

num7=num9[0]

print("You have choosen " + str(num7))

num8=num9[1::]

num11=num8[0]

num12=num8[1]

num10=num11*10+num12

print("You are " + str(num10) + " years old")
