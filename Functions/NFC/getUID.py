from __future__ import print_function
from smartcard.Exceptions import NoCardException
from smartcard.System import readers
from smartcard.util import toHexString
from smartcard.scard import *

def getCard():
    for reader in readers():
        try:
            connection = reader.createConnection()
            connection.connect()
            return toHexString(connection.getATR()).replace(" ", "")
        except NoCardException:
            #print(reader, 'no card inserted')
            pass

def getUID():
    card2 = getCard()
    #print(card2)
    if card2 == "3B8F8001804F0CA000000306030001000000006A":
        hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)

        assert hresult == SCARD_S_SUCCESS

        hresult, lires = SCardListReaders(hcontext, [])

        assert len(lires) > 0

        lire = lires[0]

        hresult, hcard, dwActiveProtocol = SCardConnect(
            hcontext,
            lire,
            SCARD_SHARE_SHARED,
            SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)

        hresult, response = SCardTransmit(hcard, dwActiveProtocol, [0xFF, 0xCA, 0x00, 0x00, 0x00])

        for i in range(len(response)):
            temp = response[i]
            response[i] = hex(temp)

        return response
