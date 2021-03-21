##################函数5:最终文件的CC和loc################
def get_code_qaulity(dictionary_file,dictionary_CC, dictionary_loc):
    #最终文件的复杂度
    file_name = []
    file_CC = []
    final_file_location = {v: k for k, v in dictionary_file.items()}
    their_key= {v: k for k, v in final_file_location.items()}
    for k,v in dictionary_CC.items():
        for m,n in their_key.items():
            if k==m:
                file_CC.append(v)
                file_name.append(n)
            else:
                pass
    d_file_CC=dict(zip(file_name,file_CC))

    file_name_1 = []
    file_loc = []
    final_file_location_1 = {v: k for k, v in dictionary_file.items()}
    their_key_1= {v: k for k, v in final_file_location_1.items()}
    for k,v in dictionary_loc.items():
        for m,n in their_key_1.items():
            if k==m:
                file_loc.append(v)
                file_name_1.append(n)
            else:
                pass
    d_file_loc=dict(zip(file_name_1,file_loc))

    return d_file_CC, d_file_loc
