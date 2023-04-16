# -*- coding: utf-8 -*-

import sys
import re
import os

def tjtm(r):
    owd = os.getcwd()
    rtx = os.path.basename(r)
    rty = os.path.splitext(rtx)
    rtz = rty[0]
    c=1
    f=open(r,"rb")
    try:
        os.mkdir(rtz)
    except FileExistsError:
        print('경고. ' + rtz + ' 폴더가 이미 있습니다. ' '프로그램이 아마도 오작동할 수 있습니다. ' + rtz + ' 폴더를 삭제해주세요.')  
    os.chdir(rtz)
    f.seek(20)
    vv=f.read(4)
    vv_int = int.from_bytes(vv, "little")
    print(vv_int)
    #f.seek(44)
    nextdata = 0
    for i in range(0, vv_int):
        if i != vv_int:
            f.seek(132*i+44)
        filenameraw=f.read(128)
        size=int.from_bytes(f.read(4), "little")
        filename = re.sub(b'\x00', b'', filenameraw).decode('ascii')
        mm=filename.split("/") # 디렉토리 삭제 시작
        filenameonly=mm[-1]
        print(filenameonly)
        print(size)
        z=open(filenameonly,'bw')
        f.seek(132*vv_int+44+nextdata)
        print(132*vv_int+44+nextdata)
        data = f.read(size)
        z.write(data)
        z.close()
        nextdata = nextdata + size

print("")
print("Project Level UPPER")
print("UPPER KIT EXTRA 2")
print("INEvangelion HAMGUARD (PROTOTYPE)")
print("")
rrr = sys.argv[1]
tjtm(rrr)      