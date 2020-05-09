
def decode_longitude(longitude_binary):
    longitude_int = int(longitude_binary, 2)

    if longitude_int >= 134217728:
        hemisphere = 'W'
        longitude = round((268435456 - longitude_int) / 600000, 5)
    else:
        hemisphere = 'E'
        longitude = round((longitude_int) / 600000, 5)

    if longitude_int == 181:
        "Longitude not available"
    else:
        print(str(longitude) + hemisphere)
        return str(longitude) + hemisphere


def decode_latitude(latitude_binary):
    latitude_int = int(latitude_binary, 2)

    if latitude_int >= 67108864:
        hemisphere = 'S'
        latitude = round((134217728 - latitude_int) / 600000, 5)
    else:
        hemisphere = 'N'
        latitude = round(latitude_int / 600000, 5)

    if latitude_int == 91:
        "Latitude not available"
    else:
       print(str(latitude) + hemisphere)
       return str(latitude) + hemisphere


