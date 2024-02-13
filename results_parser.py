
item_return_length = 4

def most_searched_completions( search_term : str) -> list :
    with open("./medical-questions/medical-questions.txt", "r", encoding='utf8') as search_records:
        #load all lines into memory - speed up search
        lines = search_records.readlines()
    
    results_dict = dict()

    for line in lines:

        if not (line.startswith(search_term)):
            #go to next iteration if not valid
            continue
        
        #split term into num string and search string
        search_string , number_string = line.rsplit('\t', 1)
        
        try:
            num_hits = int(number_string)
        except:
            #ignore any terms that are not valid integers
            #Just in case corruption occurs in file
            continue

        #assume list we get is unsorted - fair case
        #if list is sorted, like provided, optimization could occur where we just grab the 
        #first terms we see, up to max term number, but I am not.
        if len(results_dict) == item_return_length:
            key_array = results_dict.keys()
            #find minumum key value
            minumum = min(key_array)
            #Replace if current item has more results
            if minumum < num_hits:
                del results_dict[minumum]
                results_dict[num_hits] = search_string
        else:
            #Just add if limit is not reached
            results_dict[num_hits] = search_string
    
    ret = list()

    #Need to order list - assumed results may not come in order
    if len(results_dict) > 0:
        #Reversed for largest number first
        results_dict = dict(sorted(results_dict.items(), reverse=True))
        ret = list(results_dict.values())
    
    return ret
    

if __name__ == '__main__':
    ret = most_searched_completions("how")
    print(ret)