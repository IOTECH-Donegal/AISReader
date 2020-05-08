
def decode_longitude(longitude_binary):
    longitude_int = int(longitude_binary, 2)

    if longitude_int >= 134217728:
        hemisphere = 'W'
        longitude = (268435456 - longitude_int) / 600000
        print(hemisphere)
        print(longitude)


def decode_latitude(latitude_binary):
    latitude_int = int(latitude_binary, 2)

    if latitude_int >= 134217728:
        hemisphere = 'N'
        latitude = (268435456 - latitude_int) / 600000
        print(hemisphere)
        print(latitude)