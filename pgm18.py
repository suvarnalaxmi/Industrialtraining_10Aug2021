#Write program to generate equated monthly installments (EMI)(intrest 5%/Month)of 3 year and 5 year of amount 161258/-

a=161258

emifor3=a/36

emifor5=a/60

emifor3withinterest=emifor3+(0.05*emifor3)

emifor5withinterest=emifor5+(0.05*emifor5)

print("EMI for 3 years with intrest 5%",emifor3withinterest)

print("EMI for 5 years with intrest 5%",emifor5withinterest)
                                                             