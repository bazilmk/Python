'''Name: Bazil Muzaffar Kotriwala
   Student ID: 27012336   '''

print('Welcome to our online CD Store! \n')


#This function is to create a database, which reads the contents of a file and stores all the content as a 2D List.
#The Title, Artist and Genre is stored as a string inside the list, and the price of each cd is stored as a float.

def createDatabase():
    filename = 'CD_Store.txt'
    infile = open(filename, 'r')                                         #reading from a file
    contents = infile.readlines()
    infile.close()

    L = []
    for i in range(len(contents)):
        incomp_records = []
        infoStr = contents[i]
        infoList = infoStr.split(',')                               #storing each record type as a string in each list

        for j in range(len(infoList[0:3])):
            infoList[j] = infoList[j].rstrip('\n')       #Returns the lists with \n removed from the end of the strings within the list
            incomp_records.append(infoList[j])

        Record = float(infoList[3])
        incomp_records.append(Record)                    #Converts the string into float for the price of CD attribute in each list.

        L.append(incomp_records)

    return L

#This function is used to display the menu to the user from which he can select the required option.
#After the required option is chosen, the functionality is implemented and then the menu is printed again for the user.
#The menu is displayed every time after an option is chosen until the user inputs '10', to quit the program.

def DisplayMenu():

    menu = True
    while menu:
        print('1. Print List of CDs')
        print('2. Sort CDs by Title')
        print('3. Sort CDs by Artist')
        print('4. Sort CDs by Genre')
        print('5. Sort CDs by Price')
        print('6. Find all CDs by Title')
        print('7. Find all CDs by Artist')
        print('8. Find all CDs by Genre')
        print('9. Find all CDs with Price at Most X')
        print('10. Quit')
        break

#This function prints the CD's that are available in the CD Store.
#This function prints the list in a readable format identifying each field.
#This function is used throughout the program:
#To print the database of CD's or in printing the sorted CD's or in printing the searched CD's depending on the options chosen.

def PrintList(cd_list):
    for i in range(len(cd_list)):
        print('\n CD Number: %s' % (i+1))
        print('\t Title: ' + cd_list[i][0] + '\n\t Artist: ' + cd_list[i][1] + '\n\t Genre: ' + cd_list[i][2] +
              '\n\t Price of CD: ' + str(cd_list[i][3]))

#This function takes in three parameters, one list, and two indexes
#This function swaps the rows within the 2D list.

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

#This function takes two parameters, the list L and the Index of the Attribute
#This is a general bubblesort function which is called for all sortings ahead.
#We just change the AttributeIndex as required upon what attribute we are sorting.

def BubbleSort(L, AttributeIndex):
    for i in range(len(L) - 1):
        for j in range(i + 1, len(L)):
            if L[i][AttributeIndex] > L[j][AttributeIndex]:                   #compares each adjacent value and swaps it accordingly.
                swap(L, i, j)

#This function takes one parameter which is a list, in this program that is the CD list.
#This function sorts the CD List by Title in ascending order.

def SortByTitle(L):
    BubbleSort(L,0)                                                 #Title is index 0
    return L


#This function takes one parameter which is a list, in this program that is the CD list.
#This function sorts the CD List by Artist in ascending order.

def SortByArtist(L):
    BubbleSort(L, 1)                                              #Artist is index 1
    return L


#This function takes one parameter which is a list, in this program that is the CD list.
#This function sorts the CD List by Genre in ascending order.

def SortByGenre(L):
                                               #Genre is index 2
    return L

#This function takes one parameter which is a list, in this program that is the CD list.
#This function sorts the CD List by Price in ascending order.

def SortByPrice(L):
    BubbleSort(L, 3)                                            #Price is index 3
    return L

#This function takes three parameters, a list, target string and Index of the Attribute.
#This is a general Find function which is called for all Finds ahead except for FindByPrice.
#If the Attribute searched for is found, all the details of that CD are added to a list and then the list is returned.

def Find(L, target, AttributeIndex):
    Found = []
    for i in range(len(L)):
        if L[i][AttributeIndex] == target:
            Found.append(L[i][:])
    return Found

#This function takes two parameters, a list and a target string, target string in this case is the 'Title' with index 0
#If the Title searched is found, all the details of that CD are added to a list and then the list is printed.
#If the Title is not found, a message appears informing the user that the CD with that specific Title is not available.

