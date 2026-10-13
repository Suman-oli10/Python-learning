#Program to print letter= Dear <|name|> 
                        # You are selected!
                        #  <|date|>

name=input("Enter your name:")
date=input("Enter date:")
print(f"Dear<|{name}|>\nYou are selected!\n<|{date}|>")
  


  #another method:
letter='''dear <|name|> 
             You are selected!
              <|date|>'''
print(letter.replace("<|name|>","Suman").replace("<|date|>","23 march 2024"))