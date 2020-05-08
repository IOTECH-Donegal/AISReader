class Generic0183:
    def __init__(self):        # Init for instances
        self.InstrumentName = 'Unknown'
        self.InstrumentManufacturer = 'Unknown'
        self.NewMeasurement = False
        self.MeasurementValid = False

    '''
    Compare a calculated CRC to the received value
    '''
    def validate_crc(self, nmea_full_sentence):
        # The last two characters are HH where HH is the CRC
        checksum = nmea_full_sentence[-3:]
        # XOR all values between $ and *
        calculated_checksum = self.calculate_crc(nmea_full_sentence[1:-4])
        # Compare the calculated checksum with the numerical value of the extracted string
        if calculated_checksum == hex(int(checksum, 16)):
            return True
        else:
            return False

    '''
        Calculate the CRC of a NMEA sentence
        CRC is a simple XOR of all values between $ and *
    '''
    def calculate_crc(self, nmea_partial_sentence):
        # Reset to zero
        calculated_checksum = 0
        # Got through each character and XOR
        for character in nmea_partial_sentence:
            calculated_checksum ^= ord(character)
        return hex(calculated_checksum)
