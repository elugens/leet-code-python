def reverse(s):

    # Base Case
    if len(s) <= 1:
        return s
    # recursion
    else:
        return reverse(s[1:]) + s[0]


print(reverse("Shark"))

# Don't worry about the code below its for reference

a = 'krahS'

b = a[0:4] + a[-1]

print(b)
