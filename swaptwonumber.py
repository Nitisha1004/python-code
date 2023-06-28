#first number enter the user
a=int(input("Enter the first number : "))
#second number enter the user
b=int(input("Enter the second number: "))
#print a and b without swap
print("a is ",a,"b is ",b)
#swap  two number using xor operator
# a xor b then and value return and store in a
a^=b
# b xor a then and value return and store in b
b^=a
#then a xor b then and value return and store in a
a^=b
#print a and b with swap without using temporary variable
print("a is ",a,"b is ",b)

# using a new variable temp then store the value of a
temp=a
# then a is empty then store b value in a
a=b
# b value store in temp value
b=temp
print("Using temporary variable")
# the output return in same user value because the value one by swap above without temporary variable
print("a is ",a,"b is ",b)