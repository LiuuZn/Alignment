if __name__ == "__main__":

    print "start to adjust"
    for chr in range(25):
        content = []
        modifiedcontent = ""
        file = open("/3_disk/liuxin/hg19/chr" + str(chr + 1) + ".fa","r")
        print file.name
        print file.readline()

        while 1:
            line = file.readline()
            modifiedcontent = modifiedcontent + line.strip()
            if not line:
                break
            pass

        newfile = open("/3_disk/liuxin/newblast/Modifiedchr"+ str(chr + 1),"a+")
        newfile.write(modifiedcontent)
        newfile.close()
       
