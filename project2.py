##########################
# UNI:yl3433
# Name: Yuxuan Liu
# Assignment3
#######################

def find(some_string, substring, start, end):
    '''Find the first index of section that matches the substring''' 
    #Specify the range within which we are to search for substring  
    string_range = some_string[start:end+1]
    for i in range(len(string_range)):
        counter = 0
        for x in range(len(substring)):
            # Break the loop if (i + len(substring) -1) is out of index
            if i+len(substring)-1 >= len(string_range):
                break
            
            #Compare each character
            elif substring[x] == string_range[i+x]:
                counter += 1
                if counter == len(substring):
                    return i #Return the index if the substring is found
                    
            #Break out from the loop if the sequence doesn't match the substring 
            else:
                break
    return -1 #Return -1 if the iteration is finished 


def multi_find(some_string, substring, start, end):
    '''Find all the indices of sections that match the substring''' 
    index_list = [] #Store the found indices of substring into index_list
    #Specify the range within which we are to search for substring 
    string_range = some_string[start:end+1]
    for i in range(len(string_range)):
        counter = 0
        for x in range(len(substring)):
            # Break the loop if (i + len(substring) -1) is out of index
            if i+len(substring)-1 >= len(string_range):
                break
            
            #Compare each character
            elif substring[x] == string_range[i+x]:
                counter += 1
                if counter == len(substring):
                    index_list.append(str(i))
                    
            #Break out from the loop if the sequence doesn't match the substring 
            else:
                break
            
    index = ','.join(index_list) #Format the index to be returned  
            
    return index        
    
def main():   
    some_string = "12345678456000078456784567845678"
    substring = "45678"
    print(find(some_string, substring,0,100))
    print(multi_find(some_string, substring,0,100))
    
    
main()


            