"""
cars.py for listing all cars
"""
import carclass
import emicalc

def totalcars(choice):
    """
    total cars Listed
    """
    if choice == 1:
        print("\n" + "TATA Cars")
        print(" 1. Altroz")
        print(" 2. Harrier")
        print(" 3. Nexon")
        carchoice = int(input("Enter your choice of car to get more details : "))
        if carchoice == 1:
            altrozobj = carclass.Altroz()
            altrozobj.display()
            emiprice(altrozobj, carchoice)

        elif carchoice == 2:
            harrierobj = carclass.Harrier()
            harrierobj.display()
            emiprice(harrierobj, carchoice)

        elif carchoice == 3:
            nexonobj = carclass.Nexon()
            nexonobj.display()
            emiprice(nexonobj, carchoice)
    elif choice == 2:
        print("\n" + "Maruti Suzuki Cars")
        print(" 1. Swift")
        print(" 2. Vitara Breeza")
        print(" 3. Ciaz")
        carchoice = int(input("Enter your choice of car to get more details : "))
        if carchoice == 1:
            swiftobj = carclass.Swift()
            swiftobj.display()
            emiprice(swiftobj, carchoice)

        elif carchoice == 2:
            vitaraobj = carclass.Vitara()
            vitaraobj.display()
            emiprice(vitaraobj, carchoice)

        elif carchoice == 3:
            ciazobj = carclass.Ciaz()
            ciazobj.display()
            emiprice(ciazobj, carchoice)
    elif choice == 3:
        print("\n" + "Skoda Cars")
        print(" 1. Rapid")
        print(" 2. Superb")
        print(" 3. Octavia")
        carchoice = int(input("Enter your choice of car to get more details : "))
        if carchoice == 1:
            rapidobj = carclass.Rapid()
            rapidobj.display()
            emiprice(rapidobj, carchoice)

        elif carchoice == 2:
            superbobj = carclass.Superb()
            superbobj.display()
            emiprice(superbobj, carchoice)

        elif carchoice == 3:
            octaviaobj = carclass.Octavia()
            octaviaobj.display()
            emiprice(octaviaobj, carchoice)

    elif choice == 4:
        print("\n" + "Honda Cars")
        print(" 1. Jazz")
        print(" 2. City")
        print(" 3. WR-V")
        carchoice = int(input("Enter your choice of car to get more details : "))
        if carchoice == 1:
            jazzobj = carclass.Jazz()
            jazzobj.display()
            emiprice(jazzobj, carchoice)

        elif carchoice == 2:
            cityobj = carclass.City()
            cityobj.display()
            emiprice(cityobj, carchoice)

        elif carchoice == 3:
            wrvobj = carclass.Wrv()
            wrvobj.display()
            emiprice(wrvobj, carchoice)

    elif choice == 5:
        print("\n" + "Hyundai Cars")
        print(" 1. I20")
        print(" 2. Creta")
        print(" 3. Verna")
        carchoice = int(input("Enter your choice of car to get more details : "))
        if carchoice == 1:
            i20obj = carclass.I20()
            i20obj.display()
            emiprice(i20obj, carchoice)

        elif carchoice == 2:
            cretaobj = carclass.Creta()
            cretaobj.display()
            emiprice(cretaobj, carchoice)

        elif carchoice == 3:
            vernaobj = carclass.Verna()
            vernaobj.display()
            emiprice(vernaobj, carchoice)

def emiprice(carobject, carchoice):
    """
    Choose between EMI or Price Breakup
    """
    print("\n"+"Enter e for EMI Calculation")
    print("Enter p for View Price breakup")
    choice2 = input()
    if choice2 in ('e', 'E'):
        emiamount = emicalc.emi()
        if emiamount:
            print("EMI = ₹ {0}/month".format(emiamount))
        else:
            return 0
    elif choice2 in ('p', 'P'):
        carobject.pricebreakup()
    else:
        totalcars(carchoice)
