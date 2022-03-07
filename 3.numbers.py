#                                 JavaScript                                        Python      
# # int                         var num = 35                                        num = 25
# # float                       var dec = 4.2;                                      dec = 4.2
# # log                         console.log(num);                                   print(num)
# # type check                  console.log(typeof(dec))                            print(type(dec))
# # conversion                  N/A. All numbers are                                num_to_dec = float(num)
# #                             floating point in JS 
# # random number bw 2-5        var rand_num = Math.floor(Math.random()*4+2)        import random rand_num=random.randint(2,5)

# Numbers 
# THere are 3 basics types of numbersin Python
# -int - whole numbers, positive or negative. ex. 35
# -float -decimal numbers, positive or negative. ex. 4.2
# -complex -are a part of the real number system and are 
#     often referenced with the letter j. ex. 1 + 3j.
#     **Note**if you're not sure if you need to use them, 
#     it is safe to say you can ignore this data type.

# Type
# if you are unsure which type a number is, you can use the type() to view the object
# type of any object
print(type(24))
print(type(3.9))
print(type(3j))

Conversion 
All Python objects have data type methods we can use to convert number types from one to another

int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

Random Number
Python does not have a built in random number generator, use the random module instead. 

import random
print(random.randint(2, 5))