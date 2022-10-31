from ast import match_case
from distutils.command.clean import clean
from time import sleep
from rich import print
# from play import *
from stats import *
import winsound
import sys
import pyfiglet
import os

stat = Statystyki()
def cleaning():
    os.system("cls" if os.name=="nt" else "clear")

def gameover_beep():
    winsound.Beep(440,250)
    winsound.Beep(415,250)
    winsound.Beep(391,250)
    winsound.Beep(369,750)
    
def endgame_beep():
    winsound.Beep(264,250)
    winsound.Beep(528,250)
    winsound.Beep(264,250)

def gameover(type):
    cleaning()
    print(pyfiglet.figlet_format("Game over..."))
    gameover_beep()
    if type == 'studia':    
        print("[orange]Niestety, Adam nie zaliczył wymaganych egzaminów i został skreślony z listy studentów :(")
    if type == 'wakacje':
        print("[orange]Niestety Adam uległ wypadkowi, przez co nie może kontynuować studiów :(((")    
    x = input("\nKliknij enter, aby powrócić do Menu...")
    main()
    
def endgame():
    cleaning()
    print(pyfiglet.figlet_format("BRAWO!!!"))
    endgame_beep()
    print("\n\n[red]Gratulacje!!!")
    print("Udało Ci się ukończyć grę!\n\n")
    x = input("Kliknij enter, aby powrócić do Menu...")
    
    
    
    
def printing(string):
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.03)
    
def gwint(semestr):
    stat.set_upojenie()
    cleaning()
    text0 ="Adam pojawia się w znanym mu już studenckim klubie.\nJak zawsze na wstępie zamawia przy barze jedno piwko i siada przy stole razem ze swoimi kolegami.\nRozpoczynają się rozmowy o wszystkim i niczym.\nW końcu każde z nich opróżnia zawartoś swojego kufla. Nasz bohater musi podjąć\ndecyzję, czy zostaje dalej, co wiąże się z wypiciem kolejnego,\nczy wraca do domu i odpoczywa przed egzaminem.\n"
    printing(text0)
    stat.pije()
    upoj = int(stat.get_upojenie())
    while 1 and upoj < 5 :
        stat.printupojenie()
        print("Czy zamawiasz kolejne piwo?")
        print("1.Tak")
        print("2.Nie")
        odpowiedz = input(">>>")
        if odpowiedz == '1':
            stat.pije()
            upoj = int(stat.get_upojenie())
        else:
            break
    
    if upoj == 5:
        cleaning()
        text0 = "Adam przebudza się z silnym bólem głowy. Kompletnie nie pamięta jak wrócił do domu.\nSpogląda na zegarek...\n\n"
        text1 = "~~Cholera jasna! Już 11:00? Przecież miałem iść na egzamin na 10:00... Co ja teraz zrobię?~~\n"
        text2 = "\nNiestety jedyne co mu pozostało, to pogodzić się z niezaliczonym przedmiotem :(\n\n"
        text3 = "~~A mogłem tyle nie pić :(((~~"
        printing(text0)
        printing(text1)
        printing(text2)
        printing(text3)
        stat.niezdal()
        end = stat.get_przedmioty()
        x = input("\n\nKliknij enter, aby kontynuować...")
        if end == 0:
            gameover('studia')
        
        
    else:
        text0 = "Adaś grzecznie wraca do domu i kładzie się spać..."
        print()
        printing(text0)
        x = input("\n\nKliknij enter, aby kontynuować...")  
        if semestr == 1:
            egzamin1()
        elif semestr == 2:
            egzamin2()
        elif semestr == 3:
            egzamin3()
        elif semestr == 4:
            egzamin4()
            
         
    
    
def piwo1():
    text0 = "\n-Dobra, ale tylko jedno. W najgorszym wypadku kilka, jakoś to będzie!"
    printing(text0)
    x = input("\n\nKliknij enter, aby kontynuować...")
    gwint(1)
    
