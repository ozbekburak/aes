import RoundKey as RK
import Encryption as ET
input_bytes = [
    ["32", "88", "31", "e0"],
    ["43", "5a", "31", "37"],
    ["f6", "30", "98", "07"],
    ["a8", "8d", "a2", "34"]
]
cipher_key = [
    ["2b","28","ab","09"],
    ["7e","ae","f7","cf"],
    ["15","d2","15","4f"],
    ["16","a6","88","3c"]
]

def PrintSomething(text,description):
    print("...",description,"...")
    for i in range(1):
        for k in range(0,text.__len__()):
            if(k>0 & k<4):
                print("\n")
            for j in range(0,text.__len__()):
                print (text[k][j],"\t",end='')
    print("\n")



def main():

    state = ET.AddRoundKey(input_bytes,cipher_key)
    PrintSomething(input_bytes,"plaintext")
    PrintSomething(cipher_key,"cipherkey")

    for i in range (1,10): # starting 9 rounds

        state = ET.SubBytes(state)
        state = ET.ShiftRows(state)
        state = ET.MixColumns(state)

        if (i == 1):
            state = ET.AddRoundKey(state, RK.RoundKey1())
        if (i == 2):
            state = ET.AddRoundKey(state, RK.RoundKey2())
        if (i == 3):
            state = ET.AddRoundKey(state, RK.RoundKey3())
        if (i == 4):
            state = ET.AddRoundKey(state, RK.RoundKey4())
        if (i == 5):
            state = ET.AddRoundKey(state, RK.RoundKey5())
        if (i == 6):
            state = ET.AddRoundKey(state, RK.RoundKey6())
        if (i == 7):
            state = ET.AddRoundKey(state, RK.RoundKey7())
        if (i == 8):
            state = ET.AddRoundKey(state, RK.RoundKey8())
        if (i == 9):
            state = ET.AddRoundKey(state, RK.RoundKey9())

    state = ET.SubBytes(state)
    state = ET.ShiftRows(state)
    state = ET.AddRoundKey(state,RK.RoundKey10())
    PrintSomething(state,"encrypted text")

main()

