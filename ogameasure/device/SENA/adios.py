
class adios(object):

    off = {'level_off':":17010000000000,000000000011\r\n"}

    att = {
            'att1_0dB':":17011111100000,000000000010\r\n",
            'att1_1dB':":17011111100000,100000000011\r\n",
            'att1_2dB':":17011111100000,010000000011\r\n",
            'att1_3dB':":17011111100000,110000000010\r\n",
            'att1_4dB':":17011111100000,001000000011\r\n",
            'att1_5dB':":17011111100000,101000000010\r\n",
            'att1_6dB':":17011111100000,011000000010\r\n",
            'att1_7dB':":17011111100000,111000000011\r\n",
            'att1_8dB':":17011111100000,000100000011\r\n",
            'att1_9dB':":17011111100000,100100000010\r\n",
            'att1_10dB':":17011111100000,010100000010\r\n",
            'att1_11dB':":17011111100000,110100000011\r\n",
            'att1_12dB':":17011111100000,001100000010\r\n",
            'att1_13dB':":17011111100000,101100000011\r\n",
            'att1_14dB':":17011111100000,011100000011\r\n",
            'att1_15dB':":17011111100000,111100000010\r\n",
            'att1_16dB':":17011111100000,000010000011\r\n",
            'att1_17dB':":17011111100000,100010000010\r\n",
            'att1_18dB':":17011111100000,010010000010\r\n",
            'att1_19dB':":17011111100000,110010000011\r\n",
            'att1_20dB':":17011111100000,001010000010\r\n",
            'att1_21dB':":17011111100000,101010000011\r\n",
            'att1_22dB':":17011111100000,011010000011\r\n",
            'att1_23dB':":17011111100000,111010000010\r\n",
            'att1_24dB':":17011111100000,000110000010\r\n",
            'att1_25dB':":17011111100000,100110000011\r\n",
            'att1_26dB':":17011111100000,010110000011\r\n",
            'att1_27dB':":17011111100000,110110000010\r\n",
            'att1_28dB':":17011111100000,001110000011\r\n",
            'att1_29dB':":17011111100000,101110000010\r\n",
            'att1_30dB':":17011111100000,011110000010\r\n",
            'att1_31dB':":17011111100000,111110000011\r\n",
            'att2_0dB':":17010000011111,000000000010\r\n",
            'att2_1dB':":17010000011111,000001000011\r\n",
            'att2_2dB':":17010000011111,000000100011\r\n",
            'att2_3dB':":17010000011111,000001100010\r\n",
            'att2_4dB':":17010000011111,000000010011\r\n",
            'att2_5dB':":17010000011111,000001010010\r\n",
            'att2_6dB':":17010000011111,000000110010\r\n",
            'att2_7dB':":17010000011111,000001110011\r\n",
            'att2_8dB':":17010000011111,000000001011\r\n",
            'att2_9dB':":17010000011111,000001001010\r\n",
            'att2_10dB':":17010000011111,000000101010\r\n",
            'att2_11dB':":17010000011111,000001101011\r\n",
            'att2_12dB':":17010000011111,000000011010\r\n",
            'att2_13dB':":17010000011111,000001011011\r\n",
            'att2_14dB':":17010000011111,000000111011\r\n",
            'att2_15dB':":17010000011111,000001111010\r\n",
            'att2_16dB':":17010000011111,000000000111\r\n",
            'att2_17dB':":17010000011111,000001000110\r\n",
            'att2_18dB':":17010000011111,000000100110\r\n",
            'att2_19dB':":17010000011111,000001100111\r\n",
            'att2_20dB':":17010000011111,000000010110\r\n",
            'att2_21dB':":17010000011111,000001010111\r\n",
            'att2_22dB':":17010000011111,000000110111\r\n",
            'att2_23dB':":17010000011111,000001110110\r\n",
            'att2_24dB':":17010000011111,000000001110\r\n",
            'att2_25dB':":17010000011111,000001001111\r\n",
            'att2_26dB':":17010000011111,000000101111\r\n",
            'att2_27dB':":17010000011111,000001101110\r\n",
            'att2_28dB':":17010000011111,000000011111\r\n",
            'att2_29dB':":17010000011111,000001011110\r\n",
            'att2_30dB':":17010000011111,000000111110\r\n",
            'att2_31dB':":17010000011111,000001111111\r\n",
        }

    def __init__(self, com):
        self.com = com
        self.com.open()
        pass

    def _set_att(self, no, value):
        self.com.send(self.att["att{0}_{1}dB".format(no, value)].encode())
        return

    def get_att1(self):
        self.com.send(self.off['level_off'].encode())
        while True:
            try:
                temp = self.com.recv()
                if temp.find(':')==-1: continue
                else: pass
                #print temp
                break
            except communicator.CommunicatorTimeout:
                print('(error) att1')
                continue
            continue
        time.sleep(0.1)

        do1 = int(temp[-16])*1
        do2 = int(temp[-15])*2
        do3 = int(temp[-14])*4
        do4 = int(temp[-13])*8
        do5 = int(temp[-11])*16
        att1 = do1+do2+do3+do4+do5
        return att1

    def get_att2(self):
        self.com.send(self.off['level_off'].encode())
        while True:
            try:
                temp = self.com.recv()
                if temp.find(':')==-1: continue
                else: pass
                break
            except communicator.CommunicatorTimeout:
                print('(error) att2')
                continue
            continue
        time.sleep(0.1)

        do6 = int(temp[-10])*1
        do7 = int(temp[-9])*2
        do8 = int(temp[-8])*4
        do9 = int(temp[-6])*8
        do10 = int(temp[-5])*16
        att2 = do6+do7+do8+do9+do10
        return att2
