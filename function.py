#factorial
def factriol(n):
    fact=1
    for i in range(n,0,-1):
        fact*=i
    return  fact      

#binomial 
n=int(input("enter nth number:"))
r=int(input("enter rth number:"))
#calculate the factorial.
fact_n=factriol(n)
fact_r=factriol(r)
fact_nr=factriol(n-r)
#put on formula
bin_coff=fact_n/(fact_r*fact_nr)
print(bin_coff)
