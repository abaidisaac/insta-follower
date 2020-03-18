follower = open("New.txt")
following = open("New1.txt")
f = open("follower.txt",'w')
g = open("following.txt",'w')
a = follower.read()
b = following.read()
c = a.split('title=')
d = b.split('title=')
for i in c:
    f.write(i)
    f.write("\n")
for i in d:
    g.write(i)
    g.write("\n")

followers = open("follower.txt")
f1 = open("followers.txt",'w')
followings = open("following.txt")
g1 = open("followings.txt",'w')
e = followers.readlines()
h = followings.readlines()
k = []
l = []
for i in e:
    j = i.index('" ')
    if i[0:10] != '"Verified"':
        k.append(i[1:j])
for i in h:
    j = i.index('" ')
    if i[0:10] != '"Verified"':
        l.append(i[1:j])

for i in k:
    f1.write(i)
    f1.write("\n")
f1.close()
for i in l:
    g1.write(i)
    g1.write("\n")
g1.close()
