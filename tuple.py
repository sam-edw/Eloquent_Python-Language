from array import array
from collections import deque

print('\nRagam struktur data dalam Python bersama metoda masing masing:')
print('~'*62)
'''
tuple, kumpulan objek yang dapat diiterasi
tuple comprehension membentuk suatu fungsi generator, bukannya tuple
    mengingat sifatnya yang immutable,
    menjadi tidak logis jika diisi berulang kali melalui for-comprehension
unpacking operator asteriks * memiliki efek mengiterasi generator
'''
for klas in (tuple, list, dict, set, str, array, deque):   # for'each'-in loop dari iterable tuple
    metodas = (m for m in dir(klas) if '_' not in m)   # membentuk suatu generator
    print(klas,':')
    print(*metodas,'\n')   # asterix * unpacking generator, mengeluarkan elemen-2 nya.