def odmowa1():
    text0 = "\n-Sorki chłopaki, muszę to zaliczyć. Nie wybaczę sobie jak dostanę dwóję! Lećcie beze mnie, ja spadam się uczyć.\n\n"
    text1 = "Adam oddala się od kolegów, wraca do domu i pilnie przyswaja informacje o przestrzeniach liniowych, macierzach itp."
    printing(text0)
    printing(text1) 
    x = input("\n\nKliknij enter, aby kontynuować...")
    egzamin1()
    
def egzamin1():
    cleaning()
    text0 = 'Adam budzi się rano. Spogląda na zegarek.\n\n'
    text1 = "~~Dobra, jest 9:00. Zdążę dojść na uczelnię, egzamin na 10:00.~~\n\n"
    text2 = "Wstaje z łóżka, je lekkie śniadanie.\n\n"
    text3 = "~~Cholera, co zrobić, żeby się nie stresować? Dam radę, nie ma innej opcji.~~\n\n"
    text4 = "Nasz bohater ubiera się szybko i wychodzi z pokoju...\n"
    cleaning()
    text5 = "Przed uczelnią stoją jego kumple, którzy tak samo jak on przezywają i się stresują.\nWchodzą do sali wykładowej i każdy dostaje arkusz z zadaniami.\n\n"
    text6 = "Mija dłuższa chwila, Adam rozwiązał sporo zadań.\nMa problem z przypomnieniem sobie jednej definicji, poprawny wybór może zadecydowac o jego pozytywnej ocenie...\n\n"
    text7 = "~~Jak to było z tą macierzą? Nie pamiętam!~~\n\n"
    printing(text0)
    printing(text1)
    printing(text2)
    printing(text3)
    printing(text4)
    printing(text5)
    sleep(1)
    printing(text6)
    printing(text7)
    print("Macierzą odwrotną do macierzy A nazywamy taką macierz B, że:")
    print("1.AB = BA = I.")
    print("2.Jest wypełniona samymi zerami.")
    if pomoc == True:
        print("[green]~Algebra była przewalona, ale tu akurat będzie 1.~")
    wybor = input(">>>")
    text9 = "\n~~Dobra, zaznaczam {0} i wychodzę...~~".format(wybor)
    printing(text9)
    x = input("\n\nKliknij enter, aby kontynuować...")
    match wybor:
        case '1':
            cleaning()
            text0 = "Dziś wyniki z algebry. Adamowi udało się zdać pierwszy egzamin. Jednak nie powinien spocząć na laurach.\nEgzamin w przyszłym semestrze może dać mu porządnie w kość.\n\n"
            printing(text0)
            print("Statystyki po egzaminie:")
            stat.printstats()
            x = input("\nKliknij enter, aby kontynuować...")
        case '2':
            cleaning()
            text0 = "Dziś wyniki z algebry. Wiadomość, nie jest jednak satysfakcjonująca dla Adama.\nNie udało mu się zdać pierwszego egzaminu. Oby w drugim semestrze zaliczenie okazało się prostsze.\n\n"
            stat.niezdal()
            printing(text0)
            print("Statystyki po egzaminie:")
            stat.printstats()
            x = input("\nKliknij enter, aby kontynuować...")
            
def piwo2():
    text0 = "\n\nAdam odpisuje na SMS'a:\n'Dobra, będę!'\n\nUbiera się i wychodzi do klubu.\n"
    printing(text0)
    x = input("\nKliknij enter, aby kontynuować...")
    gwint(2)
    
def odmowa2():
    text0 = "\n~~Cholera, nie mogę iść z nimi...~~\n\nOdpisuje im:\n`Sorki chłopaki, zostaję się uczyć :c`\n\n"
    text1 = "Adam odkłada telefon i wchodzi w kurs z programowania obiektowego na CEZ-ie."
    printing(text0)
    printing(text1)
    x = input("\n\nKliknij enter, aby kontynuować...")
    egzamin2()
    
