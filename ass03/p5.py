"""Write a program in python to take a sentence as input. 
Now count occurrence of ‘The’ word in given sentence."""

string=input("Enter the Sentence: ")
str=string.lower()
a=str.split()
word_count={}
for the in a:
	if the in word_count:
		word_count[the]+=1
	else:
		word_count[the]=0
print(word_count[the])