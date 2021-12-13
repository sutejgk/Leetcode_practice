class Solution:
    
    def removeVowels(self, s: str) -> str:
        
        # Vowel list
        vowel_list = ["a","e","i","o","u"]
        
        # Temporary string
        temp_str = s
        
        # Counter to decide which character to slice out 
        counter = 0
        
        while(1):
            
            if(counter > len(temp_str)-1):
                break
            
            # If current character with counter value is a vowel
            if(temp_str[counter] in vowel_list):
                
                if(len(temp_str) == 1):
                    temp_str = ""
                    break
                
                # If first character of the string is a vowel 
                if(counter == 0):
                    temp_str = temp_str[1:]
                #    #print(temp_str)
                    continue
                
                # If last character of the string is a vowel (aeiou, need a special case for this)
                if(counter!=0 and counter == len(temp_str)-1):
                    temp_str = temp_str[0:-1]
                    #print(temp_str)
                    break 
                
                # If character is a vowel, and it is in the middle of the string 
                if(counter!=0):
                    temp_str = temp_str[0:counter] + temp_str[counter+1:]
                    #print(temp_str)
                    continue
                    
            counter = counter + 1 
                
        return temp_str
                
                
            
            
        
        
            
        
                
                

                
                
                    
            
            
            
        
        
        