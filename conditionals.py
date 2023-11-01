price=250000
credit = False
if credit or price>800000:
    downpayment=0.10*price
else:
    downpayment=0.2*price

print(f"downpayment = {downpayment} ")