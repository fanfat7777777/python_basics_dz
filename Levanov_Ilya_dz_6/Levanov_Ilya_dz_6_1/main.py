my_list = []
with open('nginx_logs.txt', 'r') as f:
    for l in f:
        my_list.append((l[:l.find('- ')], l[l.find('"')+1:l.find(' /')], l[l.find(' /')+1:l.find(' HTTP')]))
print(*my_list, sep='\n')