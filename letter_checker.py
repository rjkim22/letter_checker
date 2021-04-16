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
	string = string.lower()			#Make all of the characters lowercase
	maxcount = 0					
	maxchar = ""
	sent = ""
	string = string.replace(" ","")		#Remove all the spaces in the sentence
	while string != "":					#Loop the for loop until we have no more characters
		for i in range (len(string)):	#Loop through each character in the string 
			if string[i].isalpha():		#Make sure the character chosen is an alphabet and not a blank
				if string.count(string[i]) > maxcount:		#Check which character is most common
					maxcount = string.count(string[i]) 
					maxchar = string[i]
				elif string.count(string[i]) == maxcount:	#Put in alphabetical order if there is the same amount of one character
					if string[i]<maxchar:
						maxchar = string[i]

		sent += maxchar		#Append the current most frequent character to the sentence
		string = string.replace (maxchar, "")	#Replace the current most frequent character with a blank ; basicaly remove the current most frequent letter to make room for the next one
		maxcount = 0		#Reset the max count so that we can start checking for the next most freqeuent character

	return (sent)


print (letter_checker4("I am a boy"))
