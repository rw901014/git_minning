import info

def data():

    website_address = ['https://github.com/matthann/CS3012-LCA-DAG',
        'https://github.com/juliaellen/CS3012',
        'https://github.com/dowlind1/CS3012']

    df_cq_0=info.info('https://github.com/beltonn/final-assignment-1-3rd-year')
    df_cq_0.insert(df_cq_0.shape[1], 'num', '0')
    df_cq_node = df_cq_0[0:1]
    df_cq_LCA = df_cq_0[1:2]
    df_cq_TEST = df_cq_0[2:3]
    #print(df_cq_node)
    #print(df_cq_LCA)
    #print(df_cq_TEST)

    df_names = locals()
    for i in range(3):
        df_names['df_cq' + str(i) ] = info.info(website_address[i])
        df_names['df_cq' + str(i) ].insert(df_names['df_cq' + str(i) ].shape[1], 'num', str(i+1))
        '''
        if df_names['df_cq' + str(i) ][i:i+1][['file_name']].find("Node")>=0:
            df_cq_node.append(df_names['df_cq' + str(i) ][i:i+1])
        else:
            pass
        '''
        df_cq_0=df_cq_0.append(df_names['df_cq' + str(i) ])

    #给数据框编上序号
    seq = df_cq_0[0:1]
    seq.insert(df_cq_0.shape[1],'id',0)
    for i in range(len(df_cq_0)-1):
        #df_cq_0 = df_cq_0[i:i+1].insert(df_cq_0.shape[1], 'id', str(i))
        x = df_cq_0[i+1:i+2]
        x.insert(df_cq_0.shape[1],'id',str(i+1))
        seq = seq.append(x)
        #print(df_cq_0)

    print(seq)
    #print(df_cq_0)

    return seq

data()


#df_cq,df_eg=info.info('https://github.com/juliaellen/CS3012')
#print(df_cq)
#a=df_cq[2:3]




'''
print('##########')
print(a['file_name'])
'''
