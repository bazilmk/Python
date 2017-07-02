'''
Author: Bazil Muzaffar Kotriwala
Timestamp: 18-May-2017 3:43 PM
'''

def generate_graycode(n):
    '''
    This function generates the graycode list for any n elements between 2 - 10 inclusive provided by the user
    :param n: number of elements
    :precondition: The number of elements must be inputted by the user
    :postcondition: The graycode list is constructed for the total number of elements inputted by the user
    :return: The graycode list is returned
    :complexity: Best Case = Worst Case = O(n^2), where n is the number of elements
    '''

    graycode_list = [0, 1]
    i = 0
    while i < n-1:
        for k in range(len(graycode_list) - 1, -1, -1):
            graycode_list.append(graycode_list[k] << 1 | 1)
        for j in range(len(graycode_list)//2):
            graycode_list[j] = (graycode_list[j] << 1)
        i += 1
    return graycode_list

def generate_subsets(graycode_list):
    '''
    This function generates all the subsets of n elements i.e. n elements has 2^n subsets
    :param: Graycode list
    :precondition: The graycode list must have already been generated
    :postcondition: All the subsets of the n elements provided by the user are written to the output file as they are generated
    :complexity: Best Case = Worst Case = O(2^n), where n is the number of elements
    '''

    file = open('outputTask2.txt', 'w')
    i = 0
    while i < len(graycode_list):
        file.write('subset' + '\t' + str(i+1) + ': ')
        position = 0
        file.write('{')
        while graycode_list[i] != 0:
            bit = graycode_list[i] & 1
            if bit == 1:
                file.write(chr(97 + position))
                if graycode_list[i] > 1:
                    file.write(',')
            elif bit == 0:
                pass
            position += 1
            graycode_list[i] >>= 1
        file.write('}')
        if i != len(graycode_list)-1:
            file.write(',' + '\n')
        i += 1

if __name__ == '__main__':
    n = int(input('Enter the number of elements: '))
    if 2 <= n <= 10:
        graycode_list = generate_graycode(n)
        generate_subsets(graycode_list)
    else:
        raise ValueError