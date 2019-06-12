alpha=input()
alpha=alpha.lower()
if(alpha=='$' or alpha=='%' or alpha=='*' or alpha=='#'):
    print("invalid")
elif(alpha=='a' or alpha=='e' or alpha=='i' or alpha=='o' or alpha=='u'):
    print("Vowel")
else:
    print("Consonant")
 