def FindByTitle(L,Title):
    TitleFound = Find(L, Title, 0)                                #Title is index 0

    if len(TitleFound) == 0:
        print('\n Sorry, the CD with the Title: %s, is not available.' % Title)

    else:
        PrintList(TitleFound)

#This function takes two parameters, a list and a target string, target string in this case is the 'Artist' with index 1
#If the Artist searched is found, all the details of that CD are added to a list and then the list is printed.
#If the Artist is not found, a message appears informing the user that the CD with that specific Artist is not available.

def FindByArtist(L,Artist):
    ArtistFound = Find(L, Artist, 1)                                #Artist is index 1

    if len(ArtistFound) == 0:
        print('\n Sorry, CD\'s from the Artist: %s, are not available.' % Artist)

    else:
        PrintList(ArtistFound)

#This function takes two parameter, a list and a target string, target string in this case is the 'Genre' with index 2
#If the Genre searched is found, all the details of that CD are added to a list and then the list is printed.
#If the Genre is not found, a message appears informing the user that the CD with that specific Genre is not available.

def FindByGenre(L,Genre):
    GenreFound = Find(L, Genre, 2)                                      #Genre is index 2
    if len(GenreFound) == 0:
        print('\n Sorry, CD\'s with the Genre: %s, are not available.' % Genre)

    else:
        PrintList(GenreFound)

#This function takes two parameters, a list and a target string, target string in this case is the 'Price' with index 3
#If the Price searched is found:
#all the details of the CD's with prices equal to or less than the Price inputted are added to the respective lists and then the lists are printed.
#If the Price is not found, a message appears informing the user that the CD's with prices equal to or less than the price inputted are not available.

def FindByPrice(L, Price):
    PriceFound = []
    for i in range(len(L)):
        if L[i][3] <= Price:                                            #Price is index 3
            PriceFound.append(L[i][:])

    if len(PriceFound) == 0:
        print('\n Sorry, the CD\'s with the Price less than or equal to: %s, are not available.' % Price)

    else:
        PrintList(PriceFound)


cd_list = createDatabase()                             #Storing the CD database into a list.


#This is a while loop, which is never ending unless the user chooses to quit the program by selecting the option '10'.
#The menu is printed and the user is given to select an option from 1 - 10.
#If the user inputs any value apart from 1 - 10, the program notifies that option does not exist and asks to choose again from 1-10.
#Note: There are empty print() statements to make the output less clustered and more neater as it gives some line spacing.

menu = True

while menu:
    DisplayMenu()
    print()
    option_chosen = input('Select an option from 1-10: ')

    if option_chosen == '1':
        PrintList(cd_list)
        print()

    elif option_chosen == '2':
        SortByTitle(cd_list)
        print('\n The CD\'s have been sorted by Title, Select 1 to Print the sorted CD\'s or choose any another option from 2-10: \n')

    elif option_chosen == '3':
        SortByArtist(cd_list)
        print('\n The CD\'s have been sorted by Artist, Select 1 to Print the sorted CD\'s or choose any another option from 2-10: \n')

    elif option_chosen == '4':
        SortByGenre(cd_list)
        print('\n The CD\'s have been sorted by Genre, Select 1 to Print the sorted CD\'s or choose any another option from 2-10: \n')

    elif option_chosen == '5':
        SortByPrice(cd_list)
        print('\n The CD\'s have been sorted by Price, Select 1 to Print the sorted CD\'s or choose any another option from 2-10: \n')

    elif option_chosen == '6':
        Title = input('Enter the title of the CD: ')
        FindByTitle(cd_list, Title)
        print()

    elif option_chosen == '7':
        Artist = input('Enter the name of the Artist: ')
        FindByArtist(cd_list, Artist)
        print()

    elif option_chosen == '8':
        Genre = input('Enter the Genre of the CD: ')
        FindByGenre(cd_list, Genre)
        print()

    elif option_chosen == '9':
        Price = float(input('Enter the max price of the CD: '))
        FindByPrice(SortByPrice(cd_list), Price)
        print()

    elif option_chosen == '10':
        menu = False
        print('\n The Program has been terminated')

    else:
        print('\n Option does not exist. Please try again with an option from 1-10. \n')
        menu = True
