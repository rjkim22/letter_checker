def letter_checker(string):

	most = " "
	count = 0
	max = 0
	for i in range (len(string)):
		count += 1
		if count > max:
			most = string[i]
			max = count
	return (most,max)

print (letter_checker("twelve"))

def letter_checker2(string,letter):
	count = 0
	for i in range (len(string)):
		if string[i] == letter:
			count += 1

	return (letter,count)

print (letter_checker2("yellow","l"))

def letter_checker3(string):
	maxchr = " "
	maxcount = 0 
	for i in range (len(string)):
		count = 0 
		for j in range (len(string)):
			if string[i] == string[j]:
				count += 1

        	if count > maxcount:
        		maxcount = count 
        		maxchr = string[i]

	return (maxchr,maxcount)

print (letter_checker3("iiiiff"))

def letter_checker4(string):
	maxcount = 0
	maxchar = " "
	for i in range (len(string)):
		if string.count(string[i]) > maxcount:
			maxcount = string.count(string[i]) 
			maxchar = string[i]

	return (maxchar,maxcount)


print (letter_checker4("apple"))