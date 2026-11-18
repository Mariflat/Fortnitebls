def product(a, b):
    if a > b:
        a,b = b,a
    p=1
    for i in range(a, b+1):
        p = i
    return p
print(product(1, 5))

def max_of_list(list):
    max = list[0]
    for d in list:
        if d > max:
            max = d
    return max
    #list.sort(reverse = True)
    #return list[0]
print(max_of_list([1,4,3,10,5]))

def sum_and_avg(list):
    sum = 0
    for e in list:
        sum += e
    return (f"sum = {sum}"
            f"\navg = {sum / len(list)}")
print(sum_and_avg([11, 4, 72, 3, 10, 5, 5, 7, 80]))

def pos_neg_even_odd(list):
    posN = 0
    negN = 0
    evenN = 0
    oddN = 0
    for pos in list:
        if pos > 0:
            posN += 1
    for neg in list:
        if neg < 0:
            negN += 1
    for even in list:
        if even%2 == 0:
            evenN += 1
    for odd in list:
        if odd%2 != 0:
            oddN += 1

    return (f"positives: {posN}"
            f"\nnegatives: {negN}"
            f"\nevens: {evenN}"
            f"\nodds: {oddN}")
print(pos_neg_even_odd([11, -4, 66, 67, 83, -72, 43, 0]))

def reverse(list):
    newList = []
    for f in list:
        newList.insert(0, f)
    return newList
print(reverse([11, -4, 66, 67, 83, -72, 43, 0]))