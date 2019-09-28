def applyPromoCode(promoCode, amount):
    if promoCode == "FLAT50":
        return amount * 50//100
    elif promoCode == "FLAT30":
        return amount * 30//100
    else:
        return amount * 10 // 100

# Dynamic i.e. User Input
# pCode = input(">> Enter Promo Code to Apply: ")
# total = int(input(">> Enter Your Total Amount: "))
# discount = applyPromoCode(pCode, total)
# print(">> Discount for {} on {} is: {}".format(pCode, total, discount))

# Hard-Coded
# discount = applyPromoCode("FLAT50", 500)
# print(">> discount:", discount)

# print(">> Discounts:", applyPromoCode("FLAT50", 500))

# Functions are created in memory and they have HashCodes, the way storage containers have
# Print the name of Function
print(">> function applyPromoCode is:", applyPromoCode)
print(">> hex id of function applyPromoCode is:", hex(id(applyPromoCode)))

# Reference Copy
# HashCode in applyPromoCode is copied into fun
fun = applyPromoCode

print(">> fun applyPromoCode is:", fun)
print(">> hex id of fun applyPromoCode is:", hex(id(fun)))


# Now, we have 2 different names or references pointing to the same function
print(">> Discounts:", applyPromoCode("FLAT50", 500))
print(">> Discounts:", fun("FLAT50", 500))


# Assignment:
# 1. Flat50 gives 50% off for amount >= 2000
# 2. Flat30 gives 30% off for amount >= 500 and less than 2000
# 3. Flat10 gives 10% off for amount >= 200 and less than 500
# 4. No Discounts on amount less than 200
# 5. If user has applied a wrong promo code on some amount suggest him correct promo code
#    eg: amount -> 1000 | applied Flat50 -> Suggestion -> Use Flat30


