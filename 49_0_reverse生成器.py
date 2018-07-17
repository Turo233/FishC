def myRev(data):
        index = len(data)
        while index:
                index -= 1
                yield data[index]
