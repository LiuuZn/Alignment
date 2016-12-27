#coding:utf-8

import os
import os.path
import time
import struct


class BLASTMethods:

    def __findthecode__(self,sequence):
        sequenceArray = list(sequence)
        line = 0
        indicator = 10

        for code in sequenceArray:
            line += (self.__line__(code,indicator))
            indicator -= 1
        return line * 8

    def __line__(self,char,indicator):
        if char == "A":
            return 0
        if char == "T":
            return 4**indicator
        if char == "C":
            return 2*(4**indicator)
        if char == "G":
            return 3*(4**indicator)

    def __check__(self,positions,chromosomeNumber):
        for targetPositionNumber in range(len(positions) - 5):
            if ((long(positions[targetPositionNumber + 5]) - long((positions[targetPositionNumber]))) < 50):
                temsequenceOfInterest.append(positions[targetPositionNumber])
                temsequenceOfInterestLocation.append(chromosomeNumber)

    def __findKeyPoint__(self):
        addstate = True
        for count in range(len(temsequenceOfInterest) - 1):
            if abs(temsequenceOfInterest[count + 1] - temsequenceOfInterest[count]) < 5 and addstate == True:
                sequenceOfInterest.append(temsequenceOfInterest[count])
                sequenceOfInterestLocation.append(temsequenceOfInterestLocation[count])
                addstate = False
            elif temsequenceOfInterest[count +1] - temsequenceOfInterest[count] > 4:
                addstate = True

    def __findIt__(self,location,chr):
        for i in location:
            LibrarySet[chr].Library.seek(long(i),0)
            addition = LibrarySet[chr].Library.readline().strip().strip(",")
            if (addition != ""):
                matchPool[chr].append(addition)

    def __Alignment__(self,aSequence,bSequence):
        firstSequence = []
        secondSequence = []

        for i in aSequence:
           firstSequence.append(i)
           # print (i)

        # print ("hahahah")

        for i in bSequence:
            secondSequence.append(i)

        # constructing two demension array
        alignmentArray = [[0 for i in range(len(firstSequence)+1)]for y in range(len(secondSequence)+1)]
        # print (alignmentArray)

        # give value to arrays

        alignmentArray[0][0] = 0

        # print (alignmentArray)
        # print ("\n")

        for column in range(0,len(secondSequence) + 1):
            for row in range(0,len(firstSequence) + 1):

                a = b = c = 0
                if (column * row != 0):
                    if (firstSequence[row - 1] == secondSequence[column - 1]):
                        # print (firstSequence[row])
                        # print (secondSequence[column])
                        a = alignmentArray[column - 1][row - 1] + 2
                    else:
                        a = alignmentArray[column - 1][row - 1] - 1

                    b = alignmentArray[column - 1][row] - 2
                    c = alignmentArray[column][row - 1] - 2

                    alignmentArray[column][row] = max(a, b, c)


                if (column == 0):
                    alignmentArray[column][row] = (-2 * row)
                if (row == 0):
                    alignmentArray[column][row] = (-2 * column)

        aSequencePosition = alignmentArray[len(bSequence)].index(max(alignmentArray[len(bSequence)]))

        bSequencePosition = len(bSequence)
        reverseAlignedBSequence = []
        reverseAlignedASequence = []
        maximun = max(alignmentArray[bSequencePosition - 1][aSequencePosition],
                      alignmentArray[bSequencePosition - 1][aSequencePosition - 1],
                      alignmentArray[bSequencePosition][aSequencePosition - 1])

        alignmentScore = 0
        while (True):

            maximun = max(alignmentArray[bSequencePosition - 1][aSequencePosition],alignmentArray[bSequencePosition - 1][aSequencePosition - 1],alignmentArray[bSequencePosition][aSequencePosition - 1])
            if (aSequencePosition == 0 or bSequencePosition == 0):
                break

            if alignmentArray[bSequencePosition - 1][aSequencePosition - 1] == alignmentArray[bSequencePosition][aSequencePosition] - 2 and alignmentArray[bSequencePosition - 1][aSequencePosition - 1] == maximun :
                bSequencePosition -= 1
                aSequencePosition -= 1
                reverseAlignedASequence.append(aSequence[aSequencePosition])
                reverseAlignedBSequence.append(bSequence[bSequencePosition])
                alignmentScore += 1
                continue

            if alignmentArray[bSequencePosition - 1][aSequencePosition - 1] == alignmentArray[bSequencePosition][aSequencePosition] + 1 and alignmentArray[bSequencePosition - 1][aSequencePosition - 1] == maximun:
                bSequencePosition -= 1
                aSequencePosition -= 1
                reverseAlignedASequence.append(aSequence[aSequencePosition])
                reverseAlignedBSequence.append(bSequence[bSequencePosition])
                continue

            if alignmentArray[bSequencePosition - 1][aSequencePosition] == alignmentArray[bSequencePosition][aSequencePosition] + 2 and alignmentArray[bSequencePosition - 1][aSequencePosition] == maximun:
                bSequencePosition -= 1
                reverseAlignedASequence.append("-")
                reverseAlignedBSequence.append(bSequence[bSequencePosition])

                continue

            if alignmentArray[bSequencePosition][aSequencePosition - 1] == alignmentArray[bSequencePosition][aSequencePosition] + 2 and alignmentArray[bSequencePosition][aSequencePosition - 1] == maximun:
                aSequencePosition -= 1
                reverseAlignedASequence.append(aSequence[aSequencePosition])
                reverseAlignedBSequence.append("-")

                continue
            if alignmentArray[bSequencePosition - 1][aSequencePosition - 1] == alignmentArray[bSequencePosition][aSequencePosition] - 2 :
                bSequencePosition -= 1
                aSequencePosition -= 1
                reverseAlignedASequence.append(aSequence[aSequencePosition])
                reverseAlignedBSequence.append(bSequence[bSequencePosition])
                alignmentScore += 1
                continue

            if alignmentArray[bSequencePosition - 1][aSequencePosition - 1] == alignmentArray[bSequencePosition][aSequencePosition] + 1:
                bSequencePosition -= 1
                aSequencePosition -= 1
                reverseAlignedASequence.append(aSequence[aSequencePosition])
                reverseAlignedBSequence.append(bSequence[bSequencePosition])
                continue

            if alignmentArray[bSequencePosition - 1][aSequencePosition] == alignmentArray[bSequencePosition][aSequencePosition] + 2:
                bSequencePosition -= 1
                reverseAlignedASequence.append("-")
                reverseAlignedBSequence.append(bSequence[bSequencePosition])
                continue

            if alignmentArray[bSequencePosition][aSequencePosition - 1] == alignmentArray[bSequencePosition][aSequencePosition] + 2:
                aSequencePosition -= 1
                reverseAlignedASequence.append(aSequence[aSequencePosition])
                reverseAlignedBSequence.append("-")
                continue

        alignornot = []
        for i in range(len(reverseAlignedASequence)):
            if (reverseAlignedASequence[i] == reverseAlignedBSequence[i]):
                alignornot.append("|")
            else:
                alignornot.append(" ")

        print ("Blast in %d chromosome" % (int(sequenceOfInterestLocation[number]) + 1))
        print ("".join(reverseAlignedASequence[::-1]))
        print ("".join(alignornot[::-1]))
        print ("".join(reverseAlignedBSequence[::-1]))
        print ("The length of the aligned sequences is ")
        print (len(reverseAlignedASequence))
        print ("The alignment score is ")
        print (alignmentScore)
        print ("The sequence similarity between these two sequences is")
        print (float(alignmentScore)/float(len(reverseAlignedASequence)))


