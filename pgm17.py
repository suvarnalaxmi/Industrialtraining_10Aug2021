#Write programm to calculate monthly simple intrest and compound intrest(5%/Month) on amount - 161258/-

p=161258
r=0.05
n=1/12

SI=p*n*r
print("Simple interest=",SI)

A=p*(1+r)**n
print("Amount=",A)


CI=A-p
print("Compound interest=",CI)

