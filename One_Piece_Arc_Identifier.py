print('Welcome to the One Piece Arc Identifier App! To begin, insert the number of the episode you wish to search for:')
x=int(input())
saga1='East Blue Saga'
saga2='Alabasta Saga'
saga3='Sky Island Saga'
saga4='Water7 Saga'
saga5='Thriller Bark Saga'
saga6='Summit War Saga'
saga7='Fish-Man Island Saga'
saga8='Dressrosa Saga'
saga9='Whole Cake Island Saga'
saga10='Wano Country Saga'
saga_final='Egghead'
if 1<=x<=3:
    print("Romance Dawn")
    print(saga1)
elif 4<=x<=8:
    print('Orange Town')
    print(saga1)
elif 9<=x<=18:
    print('Syrup Village')
    print(saga1)
elif 19<=x<=30:
    print('Baratie')
    print(saga1)
elif 31<=x<=44:
    print('Arlong Park')
    print(saga1)
elif 45<=x<=53:
    print('Loguetown')
    print(saga1)
elif 54<=x<=61:
    print('Warship Island')
    print(saga1)
elif 62<=x<=63:
    print('Reverse Mountain')
    print(saga2)
elif 64<=x<=67:
    print('Whiskey Peak')
    print(saga2)
elif 68<=x<=69:
    print('Diary of Koby-Meppo')
    print(saga2)
elif 70<=x<=77:
    print('Little Garden')
    print(saga2)
elif 78<=x<=91:
    print('Drum Island')
    print(saga2)
elif 92<=x<=130:
    print('Alabasta')
    print(saga2)
elif 131<=x<=135:
    print('Post-Alabasta')
    print(saga2)
elif 136<=x<=138:
    print('Goat Island')
    print(saga3)
elif 139<=x<=143:
    print('Ruluka Island')
    print(saga3)
elif 144<=x<=152:
    print('Jaya')
    print(saga3)
elif 153<=x<=195:
    print('Skypeia')
    print(saga3)
elif 196<=x<=206:
    print('G-8')
    print(saga3)
elif 207<=x<=219:
    print('Long Ring Long Island')
    print(saga4)
elif 220<x<=224:
    print("Ocean's Dream")
    print(saga4)
elif 225<=x<=228:
    print("Foxy's Return")
    print(saga4)
elif 229<=x<=263:
    print('Water7')
    print(saga4)
elif 264<=x<=312:
    print('Enies Lobby')
    print(saga4)
elif 313<=x<=325:
    print('Post-Enies Lobby')
    print(saga4)
elif 326<=x<=335:
    print('Ice Hunter')
    print(saga5)
elif x==336:
    print ('Chopper Man Special')
elif 337<=x<=381:
    print('Thriller Bark')
    print(saga5)
elif 382<=x<=384:
    print('Spa Island')
    print(saga5)
elif 385<=x<=407:
    print('Sabaody Archipelago')
    print(saga6)
elif 408<=x<=417:
    print('Amazon Lily')
    print(saga6)
elif 418<=x<=421:
    print("Straw Hat's Separation Special")
    print(saga6)
elif 422<=x<=425:
    print('Impel Down')
    print(saga6)
elif 426<=x<=429:
    print('Little East Blue')
    print(saga6)
elif 430<=x<=452:
    print('Impel Down')
    print(saga6)
elif 453<=x<=456:
    print("Straw Hat's Separation Special")
    print(saga6)
elif 457<=x<=489:
    print('Marineford')
    print(saga6)
elif 490<=x<=516:
    print('Post-War')
    print(saga6)
elif 517<=x<=522:
    print('Return to Sabaody')
    print(saga7)
elif 523<=x<=574:
    print('Fish-Man Island')
    print(saga7)
elif 575<=x<=578:
    print("Z's Ambition")
    print(saga8)
elif 579<=x<=625:
    print('Punk Hazard')
    print(saga8)
elif 626<=x<=628:
    print('Caesar Retrieval')
    print(saga8)
elif 629<=x<=746:
    print('Dressrosa')
    print(saga8)
elif 747<=x<=750:
    print('Silver Mine')
    print(saga9)
elif 751<=x<=779:
    print('Zou')
    print(saga9)
elif 780<=x<=782:
    print('Marine Rookie')
    print(saga9)
elif 783<=x<=877:
    print('Whole Cake Island')
    print(saga9)
elif 878<=x<=889:
    print('Levely')
    print(saga9)
elif 890<=x<=894:
    print('Wano Country')
    print(saga10)
elif 895<=x<=896:
    print('Cidre Guild')
    print(saga10)
elif 897<=x<=1028:
    print('Wano Country')
    print(saga10)
elif 1029<=x<=1030:
    print("Uta's Past")
    print(saga10)
elif 1031<=x<=1085:
    print('Wano Country')
    print(saga10)
else:
    print('Egghead')
    print(saga_final)