def egzamin2():
    cleaning()
    text0 = "Adam budzi się rano względnie wypoczęty, ale ma mieszane uczucia co do egzaminu.\nSzybko ubiera się, aby zdążyć na czas. Po drodze wstąpił do Żabki na hotdoga.\nPrzed wydziałem czekali już na niego kumple."
    text1 = "\n\n-No i jak tam Adaś? Jak myślisz, zdasz?"
    text2 = "\n-Mam nadzieję..."
    text3 = "\n-Ej, chłopaki. Już 10:00, dawajcie do środka!"
    text4 = "\n\nWszyscy weszli na aulę, standardowo zajęli miejsca i otrzymali arkusze z zadaniami."
    text5 = "\n\nAdamowi jak zwykle średnio idzie, zostało już bardzo mało czasu. Standardowo zapomniał jednej z prostycz rzeczy...\n\n"
    text6 = "~~No kurde, znowu schrzaniłem...~~"
    printing(text0)
    printing(text1)
    printing(text2)
    printing(text3)
    printing(text4)
    printing(text5)
    sleep(1.5)
    printing(text6)
    
    print("\n\nDziedziczenie to:")
    print("1.Mechanizm współdzielenia funkcjonalności między klasami.")
    print("2.Rodzaj klasy abstrakcyjnej.")
    if pomoc == True:
        print("[green]~Jeśli się nie mylę, to git będzie pierwsza.~")
    wybor = input(">>>")
    text9 = "\n~~Dobra, zaznaczam {0} i wychodzę...~~".format(wybor)
    printing(text9)
    x = input("\n\nKliknij enter, aby kontynuować...")
    match wybor:
        case '1':
            cleaning()
            text0 = "Dziś wyniki z PO. Adamowi udało się go zaliczyć, ale lekko nie było. Następnym razem musi bardziej się przyłożyć!\n\n"
            printing(text0)
            print("Statystyki po egzaminie:")
            stat.printstats()
            x = input("\nKliknij enter, aby kontynuować...")
        case '2':
            cleaning()
            text0 = "Dziś wyniki z PO. Adam bardzo posmutniał, bo niestety nie udało mu się zaliczyć tego egzaminu.\nZnając życie pewnie zaważyło o tym te proste pytanie z dziedziczenia...\n\n"
            stat.niezdal()
            printing(text0)
            print("Statystyki po egzaminie:")
            stat.printstats()
            end = stat.get_przedmioty()
            x = input("\nKliknij enter, aby kontynuować...")
            if end == 0:
                gameover('studia')
                
