""" CSC108 Assignment 3: Social Networks - Starter code """
from typing import List, Tuple, Dict, TextIO

#    profiles_file = open('profiles.txt')
#    file = profiles_file.read().splitlines()
#    person_to_friends = {}
#    update_friend(file, person_to_friends)

def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> None:
    """Update the "person to friends" dictionary person_to_friends and the
    "person to networks" dictionary person_to_networks to include data from
    profiles_file.

    Docstring examples not given since result depends on input data.
    """
    file = profiles_file.read().splitlines()
    file.append('')
    update_friend(file, person_to_friends)
    update_network(file, person_to_networks)
    
    
def add_to_new(list1: list, person_to_friends: Dict[str, List[str]], name: str) -> None:
    """append the list1 to person_to_friends[name]
    """
    if name in person_to_friends: 
        for item in list1:
            if not item in person_to_friends[name]:
                person_to_friends[name].append(item)              
    else:
        person_to_friends[name] = list1

        
           
def update_friend(file: list, person_to_friends: Dict[str, List[str]]) -> None:
    """update friend from file to person_to_friends
    
    """
    current = []
    list1 = []
    for i in range(len(file)):
        if file[i] != '':
            current.append(file[i])
# if it's not the empty line then append to the list
        elif file[i] == '' and len(current) > 1:
            name = get_name(current[0])
            current = current[1 : ]
#remove the first item which is the name
            for item in current:
                if ',' in item:
                    list1.append(get_name(item))
            add_to_new(list1, person_to_friends, name)
            current = []
            list1 = []
        else:
            current = []
            list1 = []            
            
        
        
def update_network(file: list, person_to_networks: Dict[str, List[str]]) -> None:
    """update network from file to person_to_networks
    
    """
    current = []
    list1 = []
    for i in range(len(file)):
        if file[i] != '':
            current.append(file[i])
        elif file[i] == '' and len(current) > 1:
            name = get_name(current[0])
            current = current[1 : ]           
            for item in current:
                if not ',' in item:
                    list1.append(item)
            add_to_new(list1, person_to_networks, name)
            current = []
            list1 = []
        else:
            current = []
            list1 = []        


def get_firstname(og_name: str) -> str:
    """return the last name of og_name
    
    >>> get_firstname('a b')
    'a'
    >>> get_firstname('Jay Pritchett')
    'Jay'
    """
    indexof = og_name.index(' ')
    first = og_name[:indexof]
    return first
    
    
def get_lastname(og_name: str) -> str:
    """return the first name of og_name
    
    >>> get_lastname('a b')
    'b'
    >>> get_lastname('Jay Pritchett')
    'Pritchett'
    """
    indexof = og_name.index(' ')
    last = og_name[indexof + 1:]
    return last
    
    
def get_name(og_name: str) -> str:
    """return the og_name in the format of FirstName(s) LastName with space in 
    between
    >>> get_name('a, b')
    'b a'
    >>> get_name('Pritchett, Jay')
    'Jay Pritchett'
    """
    og_name = og_name.strip()
    indexof = og_name.index(',')
    first = og_name[indexof + 2:] 
    last = og_name[:indexof]
    return (first + ' ' + last).strip()

    
def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    """Return the average number of friends that people who appear as keys in 
    the person_to_friends have.
    
    >>> get_average_friend_count({'a': ['b', 'c', 'd'], 'e': ['f']})
    2.0
    >>> get_average_friend_count({'a': ['b'], 'c': ['d']})
    1.0
    """
    sumof = 0
    if person_to_friends != {}:
        for people in person_to_friends:
            sumof = sumof + len(person_to_friends[people])
        return sumof / len(person_to_friends)
    else:
        return 0.0

    
