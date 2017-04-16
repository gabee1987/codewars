coll = [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
coll2 = []


#def most_frequent_item_count(collection):
    #counted_db = []
    #duplicates = []
    #counter = 0
    #for item in collection:
        #if item not in counted_db:
            #counted_db.append(item)
        #else:
            #duplicates.append(item)
    #for number in (counted_db and duplicates):
        #if number in (counted_db and duplicates):
            #counter += 1
    #return counter


#def most_frequent_item_count(collection):
    #max(zip((collections.count(item) for item in set(collection))


def most_frequent_item_count(collection):
    dict = {x:collection.count(x) for x in collection}
    dict_val = dict.values()
    max_val = max(dict_val)
    print(dict_val)

most_frequent_item_count(coll)