def wakacje1():
    cleaning()
    text0 = "Jest końcówka września. Adaś spędził wakacje podróżując po Polsce.\n"
    text1 = "Niestety, wszystko co dobre szybko się kończy :/ Już za 3 dni wraca do swojego studenckiego miasta.\n\n"
    text2 = "Tego dnia była straszna ulewa, wiał silny wiatr, który wręcz kładł drzewa na ziemi.\nAdam oglądał swój ulubiony serial.\n"
    text3 = "Mamie Adama skończył się proszek do pieczenia, a była w trakcie przygotowania ciasta na niedzielny obiad."
    text4 = "\n\n-Adaś! Leć szybko do sklepu, potrzebuję proszku do pieczenia!!! Tylko uważaj, proszę!\n\n"
    text5 = "~~Cholera, akurat teraz mnie wysyła...~~\n\n"
    text6 = "-Dobrze mamo, już jadę...\n\n"
    text7 = "Adam wychodzi z domu. Leje tak mocno, że będąc na zewnątrz przez 5 sekund przemókł do suchej nitki.\n\n"
    text8 = "~~Naprawdę musiała teraz? Nie było lepszego momentu? K**rwa, mój serial!~~\n\n"
    printing(text0)
    printing(text1)
    printing(text2)
    printing(text3)
    printing(text4)
    printing(text5)
    printing(text6)
    printing(text7)
    printing(text8)
    print("Czy Adam jedzie do sklepu spokojnie? Czy chce jak najszybciej wrócić do serialu?")
    print("1.Spokojnie.")
    print("2.Szybko!!!")
    wybor = input(">>>")
    
    match wybor:
        case '1':
            print()
            text0 = "Adam opanowuje nerwy i powoli wyjeżdża z podjazdu."
            printing(text0)
            x = input("\n\nKliknij enter, aby kontynuować...")
            cleaning()
            text0 = "Wycieraczki ledwie nadążały zbierać wodę z szyby, do tego jezdnia była bardzo śliska.\n\n"
            text1 = "Adam dojeżdża do marketu oddalonego o kilka kilometrów. Bierze proszek, płaci i wsiada do auta.\n\n"
            text2 = "W drodze powrotnej przejeżdża obok pojazdów służb ratunkowych. Ktoś wypadł z zakrętu i wylądował w rowie.\nByło widać, że na pewno jechał z dużą prędkością.\n\n"
            text3 = "~~Przecież to mogłem być ja!~~\n\n"
            text4= "Powoli odjechał z miejsca wypadku i bezpiecznie dotarł do domu.\n\n"
            text5 = "Po przyjeździe opowiedział o całej sytuacji mamie.\n\n-A nie mówiłam?"
            printing(text0)
            printing(text1)
            printing(text2)
            printing(text3)
            printing(text4)
            printing(text5)
            x = input("\n\nKliknij enter, aby kontynuować...")
        case '2':
            print()
            text0 = "Adam bez zastanowienia rusza sprzed domu z piskiem opon!."
            printing(text0)
            x = input("\n\nKliknij enter, aby kontynuować...")
            cleaning()
            text0 = "Wycieraczki ledwie nadążały zbierać wodę z szyby, do tego jezdnia była bardzo śliska.\n\n"
            text1 = "Przed Adamem pojawia się dość ostry zakręt, a on jedzie bardzo szybko!\n\n"
            text2 = "Niestety, ten łuk okazuje się największym przeciwnikiem naszego bohatera...\n"
            text3 = "WPADA DO ROWU!!!\n\n"
            text4= "Prawdopodobnie traci przytomność...\n\n"
            text5 = "Ocknął się, kiedy strażacy próbowali wyciąć go z jego auta..."
            printing(text0)
            printing(text1)
            printing(text2)
            printing(text3)
            printing(text4)
            printing(text5)
            x = input("\n\nKliknij enter, aby kontynuować...")
            gameover('wakacje')
            
def piwo3():
    text0 = "\n\n~~Dobra, cały semestr się udało, to i to wyjdzie!~~\n\n"
    text1 = "-Chodźcie, dzisiaj przecież studencki czwartek, czyli tańsze piwko!!!"
    printing(text0)
    printing(text1)
    x = input("\n\nKliknij enter, aby kontynuować...")
    gwint(3)
    
def odmowa3():
    text0 = "\n~~Dlaczego oni tak mnie kuszą... Muszę poogarniać tego SQL'a.~~\n\n"
    text1 = "-Sory chłopaki, SQL wzywa!"
    printing(text0)
    printing(text1)
    x = input("\n\nKliknij enter, aby kontynuować...")
    egzamin3()
    
