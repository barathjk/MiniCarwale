"""
cars.py for listing all cars
"""
import carclass
import emicalc

def totalcars(choice):
    if choice == 1:
        print("\n" + "TATA Cars")
        print(" 1. Altroz")
        print(" 2. Harrier")
        print(" 3. Nexon")
        carchoice = int(input("Enter your choice of car to get more details : "))
        if carchoice == 1:
            altrozobj = carclass.altroz()
            altrozobj.display()
            emiprice(altrozobj, carchoice)

        elif carchoice == 2:
            harrierobj = carclass.harrier()
            harrierobj.display()
            emiprice(harrierobj, carchoice)

        elif carchoice == 3:
            nexonobj = carclass.nexon()
            nexonobj.display()
            emiprice(nexonobj, carchoice)
    elif choice == 2:
        print("\n" + "Maruti Suzuki Cars")
        print(" 1. Swift")
        print(" 2. Vitara Breeza")
        print(" 3. Ciaz")
        carchoice = int(input("Enter your choice of car to get more details : "))
        if carchoice == 1:
            swiftobj = carclass.swift()
            swiftobj.display()
            emiprice(swiftobj, carchoice)

        elif carchoice == 2:
            vitaraobj = carclass.vitara()
            vitaraobj.display()
            emiprice(vitaraobj, carchoice)

        elif carchoice == 3:
            ciazobj = carclass.ciaz()
            ciazobj.display()
            emiprice(ciazobj, carchoice)
    elif choice == 3:
        print("\n" + "Skoda Cars")
        print(" 1. Rapid")
        print(" 2. Superb")
        print(" 3. Octavia")
        carchoice = int(input("Enter your choice of car to get more details : "))
        if carchoice == 1:
            rapidobj = carclass.rapid()
            rapidobj.display()
            emiprice(rapidobj, carchoice)

        elif carchoice == 2:
            superbobj = carclass.superb()
            superbobj.display()
            emiprice(superbobj, carchoice)

        elif carchoice == 3:
            octaviaobj = carclass.octavia()
            octaviaobj.display()
            emiprice(octaviaobj, carchoice)

    elif choice == 4:
        print("\n" + "Honda Cars")
        print(" 1. Jazz")
        print(" 2. City")
        print(" 3. WR-V")
        carchoice = int(input("Enter your choice of car to get more details : "))
        if carchoice == 1:
            jazzobj = carclass.jazz()
            jazzobj.display()
            emiprice(jazzobj, carchoice)

        elif carchoice == 2:
            cityobj = carclass.city()
            cityobj.display()
            emiprice(cityobj, carchoice)

        elif carchoice == 3:
            wrvobj = carclass.wrv()
            wrvobj.display()
            emiprice(wrvobj, carchoice)

    elif choice == 5:
        print("\n" + "Hyundai Cars")
        print(" 1. i20")
        print(" 2. Creta")
        print(" 3. Verna")
        carchoice = int(input("Enter your choice of car to get more details : "))
        if carchoice == 1:
            i20obj = carclass.i20()
            i20obj.display()
            emiprice(i20obj, carchoice)

        elif carchoice == 2:
            cretaobj = carclass.creta()
            cretaobj.display()
            emiprice(cretaobj, carchoice)

        elif carchoice == 3:
            vernaobj = carclass.verna()
            vernaobj.display()
            emiprice(vernaobj, carchoice)

def emiprice(carobject, carchoice):
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
