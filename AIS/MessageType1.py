import array
import AIS.Utilities


class Message1:
    def __init__(self):  # Init for instances
        self.MessageTypeField = ''
        self.RepeatIndicator = ''
        self.MMSI = ''
        self.NavigationStatus = ''
        self.ROT = ''
        self.SOG = ''
        self.PositionAccuracy = ''
        self.Longitude = ''
        self.Latitude = ''
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

        try:
            for character in processed_payload:
                this_six_bits = format(character, '08b')
                bitstring = bitstring + this_six_bits[-6:]
        except:
            print('Error processing bitfield')
            return False

        try:
            self.RepeatIndicator = bitstring[6:7]
        except:
            print('Error - RepeatIndicator')
            return False

        try:
            mmsi_binary = bitstring[8:38]
            self.MMSI = int(mmsi_binary, 2)
        except:
            print('Error - MMSI')
            return False

        try:
            navigation_status_binary = bitstring[38:42]
            self.NavigationStatus = self.decode_navigation_status(navigation_status_binary)
        except:
            print('Error - Navigation Status')
            return False

        try:
            rate_of_turn_binary = bitstring[42:50]
            self.ROT = self.decode_rate_of_turn(rate_of_turn_binary)
        except:
            print('Error - Rate of Turn')
            return False

        try:
            speed_over_ground = bitstring[50:60]
            self.SOG = self.decode_sog(speed_over_ground)
        except:
            print('Error - SOG')
            return False


        try:
            longitude_binary = bitstring[61:89]
            self.Longitude = AIS.Utilities.decode_longitude(longitude_binary)
        except:
            print('Error - longitude')
            return False

        try:
            latitude_binary = bitstring[89:116]
            self.Latitude = AIS.Utilities.decode_latitude(latitude_binary)
        except:
            print('Error - latitude')
            return False

        try:
            course_over_ground = bitstring[116:128]
            cog_int = int(course_over_ground, 2)
            # Divide by 10 to remove 0.1 degree precision
            actual_cog = int(cog_int / 10)
            # Now make sure leading zeros
            self.COG = ("{:03d}".format(actual_cog))
        except:
            print('Error - COG')
            return False

        try:
            time_stamp = bitstring[137:143]
            time_stamp_int = int(time_stamp,2)
            self.TimeStamp = time_stamp_int
        except:
            print('Error - Timestamp')
            return False

        try:
            position_accuracy = bitstring[60:61]
            true_heading = bitstring[128:137]

            maneuver_indicator = bitstring[143:145]
            spare = bitstring[145:148]
            raim = bitstring[148:149]
            radio_status = bitstring[149:168]
        except:
            print('Error in unprocessed fields')
            return False

    def decode_navigation_status(self, navigation_status):

        navigation_status_int = int(navigation_status, 2)

        if navigation_status_int == 0:
            return 'Under way using engine'
        elif navigation_status_int == 1:
            return 'At anchor'
        elif navigation_status_int == 2:
            return 'Not under command'
        elif navigation_status_int == 3:
            return 'Restricted manoeuverability'
        elif navigation_status_int == 4:
            return 'Constrained by draught'
        elif navigation_status_int == 5:
            return 'Moored'
        elif navigation_status_int == 6:
            return 'Aground'
        elif navigation_status_int == 7:
            return 'Engaged in Fishing'
        elif navigation_status_int == 8:
            return 'Under way sailing'
        elif navigation_status_int == 9-13:
            return 'Reserved'
        elif navigation_status_int == 14:
            return 'AIS - SART is active'
        elif navigation_status_int == 15:
            return 'Not defined'
        else:
            return 'Unknown value'

    '''
    0 = not turning
    1…​126 = turning right at up to 708 degrees per minute or higher
    1…​-126 = turning left at up to 708 degrees per minute or higher
    127 = turning right at more than 5deg/30s (No TI available)
    -127 = turning left at more than 5deg/30s (No TI available)
    128 (80 hex) indicates no turn information available (default)
    '''
    def decode_rate_of_turn(self, rate_of_turn):

        rate_of_turn_int = int(rate_of_turn, 2)

        if rate_of_turn_int == 0:
            return 'Not Turning'
        elif rate_of_turn_int == 127:
            return 'Turning to Starboard'
        elif rate_of_turn_int == -127:
            return 'Turning to Port'
        elif 1 <= rate_of_turn_int <= 126:
            return 'Turning to Starboard'
        elif -126 <= rate_of_turn_int <= 1:
            return 'Turning to Port'
        else:
            return 'Unknown rate of turn'

    def decode_sog(self, sog):
        sog_int = int(sog, 2)

        if sog_int == 1023:
            return"Speed not available"
        elif sog_int ==1022:
            return "Way too fast!"
        elif 0 <= sog_int <= 102:
            return sog_int
        else:
            return 'Unknown SOG'