def egzamin3():
    cleaning()
    text0 = "~~Nie wierzę, coś za dobrze mi idzie...~~\n\n"
    text1 = "Adam wstał z łóżka naprawdę wypoczęty. Czuł przypływ pozytywnej energii i od razu dobrze nastawił się do baz.\n\n~~Ciekawe jak inni...~~\n\nNasz bohater wybrał się na uczelnię samochodem, w centrum był dość spory korek.\nNa szczęście udało mu się dotrzeć na czas, ale musiał od razu wbiec do sali egzaminacyjnej.\nUsiadł na ostatnim wolnym miejscu.\nNa pulpicie czekały już zadania i Adam od razu zabrał się za ich rozwiązywanie.\n\n"
    text2 = "Niestety, tak jak przewidywał, nie były one proste...\n\n~~Kurde, jak to było z tym?~~"         
    printing(text0)
    printing(text1)
    sleep(1.5)
    printing(text2)
    print("\n\nKtóre z poleceń jest częścią języka DDL?")
    print("1.SELECT *")
    print("2.CREATE TABLE xyz")
    if pomoc == True:
        print("[green]~Prawie na pewno nie jest to nr 1.~")
    wybor = input(">>>")
    text3 = "\n~~Dobra, zaznaczam {0}, może jest poprawne.~~".format(wybor)
    printing(text3)
    x = input("\n\nKliknij enter, aby kontynuować...")
    match wybor:
        case '2':
            cleaning()
            text0 = "Do USOS dodano nową ocenę. Jest ona z baz danych! Adamowi udało się je zaliczyć,\nale żeby je opanować w pełni musi jeszcze poćwiczyć.\n\n"
            printing(text0)
            print("Statystyki po egzaminie:")
            stat.printstats()
            x = input("\nKliknij enter, aby kontynuować...")
        case '1':
            cleaning()
            text0 = "Dziś wyniki z baz danych. Adam niestety ich nie zaliczył, ale głowa do góry!\nPrzecież jest jeszcze jeden semestr!\n\n"
            stat.niezdal()
            printing(text0)
            print("Statystyki po egzaminie:")
            stat.printstats()
            end = stat.get_przedmioty()
            x = input("\nKliknij enter, aby kontynuować...")

def piwo4():
    text0 = "\n-Tak, wiem. Idę z wami, jest tak gorąco, a jak wiadomo, jak gorąco, to pić trzeba!"
    printing(text0)
    x = input("\n\nKliknij enter, aby kontynuować...")
    gwint(4)
    
def odmowa4():
    text0 = "\n-Nie tym razem, jak nie zdam matka mnie zamorduje..."
    printing(text0)
    
    x = input("\n\nKliknij enter, aby kontynuować...")
    egzamin4() 
    
def egzamin4():
    cleaning()
    text0 = "~~Jeju, jak gorąco...~~\n\n"
    text1 = "Adam obudził się cały zlany potem. Nie czuł się najlepiej, wysoka temperatura nie pozwoliła mu spać.\nCałą noc wiercił się i przekładał ze strony na stronę.\n\n~~Dobra, ostatni egzamin i lecimy na Majorkę!~~\n\nBardzo szybko ogarnął się i zamówił taksówkę.\nPo przyjeździe na uczelnię przywitał się z kumplami, którzy ewidentnie mieli kaca.\n\n-Nieźle wczoraj zabalowaliście hahaha!\n-Daj spokój, nigdy więcej...\n\n"
    text2 = "Egzamin już trwał, czas mijał nieubłaganie. Odpowiedzi na pytanie w głowie brak!\n\n~~Naprawdę mam siebie dość, przecież to musi być proste...~~"         
    printing(text0)
    printing(text1)
    sleep(1.5)
    printing(text2)
    print("\n\nSystem plików stosowany w systemach MS DOS i Windows to")
    print("1.Tablica FAT")
    print("2.EXT")
    if pomoc == True:
        print("[green]~Prawdopodobnie jest to odpowiedź nr 1.~")
    wybor = input(">>>")
    text3 = "\n~~Dobra, zaznaczam {0}, może jest poprawne.~~".format(wybor)
    printing(text3)
    x = input("\n\nKliknij enter, aby kontynuować...")
    match wybor:
        case '1':
            cleaning()
            text0 = "~~Jakim cudem!~~\n\nAdam dostał pozytywną ocenę z ostatniego egzaminu!\n\nWybiera numer do rodziców, a kiedy odebrała mama wykrzyczał:\n\n-Mama, zdałem to!\n\n"
            printing(text0)
            x = input("\n\nKliknij enter, aby kontynuować...")
            endgame()
            
        case '2':
            cleaning()
            text0 = "~~No tak, inaczej być nie mogło...~~\n\nW USOS stoi dwója...\n\n~~Mam dość tego całęgo studiowania...~~\n\n"
            stat.niezdal()
            printing(text0)
            print("Statystyki po egzaminie:")
            stat.printstats()
            end = stat.get_przedmioty()
            x = input("\nKliknij enter, aby kontynuować...")
            if end == 0:
                gameover('studia')
            else:
                endgame()
    
    
            
