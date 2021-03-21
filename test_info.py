################函数3:识别创建和维护test的commit数量#############
def test_info(list):
    maintain_test=0
    create_test=0
    for i in range(len(list)):
        if list[i].find("test")>=0:
            maintain_test=maintain_test+1
            if list[i].find("creat")>=0:
                create_test=create_test+1
            else:
                pass
        else:
            pass

    maintain_fun=0
    create_fun=0
    for i in range(len(list)):
        if list[i].find("fun")>=0:
            maintain_fun=maintain_fun+1
            if list[i].find("creat")>=0:
                create_fun=create_fun+1
            else:
                pass
        else:
            pass
    maintain_test = maintain_test - create_test
    maintain_fun = maintain_fun - create_fun
    return maintain_test, create_test, maintain_fun, create_test
