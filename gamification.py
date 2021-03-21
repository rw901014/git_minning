import info

def gamification():

    website_address = ['https://github.com/matthann/CS3012-LCA-DAG',
        'https://github.com/juliaellen/CS3012',
        'https://github.com/dowlind1/CS3012']

    df_cq_0=info.info('https://github.com/beltonn/final-assignment-1-3rd-year')

    df_names = locals()
    for i in range(3):
        df_names['df_cq' + str(i) ] = info.info(website_address[i])
        df_cq_0=df_cq_0.append(df_names['df_cq' + str(i) ])

    maintain_test=[]
    create_test=[]
    maintain_fun=[]
    create_fun=[]
    test_total=[]
    fun_total=[]
    gamification=[]

    for i in range(4):
        maintain_test.append(float(df_cq_0[i:i+1]['No.maintain_test_commit']))
        create_test.append(float(df_cq_0[i:i+1]['No.create_test_commit']))
        maintain_fun.append(float(df_cq_0[i:i+1]['No.maintain_function_commit']))
        create_fun.append(float(df_cq_0[i:i+1]['No.create_function_commit']))
        test_total.append(float(df_cq_0[i:i+1]['No.test_commit']))
        fun_total.append(float(df_cq_0[i:i+1]['No.function_commit']))
        gamification.append(float(df_cq_0[i:i+1]['gamification']))


    for i in range(len(create_test)):
        maintain_test[i]=maintain_test[i]+1
        create_test[i]=create_test[i]+1
        maintain_fun[i]=maintain_fun[i]+1
        create_fun[i]=create_fun[i]+1

    #获取test和function的engagement分数：
    test_score=[]
    fun_score=[]
    for i in range(len(maintain_test)):
        test_score.append((maintain_test[i]+create_test[i])*create_test[i]/maintain_test[i])
        fun_score.append((maintain_fun[i]+create_fun[i])*create_fun[i]/maintain_fun[i])


    return test_score,fun_score,gamification

gamification()
