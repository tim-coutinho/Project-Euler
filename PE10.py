def primeSum(upto):
    if upto < 2:
        return None
    primeList = [2]
    for i in range(3, upto):
        for prime in primeList:
            if prime > (int(i ** 0.5) + 1):
                primeList.append(i)
                print(i)
                break
            if i % prime == 0:
                break
        else:
            primeList.append(i)
            print(i)
    return sum(primeList)

print(primeSum(100000))