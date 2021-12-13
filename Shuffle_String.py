class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        temp_str = ''
        
        my_dict = {}
        
        # Create a dictionary for all the indice values 
        
        for i in range(0,len(indices)):
            
            my_dict[indices[i]] = s[i]
                    
        counter = 0
        
        temp_str = ""
        
        final_str = ""
        
        while(counter < len(indices)):
            
            #print(my_dict[counter])
            temp_str = temp_str + my_dict[counter]
            counter = counter+1
            
        return temp_str
        