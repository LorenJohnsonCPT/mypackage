def top_n(items, n):
    """Returns the top 10 items in an array, in desc order.

    Args:
        items (array): list ot array-like object
        n (int): num of items to return

    Return:
        array: top n items, in des order

    Egs:
        >>> top_n([8,3,2,7,4],3)
        [8,7,3]
    """
    for i in range(n):# keep sorting until we have the top n items
        for j in range(len(items)-1-i): 
        
         if items[j] > items[j+1]: # if this item is bigger then the next..
             items[j], items[j+1] = items[j+1], items[j] # swap the two!

    # get last two lines
    top_n = items[-n]

    # return in decending order
    return top_n[::-1]