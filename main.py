s = str(input())
temp = s.lower()
l = temp.split("number next")
dic = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
first = l[0]
first = first.split("number")

first = [x.strip() for x in first]
ans = []
n = 0

initial = ""
for i in range(len(first)):
    x = first[i]
    x = x.strip()
    x = x.split()
    if x[0] in dic.keys():
        n = dic[x[0]]
        x = x[1:]
        x = " ".join(x)
        s = x+"".join(first[i+1:])
        ans.append(s)
    else:
        x = " ".join(x)
        initial+=x
initial = initial.capitalize()
ans+=l[1:]
print(initial)
for x in ans:
    x = x.strip()
    x = x.capitalize()
    print("{}.".format(n),x)
    n+=1
    


    

