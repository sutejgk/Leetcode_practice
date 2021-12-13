class Solution:
    
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        x = 0
        
        for i in range(0,len(operations)):
            
            if operations[i][0] == "+" or operations[i][-1] == "+":
                x = x + 1
            elif operations[i][0] == "-" or operations[i][-1] == "-":
                x = x - 1
                
        
        return x