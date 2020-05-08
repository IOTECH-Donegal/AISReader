import array
import NMEA.Decoder


class Message1:
    def __init__(self):  # Init for instances
        self.MessageTypeField = ''
        self.RepeatIndicator = ''
        self.MMSI = ''
        self.NavigationStatus = ''
        self.ROT = ''
        self.SOG = ''
        self.PositionAccuracy = ''
        self.longitude = ''
        self.latitude = ''
        self.COG = ''
        self.TrueHeading = ''
        self.TimeStamp = ''
        self.RegionalReserved = ''
        self.Spare = ''
        self.RAIM = ''
        self.state_syncstate = ''
        self.state_slottimeout = ''
        self.state_slotoffset = ''

    def decode(self, processed_payload):
        # Create a bitstring of all the bits
        bitstring = ''
        for character in processed_payload:
            this_six_bits = format(character, '08b')
            bitstring = bitstring + this_six_bits[-6:]
        print(bitstring)


        self.RepeatIndicator = bitstring[6:7]

        mmsi_binary = bitstring[8:38]
        self.MMSI = int(mmsi_binary, 2)

        navigation_status = bitstring[38:42]
        rate_of_turn = bitstring[42:50]
        speed_over_ground = bitstring[50:60]
        position_accuracy = bitstring[60:61]
        longitude_binary = bitstring[61:89]
        NMEA.Decoder.decode_longitude(longitude_binary)

        latitude = bitstring[89:116]
        course_over_ground = bitstring[116:128]
        true_heading = bitstring[128:137]
        time_stamp = bitstring[137:143]
        maneuver_indicator = bitstring[143:145]
        spare = bitstring[145:148]
        raim = bitstring[148:149]
        radio_status = bitstring[149:168]






