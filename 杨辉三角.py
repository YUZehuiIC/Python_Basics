n=5
ls=[]
try:
    for i in range(n):
        if i==0:
            ls=[[1]]
        elif i==1:
            ls=[[1],[1,1]]
        else:
            t_ls=[]
            t_ls.append(1)
            tem=ls[i-1]
            for j in range(1,i):
                t_ls.append(tem[j-1]+tem[j])
            t_ls.append(1)
            ls.append(t_ls)
print(ls)
