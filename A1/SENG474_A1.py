from collections import Counter
import os

trainlabelsFileName = 'trainlabels.txt'

accuracyList = []

def naiveBayes(mostCommonNum,trainDataFileName,trainLabelFileName,testDataFileName,testLabelFileName):
	# Training starts here
	sayingsFile = open("sFile.txt","a")
	futureFile = open("fFile.txt","a")

	# mostCommonNum = 6

	with open(trainDataFileName) as file:
		for num, line in enumerate(file,1):
			if num < 162:
				futureFile.write(line + "\n")
			else:
				sayingsFile.write(line + "\n")
		
		with open('sFile.txt') as sayingsFile:
			sayingsCollection = Counter(sayingsFile.read().split())
		with open('fFile.txt') as futureFile:
			futureCollection = Counter(futureFile.read().split())

	with open(trainDataFileName) as file:		
		data = file.read()
		
	sayingsFile.close()
	os.remove("sFile.txt")
	futureFile.close()
	os.remove("fFile.txt")
	file.close()

	# Now for the big leagues, testing starts here
	with open(testDataFileName) as file:
		content = file.readlines()

	for line in content:
		sayingsProbability = -1
		futureProbability = -1
		uniqueSentenceVocabulary = []
		for word, count in sayingsCollection.most_common(mostCommonNum):
			if word in line.split() and word not in uniqueSentenceVocabulary:
				uniqueSentenceVocabulary.append(word)
				if sayingsProbability == -1:
					sayingsProbability = (count/data.count(word))
				else:
					sayingsProbability *= (count/data.count(word))
			
		for word, count in futureCollection.most_common(mostCommonNum):
			if word in line.split() and word not in uniqueSentenceVocabulary:
				uniqueSentenceVocabulary.append(word)
				if futureProbability == -1:
					futureProbability = (count/data.count(word))
				else:
					futureProbability *= (count/data.count(word))

		if sayingsProbability == -1:
			sayingsProbability = 0
		else:
			sayingsProbability *= (170/322)
		
		if futureProbability == -1:
			futureProbability = 0
		else:
			futureProbability *= (152/322)

		with open('labels.txt','a') as labels:
			if futureProbability > sayingsProbability:
				labels.write("1\n")
			else:
				labels.write("0\n")

	# Now it's time to check what percentage we got right
	labelfile = open('labels.txt')
	labelsData = labelfile.readlines()
	testlabelfile = open(testLabelFileName)

	accuracy = 0
	count = 0

	for result in labelsData:
		answer = testlabelfile.readline()
		if result == answer:
			accuracy += 1
		count += 1

	# print(str((int) ((accuracy/len(content))*100)) + "%" + " accurate at position " + str(mostCommonNum))
	accuracyList.append((int) ((accuracy/len(content))*100))

	labelfile.close()
	os.remove("labels.txt")
	testlabelfile.close()

trainDataFileName = input("Please enter the filename of the training data file: ")
trainLabelsFileName = input("Please enter the filename of the training labels: ")
testDataFileName = input("Please enter the filename of the test data file: ")
testLabelsFileName = input("Please enter the filename of the labels data file: ")

print("Computing accuracy ...")
for x in range(1,20):
	naiveBayes(38*x*x,trainDataFileName,trainLabelsFileName,testDataFileName,testLabelsFileName)

print(str(max(accuracyList)) + "%" + " is the highest accuracy.")