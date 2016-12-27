import gc
class DataBaseGenerator :

    def __findthecode__(self,sequence):
        sequenceArray = list(sequence)
        line = 0
        indicator = 10

        for code in sequenceArray:
            line += (self.__line__(code,indicator))
            indicator -= 1
        return line

    def __line__(self,char,indicator):
        if char == "A":
            return 0
        if char == "T":
            return 4**indicator
        if char == "C":
            return 2*(4**indicator)
        if char == "G":
            return 3*(4**indicator)

    def __auto__(self,filepath1,filepath2):

        sequenceFile = open(filepath1, "r")
        Lib = open(filepath2,"a+")


        print ("The name of the sequence is %s" % (filepath1))
        sequence = ""
        sequenceindex = []
        nonModifiedSequence = sequenceFile.readline()
        sequenceFile.close()

        indicator = 0
        for code in nonModifiedSequence:
            if (code.upper() == "A" or code.upper() == "T" or code.upper() == "C" or code.upper() == "G"):
                sequence = sequence + code.upper()
                sequenceindex.append(indicator)
                indicator += 1
            else:
                indicator += 1

        nonModifiedSequence = 0
        indicator = 0
        Libs = ["" for o in range(4**11)]


        for code in range((len(sequence) - 11)):
            temporarySequence = []
            i = 0
            for i in range(11):
                temporarySequence.append(sequence[indicator + i])



            whichline = self.__findthecode__(temporarySequence)
            Libs[whichline] = str(Libs[whichline]).strip()
            Libs[whichline] = Libs[whichline] + ("," + str(sequenceindex[indicator]+1))

            indicator += 1

        for array in Libs:
            Lib.writelines(array)
            Lib.writelines("\n")

if __name__ == "__main__":
    generateWord = DataBaseGenerator()
    test = []
    a = 0

    for number in range(25) :
        print ("Start to analyze %d chromosome" % (number))
        test.append(generateWord.__auto__("Modifiedchr" + str(number + a + 1), "Library" + str(number + a)))
        print ("Finish Setting in %d chromosome" % (number + a))

    


    gc.collect()
    exit()
