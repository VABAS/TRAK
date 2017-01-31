from time import time
def jono(n):
    if n == 0 or n == 1:
        return "a"
    else:
        return jono(n-2)+jono(n-1)

for i in range(80):
    prev = time()
    print str(i) + "\t" + str(len(jono(i))) + "\t\t" + str(round(time() - prev,1)) 
