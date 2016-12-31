import PIL
from PIL import Image
import time

class NewClusterMethod():
    # ChimeraClustering


    def __generatesimilarity__(self,cluster,originalSimilarityMatrix):
        computingSequenceNumber = 0
        while (computingSequenceNumber < len(cluster) - 1):
            t = 1
            while (t <= len(cluster) - 1 - computingSequenceNumber):
                # print("Aligning %s and %s" % (cluster[computingSequenceNumber], cluster[computingSequenceNumber + t]))
                originalSimilarityMatrix[computingSequenceNumber][computingSequenceNumber + t] = (self.__Alignment__(cluster[computingSequenceNumber], cluster[computingSequenceNumber + t]))
                originalSimilarityMatrix[computingSequenceNumber + t][computingSequenceNumber] = originalSimilarityMatrix[computingSequenceNumber][computingSequenceNumber + t]
                t += 1
            computingSequenceNumber += 1

    def __secondclustering__(self,cluster):
        print ("Process second clustering")

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


                # print(alignmentArray[column][row])

        # for column in range(0,secondSequence.__len__() +1):
            # [::-1]:
            # print (alignmentArray[column])
            # print (column)

        aSequencePosition = alignmentArray[len(bSequence)].index(max(alignmentArray[len(bSequence)]))

        bSequencePosition = len(bSequence)
        reverseAlignedBSequence = []
        reverseAlignedASequence = []
        maximun = max(alignmentArray[bSequencePosition - 1][aSequencePosition],
                      alignmentArray[bSequencePosition - 1][aSequencePosition - 1],
                      alignmentArray[bSequencePosition][aSequencePosition - 1])
        # print ("The sequence similarity is")
        # print (maximun/(2*max(len(aSequence),len(bSequence))))
        alignmentScore = 0
        while (True):
            # calculate the maximun number
            # print (alignmentArray[bSequencePosition][aSequencePosition])
            # print (aSequencePosition)
            # print (bSequencePosition)
            # print ()
            maximun = max(alignmentArray[bSequencePosition - 1][aSequencePosition],alignmentArray[bSequencePosition - 1][aSequencePosition - 1],alignmentArray[bSequencePosition][aSequencePosition - 1])
            if (aSequencePosition == 0 or bSequencePosition == 0):
                break

            # print (maximun)
            # need to be rewrite

            if alignmentArray[bSequencePosition - 1][aSequencePosition - 1] == alignmentArray[bSequencePosition][aSequencePosition] - 2 and alignmentArray[bSequencePosition - 1][aSequencePosition - 1] == maximun :
                bSequencePosition -= 1
                aSequencePosition -= 1
                # print(aSequencePosition)
                # print(bSequencePosition)
                # print()
                reverseAlignedASequence.append(aSequence[aSequencePosition])
                reverseAlignedBSequence.append(bSequence[bSequencePosition])
                alignmentScore += 1
                continue

            if alignmentArray[bSequencePosition - 1][aSequencePosition - 1] == alignmentArray[bSequencePosition][aSequencePosition] + 1 and alignmentArray[bSequencePosition - 1][aSequencePosition - 1] == maximun:
                bSequencePosition -= 1
                aSequencePosition -= 1
                # print(aSequencePosition)
                # print(bSequencePosition)
                # print()
                reverseAlignedASequence.append(aSequence[aSequencePosition])
                reverseAlignedBSequence.append(bSequence[bSequencePosition])
                continue

            if alignmentArray[bSequencePosition - 1][aSequencePosition] == alignmentArray[bSequencePosition][aSequencePosition] + 2 and alignmentArray[bSequencePosition - 1][aSequencePosition] == maximun:
                bSequencePosition -= 1
                # print(aSequencePosition)
                # print(bSequencePosition)
                # print()
                reverseAlignedASequence.append("-")
                reverseAlignedBSequence.append(bSequence[bSequencePosition])

                continue

            if alignmentArray[bSequencePosition][aSequencePosition - 1] == alignmentArray[bSequencePosition][aSequencePosition] + 2 and alignmentArray[bSequencePosition][aSequencePosition - 1] == maximun:
                aSequencePosition -= 1
                # print(aSequencePosition)
                # print(bSequencePosition)
                # print()
                reverseAlignedASequence.append(aSequence[aSequencePosition])
                reverseAlignedBSequence.append("-")

                continue
            if alignmentArray[bSequencePosition - 1][aSequencePosition - 1] == alignmentArray[bSequencePosition][aSequencePosition] - 2 :
                bSequencePosition -= 1
                aSequencePosition -= 1
                # print(aSequencePosition)
                # print(bSequencePosition)
                # print()
                reverseAlignedASequence.append(aSequence[aSequencePosition])
                reverseAlignedBSequence.append(bSequence[bSequencePosition])
                alignmentScore += 1
                continue

            if alignmentArray[bSequencePosition - 1][aSequencePosition - 1] == alignmentArray[bSequencePosition][aSequencePosition] + 1:
                bSequencePosition -= 1
                aSequencePosition -= 1
                # print(aSequencePosition)
                # print(bSequencePosition)
                # print()
                reverseAlignedASequence.append(aSequence[aSequencePosition])
                reverseAlignedBSequence.append(bSequence[bSequencePosition])
                continue

            if alignmentArray[bSequencePosition - 1][aSequencePosition] == alignmentArray[bSequencePosition][aSequencePosition] + 2:
                bSequencePosition -= 1
                # print(aSequencePosition)
                # print(bSequencePosition)
                # print()
                reverseAlignedASequence.append("-")
                reverseAlignedBSequence.append(bSequence[bSequencePosition])
                continue

            if alignmentArray[bSequencePosition][aSequencePosition - 1] == alignmentArray[bSequencePosition][aSequencePosition] + 2:
                aSequencePosition -= 1
                # print(aSequencePosition)
                # print(bSequencePosition)
                # print()
                reverseAlignedASequence.append(aSequence[aSequencePosition])
                reverseAlignedBSequence.append("-")
                continue

        alignornot = []
        for i in range(len(reverseAlignedASequence)):
            if (reverseAlignedASequence[i] == reverseAlignedBSequence[i]):
                alignornot.append("|")
            else:
                alignornot.append(" ")
        inte_reverseAlignedASequence = []
        #
        # print ("".join(reverseAlignedASequence[::-1]))
        # print ("".join(alignornot[::-1]))
        # print ("".join(reverseAlignedBSequence[::-1]))
        # print ("The length of the aligned sequences is ")
        # print (len(reverseAlignedASequence))
        # print ("The alignment score is ")
        # print (alignmentScore)
        # print ("The sequence similarity between these two sequences is")
        return (alignmentScore/len(reverseAlignedASequence))

