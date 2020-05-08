import NMEA.Instrument
import AIS.MessageType1

'''
Background at 
https://gpsd.gitlab.io/gpsd/AIVDM.html
'''


class AISReceiver(NMEA.Instrument.Generic0183):
    def __init__(self):        # Init for instances
        super().__init__()
        # There are several possible talker IDs
        self.talker_id = ''
        # The count of fragments in the currently accumulating message
        self.count_of_fragments = 0
        # The fragment number of this sentence
        self.fragment_number = 0
        # Sequential message ID for multi-sentence messages
        self.sequential_message_id = 0
        # AIS Channel A is 161.975Mhz (87B); AIS Channel B is 162.025Mhz (88B).
        self.AISChannel = ''
        # Payload
        self.raw_payload = ''
        self.processed_payload = []
        # The number of fill bits requires to pad the data payload to a 6 bit boundary
        self.fillbits = ''
        self.checksum = ''
        self.message_type = ''

    def parse(self, nmea_full_sentence):
        # Break it up into fields
        list_of_values = nmea_full_sentence.split(',')
        # Process the talker ID and assign it to a property
        talker = list_of_values[0][1:3]
        self.get_talker_id(talker)
        # Assign the rest of the fields to properties
        self.get_list_of_values(list_of_values)
        # Now decode the payload
        self.payload_armoring()
        # Get the message type
        message_type_field = self.processed_payload[0]
        self.get_message_type(message_type_field)
        self.clear_data()

    def get_list_of_values(self, list_of_values):
        try:
            if list_of_values[0][3:] == 'VDM':
                self.count_of_fragments = list_of_values[1]
                self.fragment_number = list_of_values[2]
                self.sequential_message_id = list_of_values[3]
                self.AISChannel = list_of_values[4]
                self.raw_payload = list_of_values[5]
                lastbit = list_of_values[6].split('*')
                self.fillbits = lastbit[0]
                self.checksum = lastbit[1]
            elif list_of_values[0][3:] == 'VDO':
                print('Found a AIS VDO message but will not process')
            else:
                print('Unknown AIS sentence')
        except ValueError:
            print('[GPS-parse] Error parsing sentence')

    def get_talker_id(self, talker):

        if talker == 'AB':
            talker_id = 'Base AIS station'
        elif talker == 'DB':
            talker_id = 'Dependent AIS Base Station'
        elif talker == 'AI':
            talker_id = 'Mobile AIS Station'
        elif talker == 'AN':
            talker_id = 'Aid to navigation AIS Station'
        elif talker == 'AR':
            talker_id = 'AIS Receiving Station'
        elif talker == 'AS':
            talker_id = 'Limited base Station'
        elif talker == 'AT':
            talker_id = 'AIS transmitting Station'
        elif talker == 'AX':
            talker_id = 'AIS repeater Station'
        elif talker == 'SA':
            talker_id = 'Physical shore Station'
        else:
            talker_id = talker + ' unidentified'

        self.talker_id = talker_id

    def payload_armoring(self):
        print(self.raw_payload)
        for character in self.raw_payload:
            decoded_character = ord(character) - 48
            if decoded_character > 40:
                decoded_character = decoded_character -8
            self.processed_payload.append(decoded_character)

    def get_message_type(self, message_type_field):
        if message_type_field == 1:
            self.message_type = 'Position Report Class A'
            message_type1 = NMEA.MessageType1.Message1()
            message_type1.decode(self.processed_payload)

        if message_type_field == 2:
            self.message_type = 'Position Report Class A (Assigned schedule)'
        if message_type_field == 3:
            self.message_type = 'Position Report Class A (Response to interrogation)'
        if message_type_field == 4:
            self.message_type = 'Base Station Report'
        if message_type_field == 5:
            self.message_type = 'Static and Voyage Related Data'
        if message_type_field == 6:
            self.message_type = 'Binary Addressed Message'
        if message_type_field == 7:
            self.message_type = 'Binary Acknowledge'
        if message_type_field == 8:
            self.message_type = 'Binary Broadcast Message'
        if message_type_field == 9:
            self.message_type = 'Standard SAR Aircraft Position Report'
        if message_type_field == 10:
            self.message_type = 'UTC and Date Inquiry'
        if message_type_field == 11:
            self.message_type = 'UTC and Date Response'
        if message_type_field == 12:
            self.message_type = 'Addressed Safety Related Message'
        if message_type_field == 13:
            self.message_type = 'Safety Related Acknowledgement'
        if message_type_field == 14:
            self.message_type = 'Safety Related Broadcast Message'
        if message_type_field == 15:
            self.message_type = 'Interrogation'
        if message_type_field == 16:
            self.message_type = 'Assignment Mode Command'
        if message_type_field == 17:
            self.message_type = 'DGNSS Binary Broadcast Message'
        if message_type_field == 18:
            self.message_type = 'Standard Class B CS Position Report'
        if message_type_field == 19:
            self.message_type = 'Extended Class B Equipment Position Report'
        if message_type_field == 20:
            self.message_type = 'Data Link Management'
        if message_type_field == 21:
            self.message_type = 'Aid-to-Navigation Report'
        if message_type_field == 22:
            self.message_type = 'Channel Management'
        if message_type_field == 23:
            self.message_type = 'Group Assignment Command'
        if message_type_field == 24:
            self.message_type = 'Static Data Report'
        if message_type_field == 25:
            self.message_type = 'Single Slot Binary Message'
        if message_type_field == 26:
            self.message_type = 'Multiple Slot Binary Message With Communications State'
        if message_type_field == 27:
            self.message_type = 'Position Report For Long-Range Applications'

    def clear_data(self):

        self.talker_id = ''
        self.count_of_fragments = 0
        self.fragment_number = 0
        self.sequential_message_id = 0
        self.AISChannel = ''
        self.raw_payload = ''
        self.processed_payload = []
        self.fillbits = ''
        self.checksum = ''
        self.message_type = ''

