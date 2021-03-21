##################函数6:字典的value求平均值################
def avg_dict_value(dictionary_time, dictionary_CC, dictionary_loc):
    sum=0
    for k,v in dictionary_time.items():
        sum=sum+v
    CC=[]
    loc=[]
    prod=[]
    name=[]
    d_CC={}
    d_loc={}
    d_prod={}
    for k,v in dictionary_CC.items():
        v=int(v)
        v=v/sum
        CC.append(v)
    for k,v in dictionary_loc.items():
        v=int(v)
        v=v/sum
        loc.append(v)
    for k,v in dictionary_loc.items():
        v=int(v)
        v=sum/v
        prod.append(v)
    for k,v in dictionary_loc.items():
        name.append(k)
    d_CC = dict(zip(name,CC))
    d_loc = dict(zip(name,loc))
    d_prod = dict(zip(name,prod))
    return d_CC, d_loc, d_prod
