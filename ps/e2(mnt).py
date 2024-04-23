import re

def pass1(sent_tokens):
    macro_name_table, arg_list_arr, alas, macro_def_table = ([] for i in range(4))
    mdt_index, mnt_index, ala_index = (0 for i in range(3))
    int_code = ""

    flag = 0
    for sent in sent_tokens:
        mdt_entry = {'Index': 0, 'Definition': "null"}
        mnt_entry = {'Index': 0, 'Macro Name': "null", 'MDT Index': 0}
        ala_entry = {'Index': 0, 'Argument': "null", 'Value': '-'}
        sent = sent.strip()
        sent = sent.replace(",", ",")
        if ';' in sent:
            sent = re.sub(';.*', sent)

        word_tokens = re.findall(r"[\S]+", sent)

        if "MACRO" in sent:
            flag = 1
            continue
        if flag == 0:
            int_code += sent + "\n"
        if flag >= 1:
            mdt_index += 1
            mdt_entry = {'index': mdt_index, 'Definition': sent}
            macro_def_table.append(mdt_entry)
            if flag == 1:
                macro_name = word_tokens[0]
                mnt_index += 1
                operands = word_tokens[1].split(',')
                mnt_entry = {'index': mnt_index, 'Macro Name': macro_name, 'MDT index': mdt_index}
                macro_name_table.append(mnt_entry)
                for operand in operands:
                    ala_index += 1
                    if '=' in operand:
                        ala_entry = {'Index': ala_index, 'Argument': re.findall('(.*)=', operand)[0],
                                     'Value': re.findall('=(.*)', operand)[0]}
                    else:
                        ala_entry = {'Index': ala_index, 'Argument': operand, 'value': '-'}
                        alas.append(ala_entry)
                        arg_list_arr.append(alas)
                        flag += 1
        if "MEND" in sent:
            flag = 0
            alas = []
            ala_index = 0

    return int_code, macro_name_table

source_file = open('macro.txt', 'r')
sent_tokens = source_file.readlines()
source_file.close()

int_code, macro_name_table = pass1(sent_tokens)

print("\n\nmacro Name Table:-\n")
print('{:10}'.format("Index"), '{:20}'.format("Macro Name"), '{:20}'.format("MDT Index"))
for x in macro_name_table:
    print('{:10}'.format(str(x["index"])), '{:20}'.format(x["Macro Name"]), '{:20}'.format(str(x["MDT index"])))

# input
# macro.txt
# MACRO
# INCR1 &ARG1,&ARG2
#     A 1,&ARG1
#     L 2,&ARG2
# MEND
# MACRO
# INCR2 &ARG1,&ARG2
#     M 1,&ARG1
#     S 2,&ARG2
# MEND
# MACRO
# COMPLEX &X
#     INCR1 &X,DATA1
#     INCR2 &X,DATA2
# MEND