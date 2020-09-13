def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
print(test_prime(9))

##################################
#armstrong ######################
#############################
for num in range(100,1000):
  temp=num
  sum=0
  while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10

  if sum==num:
    print (num)