def history():
    cleaning()
    stat.set_przedmioty()
    text0 = "~~Ahh no i w końcu skończyły się wakację... Shiit, nie chce mi się wstawać...~~\n" 
    text1 = "\nAdam właśnie się budzi. Dziś jest 1 października 2020. Jest on mieszkańcem odległej wsi i właśnie wprowadził się\ndo akademika. Dostał się na informatykę na jednej z politechnik i dziś idzie na swoje pierwsze zajęcia w życiu." 
    text2 = "\nMimo niewyspania jest jeszcze pełen energii, ale pamiętaj to dopiero początek roku akademickiego!!!\nW jego trakcie czeka go kilka wyzwań, szczególnie w okolicah sesji, bo jak wszyscy wiemy,\npotrafi ona wyssać chęci do życia nawet najlepszym studentom..."
    text3 = "\n\n~~Dobra... Najwyższa pora wstawać meh...~~\n\n"
    text4 = "Adam ubiera się i wychodzi na uczlenię..."
    # print(str(ulatwienie))
    printing(text0)  
    printing(text1)    
    printing(text2)
    printing(text3)
    printing(text4)
    x = input("\n\nKliknij enter, aby kontynuować...")
    
    cleaning()
    print(pyfiglet.figlet_format("Pierwsza sesja!!!\n\n\n"))
    winsound.Beep(440,500)
    print("Statystyki naszego bohatera przed rozpoczęciem zmagań podczas nauki i egzaminów:")
    stat.printstats()
    print("\n")
    print("[red]PRZYPOMNIENIE!!! [white]Aby przejść na wyższy rok studiów musisz uzyskać pozytywny wynik z co najmniej jednego z egzaminów, w ciągu roku będą dwa.")
    print("Ważnym aspektem jest również kontrolowanie Adama, aby zbyt często nie imprezował, szczególnie przed sesją,\nbo może sie to dla niego źle skończyć :(")
    x = input("\nKliknij enter, aby kontynuować...")
    
    cleaning()
    text0 = "Minął praktycznie cały pierwszy semestr, a Adam niezbyt przykładał się do nauki. Pierwszy egzamin już jutro, ale nasz\nbohater zaraz stanie przed pierwszym dylematem tego roku...\n\n"
    text1 = "-Adaś, idziesz z nami? Jutro sesja, a trzeba się troszeczkę wyluzować przed egzaminem z algebry. Wybieramy się grupowo\nna piwko do Gwintu, albo kilka haha!\n"
    text2 = "-Hmm no nie wiem... Niewiele umiem na jutro, przydałoby się pouczyć.\n"
    text3 = "-No dawaj, chodź z nami! Ogarniasz coś na pewno bez nauki!\n"
    printing(text0)
    printing(text1)
    printing(text2)
    printing(text3)
    print("\nCzy wyrażasz chęć wyjścia z kumplami na piwo?")
    print("1.Tak")
    print("2.Nie")
    wybor = input(">>>")
    match wybor:
        case '1':
            piwo1()
        case '2':
            odmowa1()
    
    cleaning()
    print(pyfiglet.figlet_format("Druga sesja!!!\n\n\n"))
    winsound.Beep(440,500)
    print("Statystyki naszego bohatera przed rozpoczęciem zmagań podczas nauki i egzaminów:")
    stat.printstats()
    stat.set_upojenie()
    print("\n")
    print("[red]Powodzenia!!!")
    x = input("\nKliknij enter, aby kontynuować...")
    
    cleaning()
    text0 = "Drugi semestr minął Adamowi bardzo szybko. Nic dziwnego, w końcu była wiosna, a chwilę przed egzaminami lato.\nJak zwykle nasz bohater nie garnął się do nauki. Przecież miał mnóstwo innych ważniejszych spraw,\njak np. piwko na Murkach, albo granie w LOL'a z ziomeczkami.\nZaczął przygotowywać się do egzaminu z programowania obiektowego, standardowo dzień przed sesją.\nNadmiar materiału zaczyna go paraliżować. "
    text1 = "Telefon Adama zaczyna wibrować, a oczom bohatera ukazuje się wiadomość\nod kumpli z roku:\n`Hej Adam, wybieramy się z chłopakami do Gwintu na piwo. Mamy już dosyć nerwów przed zaliczeniem. O 19, pod Polibudą,\nco Ty na to?`" 
    printing(text0)
    printing(text1)
    print("\n\nCzy wyrażasz chęć wyjścia z kumplami na piwo?")
    print("1.Tak")
    print("2.Nie")
    
    wybor = input(">>>")
    match wybor:
        case '1':
            piwo2()
        case '2':
            odmowa2()
            
    cleaning()
    print(pyfiglet.figlet_format("Wakacje!!!\n\n\n"))
    winsound.Beep(261,500)
    winsound.Beep(329,500)
    winsound.Beep(392,500)
    print("Ostatecznie udało Ci się przetrwać pierwszy rok studiów! [red] GRATULACJE!!!")
    print("Statystyki po obu sesjach:")
    stat.printstats()
    print("\n")
    print("[red]Powodzenia w dalszej edukacji!!!")
    x = input("\nKliknij enter, aby kontynuować...")
    
    wakacje1()
    
    cleaning()
    print(pyfiglet.figlet_format("Trzecia sesja!!!\n\n\n"))
    winsound.Beep(440,500)
    stat.set_przedmioty()
    print("Statystyki naszego bohatera przed rozpoczęciem zmagań podczas nauki i egzaminów:")
    stat.printstats()
    stat.set_upojenie()
    print("\n")
    print("[red]Powodzenia!!! Połowa drogi za Tobą!!!")
    x = input("\nKliknij enter, aby kontynuować...")
    cleaning()
    text0 = "Trzeci semestr przebiegał wyjątkowo pomyślnie. Adam nie miał problemów z zaliczaniem kolokwiów.\nJedynie bazy danych sprawiały mu jakąś trudność. Do każdego z przedmiotów przygotował się względnie dobrze,\nale ten jeden wyjątek...\n\n~~Ach te bazy... Ja ich nie zaliczę!~~\n\nŻeby tradycji stała się zadość, znajomi standardowo zaproponowali wyjście na piwo i to akurat przed tymi nieszczęsnymi\nbazami!\n\n-To co Adaś, klasycznie? Lecimy na piwko?"
    printing(text0)
    print("\n\nCzy wyrażasz chęć wyjścia z kumplami na piwo?")
    print("1.Tak")
    print("2.Nie")
    
    wybor = input(">>>")
    match wybor:
        case '1':
            piwo3()
        case '2':
            odmowa3()
            
    cleaning()
    print(pyfiglet.figlet_format("Czwarta sesja!!!\n\n\n"))
    winsound.Beep(440,500)
    print("Statystyki naszego bohatera przed rozpoczęciem zmagań podczas nauki i egzaminów:")
    stat.printstats()
    stat.set_upojenie()
    print("\n")
    print("[red]Ostatnia prosta przed Tobą!!!")
    x = input("\nKliknij enter, aby kontynuować...")
    cleaning()
    text0 = "Końcówka semestru jak i cały minęły ekstremalnie szybko. Czas przyspieszył jeszcze bardziej\nkiedy rozpoczęło się lato, a wraz z nim wyjazdy nad okoliczne jezioro!\nAdam spędził nad nim mnóstwo czasu przez co zaniedbał naukę do tego stopnia,\nże ledwo zdał z wiekszości przedmiotów.\nW pierwszym dniu sesji było tak gorąco, że nie dało się usiedzieć w trakcie egzaminu!\nPrzyszedł dzień przed zaliczeniem systemów operacyjnych, bardzo dużo w nich teori...\n\n~~Damn, taki żar leje się z nieba, jak ja mam się skupić?~~\n\n-Adasiu, wiesz gdzie idziemy dziś wieczorem?-powiedział jeden z kumpli.\n\n~~No tak, na pewno na piwo. Sam bym chętnie poszedł...~~"
    printing(text0)
    print("\n\nCzy wyrażasz chęć wyjścia z kumplami na piwo?")
    print("1.Tak")
    print("2.Nie")
    wybor = input(">>>")
    match wybor:
        case '1':
            piwo4()
        case '2':
            odmowa4()
    
