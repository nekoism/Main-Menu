from wlcm import welcome_message
import RNGminigamev2
import MenuKrustyCrab
import Kalkulatorgen
from wlcm import exit_program
 

def Mainmenu() :
    
    pilihan_user = int(input('\nMain Menu : \n1.RNG Mini Game\n2.MenuKrustyCrab\n3.Kalkulatorgen\n4.Exit\n\nSilahkan pilih menu mana yang ingin kalian akses dengan memasukkan nomor menu : '))
    while True :
        if pilihan_user == 1 :
            RNGminigamev2.start()
        elif pilihan_user == 2 :
            MenuKrustyCrab.start()
        elif pilihan_user == 3 :
            Kalkulatorgen.start()
        elif pilihan_user == 4 :
            break
        elif pilihan_user == '':
            pilihan_user = int(input('tolong hanya masukkan angka 1/2/3/4!!! : '))
        else:
            pilihan_user = int(input('tolong hanya masukkan angka 1/2/3/4!!! : '))
            
        
                
 
def main():
    welcome_message('Main menu utama')
    Mainmenu()
    exit_program()

if __name__ == '__main__' :
    main()


   
    