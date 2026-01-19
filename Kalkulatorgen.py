def start () :
    from wlcm import welcome_message 
    from wlcm import exit_program
    import Mainmenu

    welcome_message ('KALKULATOR GEN')

    nama_user = input('masukkan nama kalian : ')
    while True :
        tahun_kelahiran = int(input(f'hallo {nama_user} masukkan tahun kelahiran kalian : '))
        if tahun_kelahiran >= 1928 and tahun_kelahiran <= 1945 :
            print (f' Wow sepuh, izin puhh sepuh. kamu termasuk kedalam "Silent Generation" pak {nama_user}.')
            break
        elif tahun_kelahiran > 1945 and tahun_kelahiran <=1964 :
            print (f'Kamu sudah tua pak {nama_user}, cucunya udah berapa pak? ^-^ kamu termasuk kedalam "Gen Baby Boomers".')
            break
        elif tahun_kelahiran > 1965 and tahun_kelahiran <=1980 :
            print(f'Info loker dong pak {nama_user} hehehhee, kamu termasuk kedalam "Gen X" pak.')
            break
        elif tahun_kelahiran > 1981 and tahun_kelahiran <= 1996 : 
            print(f'Sejenis Artefak kuno kamu pak {nama_user} hehheeh, kamu termasuk kedalam Gen "Y" pak.')
            break
        elif tahun_kelahiran > 1997 and tahun_kelahiran <= 2012 :
            print(f'Wahh kita se Gen bang {nama_user}, kita ada di "Gen Z"!!!')
            break
        elif tahun_kelahiran > 2013 :
            print(f'Aduh cil cil, pantesan dari tadi bau kencur. kamu masuk ke "Gen Alpha" {nama_user}')
            break
        else :
            print(f'Kamu Robot ya? {nama_user}')
            continue
    ulang = input('\nApakah kamu masih ingin menggunakan program ini? Y/N : ')
    if ulang == 'N' :
        Mainmenu.main()

if __name__ == '__main__' :
    start()
    