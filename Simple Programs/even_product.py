target = 65
L = [2,5,4,1,7,2,4]

def even_product(target, L):
    product = 1
    result = False
    for i in range(len(L)):
        if L[i] % 2 == 0:
            product = product * L[i]

    if product > target:
        result = True

    return result

print(even_product(target, L))