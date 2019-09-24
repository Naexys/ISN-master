from Functions.Controls.Keyboard.keyboard_pressed import *
from Objects.Entity.Character.Character import *
from intValues import *
from Functions.NFC.testuid import *
from Functions.NFC.getUID import *
if raspberry:
    from Functions.Server.client import *

def switch_heroes():
    if raspberry:
        uid = getUID()

    if keyboard_pressed() == "F1" or (nfc and uid == ['0xb0', '0xfa', '0x5b', '0x56', '0x90', '0x0']):
        man._set_gender("fireman/")

        if raspberry:
            msgx = "fireman"
            Sock.send(msgx.encode())
            time.sleep(0.1)

    elif keyboard_pressed() == "F2" or (nfc and uid == ['0x50', '0xe2', '0x5a', '0x56', '0x90', '0x0']):
        man._set_gender("knight/")

        if raspberry:
            msgx = "knight"
            Sock.send(msgx.encode())
            time.sleep(0.1)


