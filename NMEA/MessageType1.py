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
        self.MMSI = int(mmsi_binary,2)





