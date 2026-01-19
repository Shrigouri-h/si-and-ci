def calculate_interest(p,t,r):
    si = (p*t*r)/100
    ci = p*((1+r/100)**t)-p
    return si, ci
p=int(input("Enter the principal amount:"))
t=int(input("Enter the time :"))
r=int(input("Enter the rate"))
print(calculate_interest(p,t,r))