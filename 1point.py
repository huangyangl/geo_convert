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
filename = '航线3-备降点2.txt'  
# 使用'w'模式打开文件，如果文件不存在则创建文件  
with open(filename, 'w') as file:  
    # 写入内容到文件  
    file.write('QGC WPL 110')

# 打开第三方地图软件ovital导出的.ovjsn文件
filename_ovjsn='航线3-备降点2.ovjsn'
with open(filename_ovjsn, 'r',encoding='utf-8-sig') as file:  
    # 读取JSON数据  
    data = json.load(file)
    # 现在data是一个Python字典，你可以像操作普通字典一样操作它
    lat_gcj02=data['ObjItems'][0]['Object']['ObjectDetail']['Lat']
    lng_gcj02=data['ObjItems'][0]['Object']['ObjectDetail']['Lng']
    lng, lat = gcj02_to_wgs84(lng_gcj02,lat_gcj02)
    print('lat_gcj02:' + str(lat_gcj02) + ", lat_gcj02:" + str(lng_gcj02) + ";   lat_wgs84:" + str(lat) + ", lng_wgs84:"+str(lng)+"\n")
    prefix="1  0  3  16  0  0  0  0  "
    postfix="  1"
    alt_rel=120
    write_item(lat,lng,alt_rel,prefix,postfix,filename)