class openLibrary():
    def __openLibrary__(self,number):
        self.Library = open("Library" + str(number))

class openLibraryCount():
    def __openLibraryCount__(self,number):
        self.LibraryCount = open("LibraryCount" + str(number))


if __name__ == "__main__":

    print ("start to time")
    matchPool = [[] for i in range(25)]
    alignPool = [[] for i in range(25)]
    LibrarySet = [[] for chr in range(25)]
    LibraryCountSet = [[] for chr in range(25)]
    for chr in range(25):
        LibrarySet[chr] = openLibrary()
        LibraryCountSet[chr] = openLibraryCount()
        LibrarySet[chr].__openLibrary__(chr)
        LibraryCountSet[chr].__openLibraryCount__(chr)


    Blast = BLASTMethods()
    sequenceOfInterest = []
    temsequenceOfInterest = []
    sequenceOfInterestLocation = []
    temsequenceOfInterestLocation = []

    # blastSequence = "AAAAAAAACTCTACCCCCATTAGTAAAATCCATGTCGCATCCACTTTATTATCAGCTCTTCCCCACAAATATTCATGTGCGACCAAGAAGTATTATCTC"
    blastSequence = "AAAAAAAACTCAATACCCCCATTATGTATTTAAATCCATTGTCGCATCCACGGCTTTATTATCAGTCTCTTCCAAAAACCACAACAATATTTGTGCCTAGACAGAAGTTATTATCTC"
    # blastSequence = "GAAATGGAAGAATGGCTTGGAAATGGGCCCTGTCGACAGTGTGTCACCTGAGCACATTCTCCCAGGGGC"
    # blastSequence = raw_input("Please Enter Blast Sequence")
    print ("Starting to blast")
    time1 = time.time()
    print blastSequence

    blastSequenceWord = []
    for i in range((len(blastSequence) - 10)):
        blastSequenceWord.append("")
        for p in range(11):
            blastSequenceWord[i] = blastSequenceWord[i] + blastSequence[i + p]
        # print blastSequenceWord[i]

    print ("generate input words" + str(time.time() - time1))

    whereToFind = [[] for chr in range(25)]
    for word in blastSequenceWord:
        for chr in range(25):
            LibraryCountSet[chr].LibraryCount.seek(Blast.__findthecode__(word),0)
            # finethecode 的返回值是二进制文件里面的行头的字节数
            location, = struct.unpack("L", LibraryCountSet[chr].LibraryCount.read(8))
            whereToFind[chr].append(location)

    for chr in range(25):
        Blast.__findIt__(whereToFind[chr],chr)
        if len(matchPool[chr]) == 0:
            matchPool[chr].append(str(-1))

    tem = [[] for i in range(25)]

    print ("Blast Sequences costs %.4f seconds" %(time.time() - time1))

    for i in range(25):
        if matchPool[i] != "":
            tem[i] = ",".join(matchPool[i]).split(",")

        for t in range(len(tem[i])):

            alignPool[i].append(int(tem[i][t]))
        alignPool[i].sort()
        Blast.__check__(alignPool[i],i)
    Blast.__findKeyPoint__()

    print ("Use %.4f seconds to find key points" % (time.time() - time1))

    print sequenceOfInterest

    for number in range(len(sequenceOfInterestLocation)):

        file = open("Modifiedchr" + str(sequenceOfInterestLocation[number] + 1))
        file.seek(sequenceOfInterest[number],0)

        tem = ""
        linenumber = 0
        for i in range(11):
            add = file.read(1).upper()
            if add != "\n":
                tem += add
            else:
                i -= 1
                linenumber +=1

        # print blastSequence.find(tem)
        # print linenumber
        file.seek(-blastSequence.find(tem)- 11 -linenumber, 1)
        # file.seek(sequenceOfInterest[number] - 1, 0)
        # print ("the initial point of this alignment is %d" % (file.tell()))
        tem = ""

        i = 0
        tem = file.read(len(blastSequence)).upper()
        # print tem
        # print blastSequence

        Blast.__Alignment__(tem,blastSequence)




    print ("finish in %.4f seconds"%(time.time() - time1))
    exit()



