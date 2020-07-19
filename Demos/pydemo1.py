def happy():
	print("Happy birthday to you~")
def sing(person):
	happy()
	happy()
	#注意python大小写敏感
	print("Happy birthday,dear",person+"!")
	happy()
def main():
	sing("Mike")
	print()
	sing("Lily")
	print()
	sing("Elmer")
main()