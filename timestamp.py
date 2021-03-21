from datetime import datetime
import time
############函数1:推算data的时间戳###############
def time_data1(time_sj):                #传入单个时间比如'2019-8-01 00:00:00'，类型为str
    data_sj = time.strptime(time_sj,"%Y-%m-%d %H:%M:%S")       #定义格式
    time_int = int(time.mktime(data_sj))
    return time_int             #返回传入时间的时间戳，类型为int
