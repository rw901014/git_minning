#################函数4:分析不同文件被更新的次数################
def commit_file_analysis(dictionary):
    test_commit=0
    fun_commit=0
    for k,v in dictionary.items():
        if v.find("test")>=0:
            test_commit=test_commit+1
        else:
            pass
    for k,v in dictionary.items():
        if v.find("test")<0:
            fun_commit=fun_commit+1
        else:
            pass
    return test_commit, fun_commit
