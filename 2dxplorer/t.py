f = open("save.txt", "r")
stri = f.read()
lb = list()
lb = [int(i) for i in stri.split()]
lb.sort(reverse=True)
print(str(lb[5]))