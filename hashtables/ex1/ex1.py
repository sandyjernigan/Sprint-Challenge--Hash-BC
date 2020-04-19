#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    Get Indices of Item Weight
    """

    # weights is a list
    if not isinstance(weights, list):
        # Error if weights does not return a list
        print(f"There was an issue with weights: {weights}")

    # length is a integer
    if not isinstance(length, int):
        # Error if length does not return a integer
        print(f"There was an issue with length: {length}")

    # limit is a integer
    if not isinstance(limit, int):
        # Error if limit does not return a integer
        print(f"There was an issue with limit: {limit}")

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
