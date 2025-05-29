
import math
n = N = 68755487 # input for divisor function
abc = []
primes = []

def divisors(n): 
    for i in range (2,n+1):
       if all(i % x != 0 for x in primes) or i==2: #if number is prime
           primes.append(i)  #add to list of prime numbers
           if n%i == 0:
                exp = 0 #each exp represents a,b,c ...
                while n%i == 0:
                    n= n/i
                    exp = exp + 1 
                abc.append(exp)   
                if n == 1: return(divcount(abc))
        
# Solves (a+1)(b+1)(c+1)... = # of divisors eq
def divcount(abc):
    abc = [a+1 for a in abc]
    return(math.prod(abc))

#Listing out divisors
def divisorlist(N):
    if N>200000000: return 'but unfortunately your number is too big to list them'
    else:
        List = []
        for j in range (1,N+1):
            if n%j ==0:
                List.append (int(j) and int(N/j))
        List.sort()        
        return(List)
        
print(f"There are {divisors(n)} divisors to the number {n}")
print (divisorlist(N))      
