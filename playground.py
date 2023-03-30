
# f = open('result.txt','w')
# print(1,2,3, sep='\n'+'-'*10+'\n',end='\n'+'!'*10,file=f)
list_=[1,3,2,5,4,6,8,7]
print(sorted(list_,reverse=True))
ip = '10.1.24.128'
def ip_to_bin(ip_add):
    okt_list = [int(okt) for okt in ip_add.split('.')]
    print(f'{okt_list[0]:08b}|{okt_list[1]:08b}|{okt_list[2]:08b}|{okt_list[3]:08b}')
ip_to_bin(ip)
