import GaluaSpaces as GS
s_box = [
        ["63","7C","77","7B","F2","6B","6F","C5","30","01","67","2B","FE","D7","AB","76"],
        ["CA","82","C9","7D","FA","59","47","F0","AD","D4","A2","AF","9C","A4","72","C0"],
        ["B7","FD","93","26","36","3F","F7","CC","34","A5","E5","F1","71","D8","31","15"],
        ["04","C7","23","C3","18","96","05","9A","07","12","80","E2","EB","27","B2","75"],
        ["09","83","2C","1A","1B","6E","5A","A0","52","3B","D6","B3","29","E3","2F","84"],
        ["53","D1","00","ED","20","FC","B1","5B","6A","CB","BE","39","4A","4C","58","CF"],
        ["D0","EF","AA","FB","43","4D","33","85","45","F9","02","7F","50","3C","9F","A8"],
        ["51","A3","40","8F","92","9D","38","F5","BC","B6","DA","21","10","FF","F3","D2"],
        ["CD","0C","13","EC","5F","97","44","17","C4","A7","7E","3D","64","5D","19","73"],
        ["60","81","4F","DC","22","2A","90","88","46","EE","B8","14","DE","5E","0B","DB"],
        ["E0","32","3A","0A","49","06","24","5C","C2","D3","AC","62","91","95","E4","79"],
        ["E7","C8","37","6D","8D","D5","4E","A9","6C","56","F4","EA","65","7A","AE","08"],
        ["BA","78","25","2E","1C","A6","B4","C6","E8","DD","74","1F","4B","BD","8B","8A"],
        ["70","3E","B5","66","48","03","F6","0E","61","35","57","B9","86","C1","1D","9E"],
        ["E1","F8","98","11","69","D9","8E","94","9B","1E","87","E9","CE","55","28","DF"],
        ["8C","A1","89","0D","BF","E6","42","68","41","99","2D","0F","B0","54","BB","16"]
        ]

def AddRoundKey(input_bytes,cipher_key):
    for i in range(0,input_bytes.__len__()):
        for k in range(0,input_bytes.__len__()):
            a = hex(int(input_bytes[i][k], 16) ^ int(cipher_key[i][k], 16)) # matrix > decimal > hex
            input_bytes[i][k] = a

    return (input_bytes)

def SubBytes(xored): # example: we need sbox[1][9] for input_bytes[0][0] (it equals 19 after addroundkey)
    for i in range(0,xored.__len__()):
        for k in range(0,xored.__len__()):
             m = (int(int(xored[i][k],16) / 16)) # 19 / 10 = 1
             n = (int(int(xored[i][k],16) % 16)) # 19 % 10 = 9 so we can look s_box matrix for 19
             xored[i][k] = s_box[m][n]

    return xored

def ShiftRows(shifted):
    shift_1 = GS.shift(shifted[1],-1)
    shift_2 = GS.shift(shifted[2],-2)
    shift_3 = GS.shift(shifted[3],-3)
    shifted[1] = shift_1
    shifted[2] = shift_2
    shifted[3] = shift_3

    return (shifted)

def MixColumns(mixed):

    for i in range(4):
        s0 = GS.multiply_by_02(int(mixed[0][i], 16)) ^ GS.multiply_by_03(int(mixed[1][i], 16)) ^ int(mixed[2][i], 16) ^ int(mixed[3][i], 16)
        #print (hex(s0))
        s1 = int(mixed[0][i], 16) ^ GS.multiply_by_02(int(mixed[1][i], 16)) ^ GS.multiply_by_03(int(mixed[2][i], 16)) ^ int(mixed[3][i], 16)
        #print (hex(s1))
        s2 = int(mixed[0][i], 16) ^ int(mixed[1][i], 16) ^ GS.multiply_by_02(int(mixed[2][i], 16)) ^ GS.multiply_by_03(int(mixed[3][i], 16))
        #print (hex(s2))
        s3 = GS.multiply_by_03(int(mixed[0][i], 16)) ^ int(mixed[1][i], 16) ^ int(mixed[2][i], 16) ^ GS.multiply_by_02(int(mixed[3][i], 16))
        #print (hex(s3))

        mixed[0][i] = hex(s0)
        mixed[1][i] = hex(s1)
        mixed[2][i] = hex(s2)
        mixed[3][i] = hex(s3)
    return mixed
