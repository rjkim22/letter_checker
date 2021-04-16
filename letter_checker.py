def letter_checker(string):

	most = " "
	count = 0
	max = 0
	for i in range (len(string)):
		count += 1
		if count > max:
			most = string[i]
			max = count
	print (most,max)

print (letter_checker("twelve"))

def letter_checker2(string,letter):
	count = 0
	for i in range (len(string)):
		if string[i] == letter:
			count += 1

	print (letter,count)

print (letter_checker2("yellow","l"))

def letter_checker3(string):
	max = " "
	maxcount = 0 
	for i in range (len(string)):
		count = 0 
		for j in range (len(string)):
			if string[i] == string[j]:
				count += 1

        	if count > maxcount:
        		maxcount = count 
        		max = string[i]

	print (max,maxcount)

print (letter_checker3("iiiiff"))