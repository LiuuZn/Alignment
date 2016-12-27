import struct

class method:
    def __fuck__(self, filepath2, number):

        Lib = open(filepath2 + str(number), "rw+")

        LibCount = open("LibraryCount" + str(number), "a+")
        length = 0

        for lines in Lib:
            LibCount.write(struct.pack("L",length))
            length += len(lines)

if __name__ == "__main__":
    # filename = input("filename")
    method = method()
    for i in range(25):
        print i
        method.__fuck__("Library",i)

    exit()
