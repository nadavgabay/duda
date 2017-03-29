
original_file = '/Users/nadavgabay/src/trunk/duda/DudaRoot/src/resources/Turkish/config/CommonStrings_TURKISH.config.properties'
the_new_file = '/Users/nadavgabay/Downloads/CommonStrings.config_tr_TR.properties'

list_of_lines = []
list_of_old_lines = []

with open(original_file, 'r') as f:
    for line in f.readlines():
        list_of_old_lines.append(line.split('=')[0].lower())


with open(the_new_file, 'r') as f:
    for line in f.readlines():
        line_temp = line.split('=')[0].lower()
        if ('title' in line_temp or 'subject' in line_temp) and line_temp not in list_of_old_lines:
            list_of_lines.append(line)

# print list_of_lines
for i in list_of_lines:
    print i