    def cypher(userkaput):
        userkaput=list(userkaput)
        for i in userkaput:
            numbervali=ord(i)
            nunumvali=numbervali+valienter
            charvali=chr(i)
            idex=userkaput.index(i)
            userkaput.insert(idex+1, charvali)
