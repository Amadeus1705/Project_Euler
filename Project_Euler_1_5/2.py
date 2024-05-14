# Even Fibonacci Numbers

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 
#  and 
# , the first 
#  terms will be: 1,2,3,5,8,13,21,34....

# By considering the terms in the Fibonacci sequence whose 
# values do not exceed four million, find the sum of the even-valued terms.

fibs = []*2
fibs.append(1)
fibs.append(2)
i = 1
while fibs[len(fibs)-1]<4000000:
    fibs.append(fibs[i-1]+fibs[i])
    i+=1
sum_=0
for i in fibs:
    if i%2==0:
        sum_+=i
        
print(sum_)