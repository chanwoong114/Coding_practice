def fee(t, d):
    rental_fee = t//10 * 1200
    insurance_fee = ((t-1)//30 + 1) * 525
    if d>100:
        driving_fee = (d%100)*85 + (d//100)*17000
    else:
        driving_fee = d*170

    return print(rental_fee + insurance_fee + driving_fee)

fee(600, 50) #=> 91000
fee(600, 110) #=> 100350
