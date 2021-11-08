def verify(key, A): #The algorithm of verification.
    r = A%97
    return key == 97-r

num = "285078618304815" #Defines a code.
A = int(num[:-2]) #All numbers without the two last.
K = int(num[-2:]) #The two last numbers -> the key.
print("Verifying if the code works...")
print("Result :", verify(K, A)) #Just to verify if the num has no error.
print("Now we will test if we change a number.")
for j in "0123456789": #Tests with all the numbers.
    for i in range(len(num)-2): #For all numbers except the key. 
        num_chg = num[:i] + str(j) + num[(i+1):] #Changes the number at the index i by j.
        A_ = int(num_chg[:-2]) #All numbers without the two last
        if((verify(K, A_) and A != A) or not verify(K, A_)): #If the code works, it verifies if the code isn't the same.
            print("Result :", verify(K, A_), "> Num :", num_chg, "> Index :", i) #Shows the result.
    
