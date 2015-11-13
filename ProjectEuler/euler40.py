# Champernown constant
# Correct code!!

def champConst():
        champer = "0.1"
        for i in range(2, 2000000):
                champer += str(i)

        d1 = 1				# champer[2]
        d10 = 1				# champer[11]
        d100 = 5			# champer[101]
        d1000 = champer[1001]
        d10000 = champer[10001]		# 10k
        d100000 = champer[100001]	# 100k
        d1000000 = champer[1000001]	# mil

        return int(d1) * int(d10) * int(d100) * int(d1000) * int(d10000) * int(d100000) * int(d1000000)

if __name__ == '__main__':
        print(champConst())
        
