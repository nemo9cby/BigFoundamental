import random

if __name__ == '__main__':

    for i in xrange(5,6):
        print i

    a = random.sample(range(1, 100), 5)

    print a

    for j in xrange(1,len(a)):
        key = a[j]
        i =  j - 1
        while i >= 0 and a[i] < key:
            a[i + 1] = a [i]
            i = i - 1
        a[i+1] = key
    print a