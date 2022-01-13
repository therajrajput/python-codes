def reverse(s):
    raj = " "
    for i in s:
        raj = i + raj
    return raj
s = "rajput"
print("the original string :",end="")
print(s)
print("the reversed string :",end="")
print(reverse(s))

