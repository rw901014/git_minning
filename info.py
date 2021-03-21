from pydriller import RepositoryMining
import time_interval, get_code_qaulity, commit_file_analysis, test_info, avg_dict_value
import pandas as pd
from pandas.core.frame import DataFrame
import chart

##################函数7:创建并收集基本信息################

def info(address):
    #commit内容
    l_commit_info=[]
    #commit源代码作者
    l_commit_author=[]
    #commit涉及的文件
    l_commit_file=[]
    #commit时间
    l_commit_date=[]
    #commit见时间差
    l_commit_interval=[]
    #commit对应代码的复杂度
    l_commit_CC=[]
    #commit对应代码的loc
    l_commit_loc=[]
    #单元的大小
    l_unit_size=[]
    #单元的复杂度
    l_unit_complexity=[]
    #单元的借口
    l_unit_interfacing=[]
    #以上几项的编号
    l_key=[]
    #用于编号计数
    k=0
    #从git上获取各种信息
    for commit in RepositoryMining(address).traverse_commits():
        for m in commit.modifications:
            l_commit_info.append(format(commit.msg))
            l_commit_author.append(format(commit.author))
            l_commit_file.append(format(m.filename))
            l_commit_date.append(format(commit.committer_date))
            l_commit_CC.append(format(m.complexity))
            l_commit_loc.append(format(m.nloc))
            l_unit_size.append(format(commit.dmm_unit_size))
            l_unit_complexity.append(format(commit.dmm_unit_complexity))
            l_unit_interfacing.append(format(commit.dmm_unit_interfacing))
            l_key.append(k)
            k=k+1
    #将date转换成时间戳之差
    l_commit_interval=time_interval.time_interval(l_commit_date)
    #将不同信息的list按照key对应成字典
    d_commit_info = dict(zip(l_key,l_commit_info))
    d_commit_author = dict(zip(l_key,l_commit_author))
    d_commit_file = dict(zip(l_key,l_commit_file))
    d_commit_date = dict(zip(l_key,l_commit_date))
    d_commit_interval = dict(zip(l_key,l_commit_interval))
    d_commit_CC = dict(zip(l_key,l_commit_CC))
    d_commit_loc = dict(zip(l_key,l_commit_loc))
    d_unit_size = dict(zip(l_key,l_unit_size))
    d_unit_complexity = dict(zip(l_key,l_unit_complexity))
    d_unit_interfacing = dict(zip(l_key,l_unit_interfacing))
    #依据loc来删除无效commit
    d_loc_del = dict(zip(l_key,l_commit_loc))
    for k,v in d_loc_del.items():
        if v=="None":
            del d_commit_info[k]
            del d_commit_author[k]
            del d_commit_file[k]
            del d_commit_date[k]
            del d_commit_interval[k]
            del d_commit_CC[k]
            del d_commit_loc[k]
            del d_unit_size[k]
            del d_unit_complexity[k]
            del d_unit_interfacing[k]
        else:
            pass

    #pd.set_option('display.max_columns',1000)
    #把一般的信息组成表格
    df_commit_info = pd.DataFrame.from_dict(d_commit_info, orient='index')
    df_commit_author = pd.DataFrame.from_dict(d_commit_author, orient='index')
    df_commit_file = pd.DataFrame.from_dict(d_commit_file, orient='index')
    df_commit_date = pd.DataFrame.from_dict(d_commit_date, orient='index')
    df_commit_interval = pd.DataFrame.from_dict(d_commit_interval, orient='index')
    df_commit_CC = pd.DataFrame.from_dict(d_commit_CC, orient='index')
    df_commit_loc = pd.DataFrame.from_dict(d_commit_loc, orient='index')
    df_unit_size = pd.DataFrame.from_dict(d_unit_size, orient='index')
    df_unit_complexity = pd.DataFrame.from_dict(d_unit_complexity, orient='index')
    df_unit_interfacing = pd.DataFrame.from_dict(d_unit_interfacing, orient='index')
    df_general_info = pd.concat([df_commit_info, df_commit_author, df_commit_file, df_commit_date, df_commit_interval,
        df_commit_CC, df_commit_loc, df_unit_size, df_unit_complexity, df_unit_interfacing],axis=1)
    #把顺序存成一列
    list_key=[]
    for k,v in d_commit_info.items():
        list_key.append(k)
    df_general_info.columns = ['commit_info','commit_author','commit_file','commit_date', 'commit_interval', 'commit_CC'
        , 'commit_loc', 'unit_size', 'unit_complexity', 'unit_interfacing']
    df_general_info['key'] = list_key
    ##############
    df_general_info

    #把cc和loc信息组成表格
    #获取最终文件的CC和loc
    d_final_CC, d_final_loc = get_code_qaulity.get_code_qaulity(d_commit_file, d_commit_CC, d_commit_loc)
    df_final_CC = pd.DataFrame.from_dict(d_final_CC, orient='index')
    df_final_loc = pd.DataFrame.from_dict(d_final_loc, orient='index')
    df_final_info = pd.concat([df_final_CC,df_final_loc],axis=1)
    df_final_info.columns = ['CC','loc']
    df_final_info

    #productivity有以下几点（除以耗时cc/time和loc/time和time/loc）（三个字典）
    d_CC, d_loc, d_prod = avg_dict_value.avg_dict_value(d_commit_interval, d_final_CC, d_final_loc)
    df_CC = pd.DataFrame.from_dict(d_CC, orient='index')
    df_loc = pd.DataFrame.from_dict(d_loc, orient='index')
    df_prod = pd.DataFrame.from_dict(d_prod, orient='index')
    df_productivity = pd.concat([df_CC, df_loc, df_prod],axis=1)
    df_productivity.columns = ['CC/time','loc/time','time/loc']

    #分析test和function代码的commit数量
    test_commit, fun_commit = commit_file_analysis.commit_file_analysis(d_commit_file)

    #engagement所需的相关参数
    maintain_test, create_test,maintain_fun, create_fun = test_info.test_info(l_commit_info)

    ################################################################################################
    #commit的一般信息
    df_general_info
    ##############
    #code quality由以下变量组成(两个字典)& productivity有以下几点（除以耗时cc/time和loc/time和time/loc）
    df_cq_prod = pd.concat([df_final_info, df_productivity],axis=1)
    #把文件名存成一列
    list_file=[]
    for k,v in d_final_CC.items():
        list_file.append(k)
    df_cq_prod['file_name'] = list_file
    df_cq_prod
    ##############
    #gamification规则下的评分：number of cycle(create_fun)*2+number of new test(create_test)*2+number of maintain test(maintain_test)
    #engagement由以下变量组成(均为数值)
    #生成表格
    gamification=create_fun*2+create_test*2+maintain_test
    engagement_gamification=[maintain_test,create_test,maintain_fun,create_fun,test_commit,fun_commit, gamification]
    df_engage_gami=DataFrame(engagement_gamification)
    df_engage_gami=df_engage_gami.T
    df_engage_gami.columns = ['No.maintain_test_commit','No.create_test_commit','No.maintain_function_commit'
        , 'No.create_function_commit', 'No.test_commit', 'No.function_commit', 'gamification']
    df_engage_gami
    ##############
    ################################################################################################

    #可以返回的commit内容包括：#d_commit_info, d_commit_author, d_commit_file, d_commit_date,d_commit_interval,d_commit_CC,d_commit_loc, d_unit_size, d_unit_complexity, d_unit_interfacing
    #############
    #输出df_general_info
    #涉及code quality的变量：d_final_CC, d_final_loc & 涉及productivity的变量：d_CC, d_loc, d_prod
    #############
    #输出df_cq_prod
    #涉及engagement和gamification的变量：maintain_test,create_test,maintain_fun,create_fun,test_commit,fun_commit, gamification
    #############
    #df_engage_gami

    #chart.chart(df_cq_prod)

    return df_engage_gami
