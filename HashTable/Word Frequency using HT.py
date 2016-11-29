'''
Created By: Bazil Muzaffar Kotriwala
Student ID: 27012336
'''

import string

class QuadraticProbeHashTable:

    def __init__(self, size, b):

        '''
        When an object is created using the QuadraticProbeHashTable, a table with linear probing of a default size is created.
        :param: Size of the table (size is a prime number)
        :precondition: None
        :postcondition: None
        :complexity: Best Case = Worst Case = O(1), constant time complexity, since there are single statements being executed.
        '''

        self.array = [None] * size
        self.table_size = size
        self.count = 0
        self.b = b
        self.collision_counter = 0
        self.maximum_frequency = 0

    def hash(self, key):
        '''
        This function is the universal hash function which calculates the hash value for the given key.
        :param: The keys in the hash table
        :precondition: None
        :postcondition: None
        :complexity: Best Case = Worst Case = O(n), where n is the length of hash table
        '''

        value = 0
        a = 31415
        b = self.b
        for i in range(len(key)):
            value = (ord(key[i]) + a * value) % self.table_size
            a = a * b % (self.table_size - 1)
        return value

    def __setitem__(self, key, value):
        '''
        This function puts the value corresponding to the key at the position which is empty in the Hash Table or
        updates a value if there is something in the position with the same key or finds a new empty spot if there is
        already something there with a different key. (Uses linear search)
        :param: Key and its corresponding value
        :precondition: None
        :postcondition: None
        :complexity: Best Case O(1), constant time complexity, if the code does not enter the for loop and raises exception
                     Worst Case O(n), linear time complexity, where n is the size of the hash table.
        '''

        position = self.hash(key)
        fixed_position = position
        copyPos = position
        if self.count == self.table_size:
            raise Exception('The Hash Table is full. ')
        if self.array[position] is not None and self.array[position][0] != key:
            self.collision_counter += 1
        for i in range(self.table_size):
            if self.array[position] is None:                    # if the slot is empty in the table it sets the value at that position
                self.array[position] = (key, value)
                self.count += 1
                return
            elif self.array[position][0] == key:                # if the same key is found it updates the value at that position
                self.array[position] = (key, value)
                return
            else:
                position = (fixed_position + ((i + 1) ** 2)) % self.table_size     # if key is not found, look for the next position
                if copyPos == position:
                    raise Exception('High load factor')

    def __getitem__(self, key):
        '''
        This function returns the value corresponding to the key at the position in the Hash Table. The function raises
        a KeyError if the key does not exist in the Hash Table
        :param: The key which may or may not exist in the Hash Table
        :precondition: None
        :postcondition: The value is returned corresponding to the key in the hash table or a KeyError if key does not exist
        :complexity: Best Case = Worst Case = O(n), where n is the size of the table
        '''

        position = self.hash(key)
        fixed_position = position
        for i in range(self.table_size):
            if self.array[position] is None:                            # at that key position there is an empty slot
                break
            elif self.array[position][0] == key:                        # if the same key is found we return the value at that key
                return self.array[position][1]
            else:
                position = (fixed_position + ((i+1) ** 2)) % self.table_size    # if the key is not found, we look for the next position
        raise KeyError(key)                                               # if the for loop exits without returning means key does
                                                                          # not exist the hash table

    def __contains__(self, key):
        '''
        This function returns True if key is in the table and False otherwise.
        :param: The key which may or may not exist in the table
        :precondition: A hash table must already exist
        :postcondition: Returns true or false depending on whether the key exists in the table or not
        :complexity: Best Case = Worst Case = O(n), where n is the size of the hash table
        '''

        position = self.hash(key)
        fixed_position = position
        for i in range(self.table_size):
            if self.array[position] is None:                        # at that key position there is an empty slot, hence false since key does not exist there
                return False
            elif self.array[position][0] == key:                    # if the same key is found we return true as the key is found
                return True
            else:
                position = (fixed_position + ((i+1) ** 2)) % self.table_size         # if the key is not found, we look for the next position in the hash table
        return False

    def no_collisions(self):
        '''
        This function returns the number of collisions
        :param: None
        :precondition: None
        :postcondition: None
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        return self.collision_counter

def word_type(HashTable, word, maximum_frequency):
    if HashTable[word] >= (maximum_frequency / 100):
        print('Common\n')
    elif HashTable[word] >= (maximum_frequency / 1000):
        print('Uncommon\n')
    else:
        print('Rare\n')

HashTable = QuadraticProbeHashTable(1000081, 1)

def readBook(HashTable):
    '''
    This function reads the book into the hashtable and removes the punctuation from the words and increments the frequency depending on the word
    :param: HashTable
    :precondition: None
    :postcondition: None
    :complexity: Best Case = Worst Case = O(n), quadratic complexity
    '''

    file = 'book.txt'
    infile = open(file, 'r')

    for line in infile:
        n = line.strip('\n').split()
        for x in n:
            x = x.strip(string.punctuation).lower()
            if x == '':
                continue
            elif x not in HashTable:
                HashTable[x] = 1
            else:
                HashTable[x] = HashTable[x] + 1
                if HashTable[x] > HashTable.maximum_frequency:
                    HashTable.maximum_frequency = HashTable[x]

readBook(HashTable)

if __name__ == '__main__':

    while True:
        word = input("Enter a word to search or '!!' to quit: ")
        if word == '!!':
            print('The program has been terminated. ')
            break
        try:
            word_type(HashTable, word, HashTable.maximum_frequency)
        except:
            print('Word not found in the book. Please try again. \n')