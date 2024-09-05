geo_convert
Geolocataion conversion between WGS84, BD09 and GCJ02.

WGS84 / BD09 / GCJ02 / MapBar 经纬度坐标互转。

WGS84: GPS coordinates for Google Earth (GPS坐标，谷歌地球使用)
GCJ02: national coordinate system developed by China (国测局坐标，谷歌中国地图、腾讯地图、高德地图使用)
BD09: Baidu coordinates (百度坐标系，百度地图使用)
MapBar: MapBar coordinates (图吧坐标系，图吧地图使用)
Test website: http://gpsspg.com/maps.htm

注意：converter.py是库文件，其他*.py都是使用示例文件！！！！




GCJ-02
117.20760890,31.83914407
lng,lat

QGC WPL 110
0	1	0	16	0	0	0	0	31.8360129	117.2011954	        47.040000	1    #home
1	0	3	16	0	0	0.	0	31.82106820	117.06952150	120.00000	1    #航点

20240904

def gcj02_to_wgs84(lng, lat):
    """GCJ02 -> WGS84"""
    if out_of_china(lng, lat):
        return lng, lat
    dlat = transform_lat(lng - 105.0, lat - 35.0)
    dlng = transform_lng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * PI
    magic = math.sin(radlat)
    magic = 1 - EE * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((A * (1 - EE)) / (magic * sqrtmagic) * PI)
    dlng = (dlng * 180.0) / (A / sqrtmagic * math.cos(radlat) * PI)
    lng, lat = lng - dlng, lat - dlat
    return lng, lat

python3
from converter import gcj02_to_wgs84
gcj02_to_wgs84()