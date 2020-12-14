from korisnici.korisnici import prijava
from knjige.knjiga import prikazi_knjige
from knjige.knjiga import pretrazi_knjige
#from korisnici.administrator import meni_administrator


def main():
    ulogovani_korisnik = prijava()
    print(ulogovani_korisnik)

    if ulogovani_korisnik is not None:

        if ulogovani_korisnik["tip_korisnika"] == "Administrator":
            meni_administrator()
        elif ulogovani_korisnik["tip_korisnika"] == "Menadzer":
            pass
        elif ulogovani_korisnik["tip_korisnika"] == "Prodavac":
            pass
        else:
            print("Greska. Nepostojeca uloga korisnika.")



main()