if __name__ == "__main__":
    time1 = time.time()
    cluster = []
    division = 10
    analysis = NewClusterMethod()
    sequenceName = []
    file = open("complexSequence")
    print ("Sucessfully open the sequence file")
    sequence = file.readlines()
    for lines in sequence:
        if lines[0] == ">":
            sequenceName.append(lines.strip())
        if lines[0] != ">":
            cluster.append(lines)

    originalSimilarityMatrix = [[] for i in range(len(cluster))]
    similarityMatrix = [[] for i in range(len(cluster))]
    for elements in range(len(cluster)):
        for element in range(len(cluster)):
            originalSimilarityMatrix[elements].append(0)
            similarityMatrix[elements].append(0)
    print ("Begin to clustering")

    print("Process first clustering")
    analysis.__generatesimilarity__(cluster, originalSimilarityMatrix)
    analysis.__generatesimilarity__(cluster,similarityMatrix)

    firstClusterThreshold = 9

    while(len(similarityMatrix) >= firstClusterThreshold):
        maximunSimilarity = 0
        for lines in range(len(similarityMatrix)):
            # print(similarityMatrix[lines])
            for elements in range(len(similarityMatrix[lines])):
                if (similarityMatrix[lines][elements] >= maximunSimilarity):
                    maximunSimilarity = similarityMatrix[lines][elements]
                    maxline = lines
                    maxelement = elements
        # print(sequenceName)
        # print(maxline)
        # print(maxelement)
        sequenceName.append("(" + sequenceName[min(maxline, maxelement)] + "," + sequenceName[max(maxline, maxelement)] + ")")
        similarityMatrix.append([])
        for i in range(len(similarityMatrix)-1):
            similarityMatrix[-1].append((similarityMatrix[i][maxelement] + similarityMatrix[i][maxline]) / 2)
        for i in range(len(similarityMatrix)):
            # print(i)
            del similarityMatrix[i][max(maxline,maxelement)]
            del similarityMatrix[i][min(maxline,maxelement)]
        del similarityMatrix[max(maxline,maxelement)]
        del similarityMatrix[min(maxline,maxelement)]
        del sequenceName[max(maxline,maxelement)]
        del sequenceName[min(maxline,maxelement)]
        for i in range(len(similarityMatrix) - 1):
            similarityMatrix[i].append(similarityMatrix[-1][i])
        similarityMatrix[len(similarityMatrix)-1].append(0)


    while (len(similarityMatrix) >= 2):
    # keep slustering until less then 2 elements
        maximunSimilarity = 0
        for i in range(len(similarityMatrix) - 1 ):
        # pair every two elements and make a matrix

            for qz in range(i + 1,len(sequenceName)):
                cluster1 = str(sequenceName[i]).replace("(","").replace(")","").replace(">Sequence","").split(",")
                cluster2 = str(sequenceName[qz]).replace("(","").replace(")","").replace(">Sequence","").split(",")
                for m in cluster1:
                    for n in cluster2:
                        similarity = originalSimilarityMatrix[int(n)-1][int(m)-1]
                        if (similarity >= maximunSimilarity):
                            maximunSimilarity = similarity
                            maxline = i
                            maxelement = qz
        sequenceName.append(
            "(" + sequenceName[min(maxline, maxelement)] + "," + sequenceName[max(maxline, maxelement)] + ")")
        similarityMatrix.append([])
        for j in range(len(similarityMatrix) - 1):
            similarityMatrix[-1].append((similarityMatrix[j][maxelement] + similarityMatrix[j][maxline]) / 2)
        for k in range(len(similarityMatrix)):
            # print(i)
            del similarityMatrix[k][max(maxline, maxelement)]
            del similarityMatrix[k][min(maxline, maxelement)]
        del similarityMatrix[max(maxline, maxelement)]
        del similarityMatrix[min(maxline, maxelement)]
        del sequenceName[max(maxline, maxelement)]
        del sequenceName[min(maxline, maxelement)]
        for l in range(len(similarityMatrix) - 1):
            similarityMatrix[l].append(similarityMatrix[-1][l])
        similarityMatrix[len(similarityMatrix) - 1].append(0)



    print(sequenceName)
    print (time.time() - time1)
