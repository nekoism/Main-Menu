def start () :
    import random
    import Mainmenu
    from wlcm import welcome_message
    from wlcm import exit_program

    welcome_message('RNG MINI GAME')

    lokasi_air = random.randint(1,4)


    nama = input('masukkan nama anda : ')

    while nama == '' :
        nama = input('Masukkan dulu nama Anda : ')
        


    bentuk_gelas = '|___|'
    gelas_kosong = [bentuk_gelas] * 4
    gelas_isi = gelas_kosong.copy()

    gelas_isi[lokasi_air - 1] = '|███|'

    gelas_kosong = ' '.join(gelas_kosong)
    gelas_isi = ' '.join(gelas_isi)

    print()
    print(f'Hallo {nama} coba perhatikan Gelas dibawah ini : \n {gelas_kosong}')
    print()
    
    while True :
        pilihan_user = int(input('Lokasi air berada di gelas no berapa? : ' ))

        konfirmasi = input('\napakah kamu yakin dengan pilihanmu Y/N? : ')

        if konfirmasi == 'N' :
            print('Pastikan pilihan anda benar!!!')
            continue
        elif konfirmasi == 'Y' :
            break      
        else:
            print('Perhatikan huruf besarnya dan cuman menerima jawaban Y/N')
            continue      
    if pilihan_user == lokasi_air :
        print (f'SELAMAT KAMU MENANG!!! Lokasi air berada di gelas no : {lokasi_air} \n {gelas_isi}')
    elif pilihan_user > 4 :
        print (f'KOCAK!!!! Gelas cuman 4 Boss, gelas yang berisi air ada di gelas no : {lokasi_air} \n {gelas_isi}')
    else:
        print (f'Kamu kalah!!!! lokasi air berada di gelas no : {lokasi_air} \n {gelas_isi}')
    
    ulang = input('\nApakah kamu ingin melanjutkan game? Y/N :  ')
    if ulang == 'N':
        Mainmenu.main()
    
                   
if __name__ == '__main__' :
    start()