f = open("followers.txt")
g = open("followings.txt")
a = f.readlines()
b = g.readlines()
for i in b:
   if i not in a:
      print i

         