#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    
    for i in range(list_length):
        try:      
            # Perform division
            result = my_list_1[i] / my_list_2[i]
        
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        
        except TypeError:
            print("wrong type")
            result = 0
        
        except IndexError:
            print("out of range")
            result = 0
        
        finally:
            # Add the result to the new list regardless of errors
            new_list.append(result)
    
    return new_list
