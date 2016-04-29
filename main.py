import random
        
def scaleselect():
    while True:
        scale = input("Pick a key: 1=ionian, 2=dorian, 3=phrygian, 4=lydian, 5=mixolydian, 6=aeolian, 7=harmonic, 8=random: ")
        if scale in [1,2,3,4,5,6,7]:
            return scale
        elif scale == 8:
            return random.randrange(1,7)
        else:
            print("Please use an appropriate input.")
            scaleselect()
def length():
    while True:
        len = input("How many chords do you want in your progression? ")
        if len in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
            return len
        elif len<1 or 20<len:
            print("Too extreme! 0<length<20")
            length()
        else:
            print("Please use an appropriate integer value between 1 and 20.")
            length()

def progressiongen(scale,length):
    progression = []
    scalechords = [
        ["Ionian",'I','ii','iii','IV','V^','vi','vii*'],
        ["Dorian",'i','ii','III','IV^','v','vi*','VII'],
        ["Phrygian",'i','II','III^','iv','v*','VI','vii'],
        ["Lydian",'I','II^','iii','iv*','V','vi','vii'],
        ["Mixolydian",'I^','ii','iii*','IV','v','vi','VII'],
        ["Aeolian",'i','ii*','III','iv','v','VI','VII^'],
        ["Harmonic Minor",'i','ii*','III','iv','V','VI','vii*']
        ]
    count = length
    progression.append(scalechords[scale - 1][0])
    while count > 0:
        if 0 < scale < 8:
            progression.append(scalechords[scale - 1][random.randrange(1,7)])
            count -= 1
    return progression

def runit():
        result = progressiongen(scaleselect(),length())
        tempo = random.randrange(40,120)
        print result[0]
        print result[1:]
        print "Tempo:"
        print tempo
        repeat = raw_input("Again? N for no, else repeat: ")
        if repeat.lower() != "n":
            runit()
runit()
