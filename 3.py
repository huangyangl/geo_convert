import json  
from converter import gcj02_to_wgs84

def write_item(lat,lng,alt_rel,prefix,postfix,filename):
    with open(filename, 'a') as file: 
        file.write("\n")
        file.write(prefix)
        file.write(str(lat))
        file.write("  ")
        file.write(str(lng))
        file.write("  ")
        file.write(str(alt_rel))
        file.write(postfix)
    return True

# 创建航点文件txt
filename = '3.txt'  
# 使用'w'模式打开文件，如果文件不存在则创建文件  
with open(filename, 'w') as file:  
    # 写入内容到文件  
    file.write('QGC WPL 110')

# 打开第三方地图软件ovital导出的.ovjsn文件
filename_ovjsn='航线3.ovjsn'
with open(filename_ovjsn, 'r',encoding='utf-8-sig') as file:  
    # 读取JSON数据  
    data = json.load(file)
    # 现在data是一个Python字典，你可以像操作普通字典一样操作它
    Latlng_list=data['ObjItems'][0]['Object']['ObjectDetail']['Latlng']
    print('Latlng_list:\n' + str(Latlng_list) + '\n')
    postfix="  1"
    alt_rel=120
    seq=1
    # 遍历
    for i in range(0, len(Latlng_list), 2):
        print(seq)
        lat_gcj02=Latlng_list[i]
        lng_gcj02=Latlng_list[i+1]
        lng, lat = gcj02_to_wgs84(lng_gcj02,lat_gcj02)
        print('lat_gcj02:' + str(lat_gcj02) + ", lat_gcj02:" + str(lng_gcj02) + ";   lat_wgs84:" + str(lat) + ", lng_wgs84:"+str(lng)+"\n")
        prefix=str(seq) + "  0  3  16  0  0  0  0  "
        write_item(lat,lng,alt_rel,prefix,postfix,filename)
        seq=seq+1