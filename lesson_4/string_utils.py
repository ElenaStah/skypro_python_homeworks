class StringUtils:
 
    def capitilize(self, string: str):# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
      #Пример: `capitilize("skypro") -> "Skypro"`
        return string.capitalize()

    

    def trim(self, string: str) : #Пример: `trim(" skypro") -> "skypro"`
      

        whitespace = " "
        while (string.startswith(whitespace)):
            string = string.removeprefix(whitespace)
        return string
    

    def to_list(self, string: str, delimeter = ","):
 

        if(self.is_empty(string)):
            return []
        
        return string.split(delimeter)


    def contains(self, string: str, symbol: str) :#`contains("SkyPro", "S") -> True`
                                                  #contains("SkyPro", "U") -> False`
 

    
        res = False

        res = string.index(symbol) > -1
       

        return res
    

    def delete_symbol(self, string: str, symbol: str):
        
        if(self.contains(string, symbol)):
            string = string.replace(symbol, "") 
        return string


    def starts_with(self, string: str, symbol: str) :
        
        return string.startswith(symbol)


    def end_with(self, string: str, symbol: str) :
        
        return string.endswith(symbol)
    
    def is_empty(self, string: str):
        
        
        string = self.trim(string)
        return string == ""
    
    def list_to_string(self, lst: list, joiner=", "):
        
        

        string = ""
        length = len(lst)
        
        if length == 0: 
            return string 
        
        for i in range(0, length-1):
            string += str(lst[i]) + joiner
        
        return string + str(lst[-1])   