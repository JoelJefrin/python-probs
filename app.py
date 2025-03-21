#precedence of operaters
#that which operation should be conducted first
# x= 10 +3*2#here first the 3*2 is solved first 

# print(x)
# #0. parenthtesis 1.exponenation 2.mul or div 3.add or sub
# import math
# # math.floor
# is_hot = False
# if is_hot:
#     print("its a hot day")
# else:
#     print("its a cold day")

price = 1000000
has_good_credit= False
has_bad_credit= False
if has_good_credit:
    down_payment= 0.1*price
else:
    down_payment=0.2*price

print(f"the down payment will be : {down_payment}")