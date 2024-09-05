from converter import gcj02_to_wgs84

def write_item(lat,lng,alt_rel,prefix,postfix):
    with open('home.txt', 'a') as file: 
        file.write("\n")
        file.write(prefix)
        file.write(str(lat))
        file.write("  ")
        file.write(str(lng))
        file.write("  ")
        file.write(str(alt_rel))
        file.write(postfix)
    return True

lng, lat = gcj02_to_wgs84(117.20760890,31.83914407)
prefix="1  0  3  16  0  0  0  0  "  
postfix="  1"
alt_rel=120
write_item(lat,lng,alt_rel,prefix,postfix)
