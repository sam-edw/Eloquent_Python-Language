'''
Mencetak bilangan prima dalam suatu rentang tertentu.
Contoh while-else loop yang pythonic.
    Jika loop sudah selesai dijalani tapi if clause tidak terjadi
    artinya tidak terjadi break sampai habis parameter loop control
    maka else clause dieksekusi,
    tetapi jika terjadi break maka else clause diloncati
'''
i = 2
while i < 100:
    j = 2
    while j*j <= i:  # selama j kurang/sama dari akar i
        if i%j == 0: # jika i habis dibagi j
            break    # artinya bukan bilangan prima
        j = j + 1
    else:            # jika semua kemungkinan pembagi sudah dicoba
        print(f'{i} bilangan prima')
    i = i + 1
