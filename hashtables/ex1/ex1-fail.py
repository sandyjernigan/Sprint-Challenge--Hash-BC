#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    Given a package with a weight limit limit and a list weights of item weights, 
    implement a function get_indices_of_item_weights that finds two items whose 
    sum of weights equals the weight limit limit. 
    Your function will return an instance of an Answer tuple where each element 
    represents the item weights of the two packages. The higher valued index 
    should be placed in the zeroth index and the smaller index should be placed 
    in the first index. If such a pair doesn’t exist for the given inputs, 
    your function should return `None`
    """

    # weights is a list
    if not isinstance(weights, list):
        # Error if weights does not return a list
        print(f"There was an issue with weights: {weights}")

    # length is the length of the weights array
    if not isinstance(length, int):
        # Error if length does not return a integer
        print(f"There was an issue with length: {length}")

    # limit is a integer
    if not isinstance(limit, int):
        # Error if limit does not return a integer
        print(f"There was an issue with limit: {limit}")

    if length < 2:
        return None

    # Loop thru weights and add to hashtable
    for i in range(length):

        # store each weight in the input list as keys
        # store each weight's list index as its value
        hash_table_insert(ht, weights[i], i)

    # Loop thru weights and add sums
    current = ht.storage[5]

    print (current.key)
    
    print (current.next)

    while not current.next is None:

        # Get sum
        sumWeights = current.key + current.next.key

        # Check is sumWeight is equal to limit
        if sumWeights == limit:

            ''' The higher valued index should be placed in the zeroth index 
                and the smaller index should be placed in the first  '''
                
            # If a value is zero it should be first
            if current.key == 0:
                answer = [current.value, current.next.value]
                return answer
            if current.next.key == 0: 
                answer = [current.next.value, current.value]
                return answer
            
            # Find which weight is higher
            if current.key > current.next.key:
                answer = [current.value, current.next.value]
            else: 
                answer = [current.next.value, current.value]
                
            return answer

def print_answer(answer):
    if answer is not None:
        print(str(answer[0]) + " " + str(answer[1]))
    else:
        print("None")

        
weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print_answer(answer_4)
