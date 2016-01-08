#!/usr/bin/env python
# coding=utf-8

def mycrc32(szString, dwPolynomial):
    m_pdwCrc32Table = [0 for x in range(0,256)]
    #dwPolynomial = 0xEDB88320;#0x04c11db7
    dwCrc = 0
    for i in range(0,255):
        dwCrc = i
        for j in [8,7,6,5,4,3,2,1]:
            if dwCrc & 1:
                dwCrc = (dwCrc >> 1) ^ dwPolynomial
            else:
                dwCrc >>= 1
        m_pdwCrc32Table[i] = dwCrc
    dwCrc32 = 0xFFFFFFFF
    for i in szString:
        b = ord(i)
        dwCrc32 = ((dwCrc32) >> 8) ^ m_pdwCrc32Table[(b) ^ ((dwCrc32) & 0x000000FF)]
    dwCrc32 = dwCrc32 ^ 0xFFFFFFFF
    return dwCrc32


if __name__ == "__main__":
    datak = 'D8557E4A13516F7A5ECC1FEB7FF3DAB2'
    crc32 = mycrc32(datak, 0xEDB88320)
    print ('crc32 0xEDB88320 0x%X' % crc32)
    crc32 = mycrc32(datak, 0x04c11db7)
    print ('crc32 0x04c11db7 0x%X' % crc32)
    crc32 = mycrc32(datak, 0x77073096)
    print ('crc32 0x77073096 0x%X' % crc32)
