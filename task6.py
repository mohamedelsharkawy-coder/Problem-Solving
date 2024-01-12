# we here check if the year is a leap year or not 
# leap year --> is the year with aditional day 
# according to Gregorian calendar there are rules for this 
# year / 4 --> true and year / 100 --> false --> leap 
# year / 4 --> true and year / 100 --> true and year / 400 --> false  --> not leap 
# year / 4 --> true and year / 100 --> true and year / 400 --> true  --> leap 

# sol 1 

# def is_leap(year : int):

#     if year % 4 != 0:
#         return False
    
#     elif year % 4 == 0 and year % 100 != 0:
#         return True
    
#     elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
#         return False 

#     elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: 
#         return True 
    
#     else:
#         return "error"

# sol2 

def is_leap(year):
    
    # not divisble by 4 
    if year % 4 != 0:
        return False

    # divible by 4 
    elif year % 4 == 0:
        
        # not divisible by 100 
        if year % 100 != 0:
            return True
        
        # divisible by 100 
        elif year % 100 == 0:
            
            # divisible by 400 
            if year % 400 == 0:
                return True  
            
            # not divisible by 400 
            else: 
                return False 
            

year = int(input().strip())
print(is_leap(year))            
            