def get_families(person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first names" dictionary based on person_to_friends. 
    The returned dictionary contains every person whose name appears in 
    person_to_friends (as a key or in a value list). The keys in returned list 
    are the last names of people in person_to_friends. 
    
    >>> get_families({'a b': ['c d', 'e f'], 'e d': ['a d', 'b c']})
    {'b': ['a'], 'd': ['a', 'c', 'e'], 'f': ['e'], 'c': ['b']}
    >>> get_families({'a b': ['c b', 'e b'], 'e d': ['a d']})
    {'b': ['a', 'c', 'e'], 'd': ['a', 'e']}
    """
    familydic = {}
    
    for keys in person_to_friends:
        if get_lastname(keys) in familydic:
            familydic[get_lastname(keys)].append(get_firstname(keys))
            for values in person_to_friends[keys]:
                if get_lastname(values) in familydic:
                    familydic[get_lastname(values)].append(get_firstname(values))
                else:
                    familydic[get_lastname(values)] = [get_firstname(values)]
        else:
            familydic[get_lastname(keys)] = [get_firstname(keys)]
            for values in person_to_friends[keys]:
                if get_lastname(values) in familydic:
                    familydic[get_lastname(values)].append(get_firstname(values))
                else:
                    familydic[get_lastname(values)] = [get_firstname(values)]
    for item in familydic:
        familydic[item].sort()
    for item in familydic:
        for people in familydic[item]:
            while familydic[item].count(people) > 1:
                familydic[item].remove(people)
    return familydic


def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "network to people" dictionary based on person_to_networks. 
    The values in the dictionary are sorted alphabetically.
    
    >>> invert_network({'a b': 'X', 'a c': 'Y', 'a d': 'X'})
    {'X': ['a b', 'a d'], 'Y': ['a c']}
    """
    networkdic = {}
    for name in person_to_networks:
        for network in person_to_networks[name]:
            if not network in networkdic:
                networkdic[network] = [name]
            else:
                networkdic[network].append(name)
    for item in networkdic:
        networkdic[item].sort()
    return networkdic


def get_friends_of_friends(person_to_friends: Dict[str, List[str]], \
    person: str) -> List[str]:
    """Given person_to_friends and person (in the same format as the dictionary 
    keys), return the list of names of people who are friends of the named 
    person's friends.
    
    >>> get_friends_of_friends({'a b': ['a c', 'a d'], 'b c': ['b d', 'a d']}, 'a b')
    ['b c']
    >>> get_friends_of_friends({'a b': ['a c', 'a d'], 'b c': ['b d', 'a d'], 'a c': ['e f']}, 'a b')
    ['b c', 'e f']
    """
    returnlist = []
    target_friend = []
    if person in person_to_friends:
        target_friend = target_friend + person_to_friends[person]
    for friend in person_to_friends:
        if person in person_to_friends[friend]:
            target_friend.append(friend)
    for friend in person_to_friends:
        for name in target_friend:
            if name == friend:
                returnlist = returnlist + person_to_friends[friend]
            if name in person_to_friends[friend]:
                returnlist.append(friend)
    while person in returnlist:
        returnlist.remove(person)    
    returnlist.sort()
    return returnlist


def get_potential_friend(person_to_friends: Dict[str, List[str]], person: str) \
    ->List[str]:
    """get a list of potential friend of person according to person_to_friends
    
    >>> get_potential_friend({'a b': ['a c', 'a d'], 'b c': ['b d', 'a d']}, 'a b')
    ['b c', 'b d']
    """
    potential_friend = []
    potential_friends = []    
    for name in person_to_friends:
        if person != name and not name in person_to_friends[person]:
            potential_friend.append(name)
        for names in person_to_friends[name]:
            if person != names and not names in person_to_friends[person]:
                potential_friend.append(names)
    for name in potential_friend:
        if not name in potential_friends:
            potential_friends.append(name)
    return potential_friends    


def common_friend_num(person1: str, person2: str, person_to_friends: \
                      Dict[str, List[str]]) -> int:
    """return the number of common friends person1 and person2 have
    
    >>> common_friend_num('a', 'b', {'a': ['c', 'd', 'e'], 'e': ['b']})
    1
    >>> common_friend_num('a', 'b', {'a': ['c', 'd', 'e'], 'e': ['b'], 'd' :['b', 'f']})
    2
    """
    common = 0
    if person1 in person_to_friends and person2 in person_to_friends:
        for name1 in person_to_friends[person1]:
            for name2 in person_to_friends[person2]:
                if name1 == name2:
                    common += 1
    else:
        for name in person_to_friends:
            if person2 in person_to_friends[name]:
                common += 1
    return common

def common_network_num(person1: str, person2: str, person_to_networks: \
                       Dict[str, List[str]]) -> int:
    """return number of common network person1 and person2 have according to 
    person_to_networks
    
    >>> common_network_num('a', 'b', {'a': ['c', 'd'], 'b': ['c', 'e']})
    1
    >>> common_network_num('a', 'b', {'a': ['c', 'd', 'e'], 'b': ['c', 'e']})
    2
    """
    common = 0
    if person1 in person_to_networks and person2 in person_to_networks:
        for network1 in person_to_networks[person1]:
            if network1 in person_to_networks[person2]:
                common += 1
    return common
    
def sort_friend(old: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """sort the friend from old 
    >>> sort_friend([('d', 1), ('b', 3), ('c', 5), ('a', 1)])
    [('c', 5), ('b', 3), ('a', 1), ('d', 1)]
    """
    old.sort()
    for j in range(len(old) - 1, 0, -1):
        for i in range(j):
            if old[i][1] < old[i + 1][1]:
                old[i], old[i + 1] = old[i + 1], old[i]  
    return old

   
def make_recommendations(person: str, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> List[Tuple[str, int]]:
    """ Using person_to_friends and person_to_networks to return the friend 
    recommendations for person as a list of tuples where the first element of 
    each tuple is a potential friend's name and the second element is that 
    potential friend's score.
    
    >>> make_recommendations('a b', {'a b': ['a c', 'a d'], 'b c': ['a c', 'b d'], \
    'c d': ['b z']}, {'a b': ['a', 'b'], 'b c': ['a'], 'c d': ['b']})
    [('b c', 2), ('c d', 1)]
    """
    
    recommendation = []
    for names in person_to_friends:
        if person in person_to_friends or person in person_to_friends[names]:
            potenetial_friends = get_potential_friend(person_to_friends, person)
            for name in potenetial_friends:
                potential = 0
                if name in get_friends_of_friends(person_to_friends, person) or person \
                   in get_friends_of_friends(person_to_friends, name):
                    potential += common_friend_num(person, name, person_to_friends)
                potential += common_network_num(person, name, person_to_networks)
                if name in get_friends_of_friends(person_to_friends, person) or person \
                   in get_friends_of_friends(person_to_friends, name) or \
                   common_friend_num(person, name, person_to_friends) > 0:
                    if get_lastname(person) == get_lastname(name):
                        potential += 1
                if potential > 0:
                    recommendation.append((name, potential))
                recommendation = sort_friend(recommendation)
            return recommendation            
    return []

          
if __name__ == '__main__':
    import doctest
    doctest.testmod()
