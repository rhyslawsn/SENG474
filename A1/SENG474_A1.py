from collections import Counter
import os

sayingsFile = open("sFile.txt","a")
futureFile = open("fFile.txt","a")

with open('traindata.txt') as file:
	for num, line in enumerate(file,1):
		if num < 162:
			sayingsFile.write(line + "\n")
		else:
			futureFile.write(line + "\n")
	
	with open('sFile.txt') as sayingsFile:
		sayingsCollection = Counter(sayingsFile.read().split())
	with open('fFile.txt') as futureFile:
		futureCollection = Counter(futureFile.read().split())

with open('traindata.txt') as file:		
	print("The top 5 common words in sayingsCollection are:")
	data = file.read()
	for word, count in sayingsCollection.most_common(5):
		print("\t" + word + " %d/%d" % (count, data.count(word)))
		
	print("\nThe top 5 common words in futureCollection are:")
	for word, count in futureCollection.most_common(5):
		print("\t" + word + "\t%d/%d" % (count, data.count(word)))
sayingsFile.close()
os.remove("sFile.txt")
futureFile.close()
os.remove("fFile.txt")
file.close()