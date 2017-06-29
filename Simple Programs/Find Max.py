'''
Name: Bazil Muzaffar Kotriwala
Timestamp: 5:35pm 09 Dec 2016
'''

class Country:

    def __init__(self, cont, lead, pop):
        self.continent = cont
        self.leader = lead
        self.population = pop

def leader_most_pop():
    '''
    This function compares the countries populations and returns the leader of the country with the highest population
    :param: None
    :precondition: A non empty country object list must exist
    :postcondition: The leader of the country with the highest population is returned
    :complexity: Best Case = Worst Case = O(n^2), where n is the length of the object list
    '''

    for i in range(len(obj_list)):
        for j in range(i + 1, len(obj_list)):
            if obj_list[i].population < obj_list[j].population:
                swap(obj_list, i, j)
    return obj_list[0].leader

def swap(obj_list, i, j):
    obj_list[i], obj_list[j] = obj_list[j], obj_list[i]

if __name__ == '__main__':
    canada = Country("North America", "Trudeau", 35344962)
    india = Country("Asia", "Modi", 2414919602323232)
    us = Country("North America", 'Obama', 311591917)

    obj_list = [canada, india, us]

    print(leader_most_pop())