def start_sound():
    winsound.Beep(261,500)
    winsound.Beep(261,500)
    winsound.Beep(391,500)

def ekran_startowy():
    os.system("cls" if os.name=="nt" else "clear")
    start_sound()
    print(pyfiglet.figlet_format("Mroczny Sen Studenta\n\n\n"))
    print(pyfiglet.figlet_format("                       RPG tekstowy"))
    
    start = input("\n\n\n\n\n\n\n\nKliknij enter, aby rozpocząć...")
    
def menu():
    global pomoc
    cleaning()
    print(pyfiglet.figlet_format("Menu"))
    print("[red]1.Rozpocznij grę (wersja dla nienformatyków z podpowiedziami autora)")
    print("[blue]2.Rozpocznij grę (wersja dla informatyków)")
    print("[purple]3.Info o grze")
    print("[brown]4.Wyjście z gry")
    print("\n[green]Wybierz opcję i zatwierdź enterem:")
    wybor = input(">>>")
    match wybor:
        case '1':
            pomoc = True
            history()
        case '2':
            pomoc = False
            history()
        case '3':
            info()
        case '4':
            os._exit(0)
    
            
def info():
    os.system("cls" if os.name=="nt" else "clear")
    print(pyfiglet.figlet_format("Info o grze"))
    # print("\n")  
    print("Mroczny sen stydenta jest tekstową grą RPG.")
    print("Głównym bohaterem gry jest Adam, student informatyki na pewnej uczleni technicznej.")
    print("Stoi przed nim wiele wyzwań, ponieważ jak każdy wie, takie studia nie należą do najłatwiejszych...")
    print("Rozpoczynając grę stajesz się Adamem, musisz podejmować za niego bardzo ważne decyzje i pilnować, żeby zaliczył wszystkie przedmioty.")
    print("\nKrótka intrukcja:")
    print("1.Wyboru dokonuje się wprowadzając liczbę odpowiadającą numerowi czynności do wykonania.")
    print("2.Aby przejść grę należy zaliczyć co najmniej jeden z dwóch egzaminów w semestrze, oraz zbytnio nie imprezować w Gwincie (klubie studenckim).")
    print("3.Możliwe jest, że Adama może spotkać coś niespodziewanego, co bardzo wpłynie na jego życie.")
    print("\nPowodzenia!!!\n")
    wybor2 = input("Kliknij enter, aby powrócić...")
    main()
    
def main():
    while 1:
        menu()
        
ekran_startowy()
main()
# history()
# gwint()


                

    