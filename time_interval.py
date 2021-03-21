import timestamp
############函数2:把commit_date的时间list转换成时间戳，最后一项为总时间差###############
def time_interval(list):                #传入爬取的commit时间的list
    list_1=[]
    for i in range(len(list)):
        rep_01 = list[i].replace('+01:00','')
        list_1.append(rep_01)

    list_2=[]
    for i in range(len(list_1)):
        rep_02 = list_1[i].replace('+00:00','')
        list_2.append(rep_02)
    list_inter=[]
    for i in range(len(list_2)-1):
        diff = timestamp.time_data1(list_2[i+1]) - timestamp.time_data1(list_2[i])
        list_inter.append(diff)

    total = 0
    for ele in range(0, len(list_inter)):
        total = total + list_inter[ele]

    list_inter.append(total)
    return list_inter
