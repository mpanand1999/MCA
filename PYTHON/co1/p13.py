#Accept an integer n and compute n+nn+nnn



n = int(input("Enter an integer n: "))
nn = n * 11 
nnn = n * 111
s = n + nn + nnn
print(f"{n}+{nn} + {nnn} = {s}")
