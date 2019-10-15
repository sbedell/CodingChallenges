# CORRECT - Takes nearly 3 minutes to run.

smallest = 0	# 2520
num = 100000	# start high, tested thru 10 mil and didn't find anything

while True:
	flag = 1
	for n in range(1, 21):
		if (num % n != 0):			
			flag = 0
			break
	if flag == 1:
		smallest = num
		break	
	num = num + 1
	#if (num % 15 == 0):print num

if __name__ == '__main__':
	print(smallest)
