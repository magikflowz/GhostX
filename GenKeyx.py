import random
from os import system, name
import sys
import threading
import time
import itertools


def clr():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
def KeyXGenerator(PersonDetailsArray,UsernamesArray, PetNamesArray, PartnersDetailsArray):
            
            PersonDetails = []
            UsernameList = []
            PersonbirthYear = ""
            Birthyears = []
            objects = []
            PartnerDetails = []
            PartnerBirthYear = ""
            
            for item in PersonDetailsArray[:]:
                PersonDetails.append(item)
                try:
                    x=int(item)
                    PersonDetails.remove(item)
                    PersonbirthYear = PersonbirthYear + item
                    print('\nBIRTH INFORMATION FOUND: '+ PersonbirthYear)
                except:
                    continue 

            PersonBirthYear4Digits = PersonbirthYear[4:8]
            print('\n4 year digits: ' + PersonBirthYear4Digits)
            PersonBirthYear2Digits = PersonbirthYear[6:8]
            print('\n2 year digits: ' + PersonBirthYear2Digits)
            Birthyears.append(PersonBirthYear4Digits)
            Birthyears.append(PersonBirthYear2Digits)

            for PartnerItem in PartnersDetailsArray:
                PartnerDetails.append(PartnerItem)
                try:
                    x=int(PartnerItem)
                    PartnerDetails.remove(PartnerItem)
                    PartnerBirthYear = PartnerBirthYear + PartnerItem
                    print('\nPartner BIRTH INFORMATION FOUND: '+ PartnerBirthYear)
                except:
                    continue
            
            PartnerBirthYear4Digits = PartnerBirthYear[4:8]
            print('\n4 year digits: ' + PartnerBirthYear4Digits)
            PartnerBirthYear2Digits = PartnerBirthYear[6:8]
            print('\n2 year digits: ' + PartnerBirthYear2Digits)
            Birthyears.append(PartnerBirthYear4Digits)
            Birthyears.append(PartnerBirthYear2Digits)

            for Detail in PersonDetails:
                objects.append(Detail)
            
            for Years in Birthyears:
                objects.append(Years)
            
            for username in UsernamesArray:
                objects.append(username)
            
            for PetName in PetNamesArray:
                objects.append(PetName)
                
            combinations = [ "".join(a) for a in itertools.combinations(objects, 8)]

            for combo in combinations:
                print(combo)

            print("\nNumber of Combinations: " + str(len(combinations)))
            

def GenKeyX():
    
    GenKeyX_Welcome = print("""
    
   _____              _  __           __   __
  / ____|            | |/ /           \ \ / /
 | |  __  ___ _ __   | ' / ___ _   _   \ V / 
 | | |_ |/ _ \ '_ \  |  < / _ \ | | |   > <  
 | |__| |  __/ | | | | . \  __/ |_| |  / . \ 
  \_____|\___|_| |_| |_|\_\___|\__, | /_/ \_\_
                                __/ |        
                               |___/         
    """)
     
    PersonDetailsArray = []
    UsernamesArray =[]
    PartnersDetailsArray = []
    PetNamesArray = []
    
    while(True):
        
        print("[+] Enter Targets Personal Information to create a custom dictionary list")
        print("[+] Press enter to skip over an entry at anytime ")
        PersonFirstName = input("--> Enter First Name: ")
        PersonLastName = input("--> Enter Last Name: ")
        while(True):
            PersonDateofBirth = input("--> Enter date of birth ex(01021993): ")
            if len(PersonDateofBirth) == 8 or PersonDateofBirth == "":
                break
            else:
                print("Enter Correct date of birth length or skip over an entry")
        PersonSchool = input("--> Enter School or University: ")
        PersonWork = input("--> Enter company's name: ")
        PersonHomeTown = input("--> Enter Home Town: ")
        PersonFavoriteColor = input("--> Favorite color: ")
        PersonCarModel = input("--> Car model: ")
        
        while(True):
            PersonUsernameNumber = input("[!] Number of Usernames: ")
            try:
                x = int(PersonUsernameNumber)
                n=1
                UserNumber = x+1
                while(n<UserNumber):
                    Username = input("[+] Enter Username: ")
                    UsernamesArray.append(Username)
                    n+=1
            except ValueError: 
                print("Enter a integer")
                continue 
            break
                
        UsernamesArray = [string for string in UsernamesArray if string != ""]
                
        while(True):
            NumberofPets = input("[!] Number of Pets: ")
            try:
                x = int(NumberofPets)
                n=1
                NumberofPets = x+1
                while(n<NumberofPets):
                    PetsName = input("[+]Enter Pets Name: ")
                    PetNamesArray.append(PetsName)
                    n+=1
            except ValueError:
                print("enter a integer")
                continue
            break
        PetNamesArray = [string for string in PetNamesArray if string != ""]
        
        PersonDetailsArray.extend((PersonFirstName,PersonLastName,PersonDateofBirth,PersonSchool,PersonWork,PersonHomeTown,PersonFavoriteColor,PersonCarModel))
        PersonDetailsArray = [string for string in PersonDetailsArray if string != ""]
        
        print("[+] Enter Partners Information")
        PartnersFirstName = input("--> Partners First Name: ")
        PartnersLastName = input("--> Partners Last Name: ")
        while(True):
            PartnersDateofBirth = input("--> Partners Date of Birth ex(01021993): ")
            if len(PartnersDateofBirth) == 8 or PartnersDateofBirth == "":
                break
            else:
                print("Enter Correct date of birth length or skip over an entry") 
        PartnersDetailsArray.extend((PartnersFirstName, PartnersLastName, PartnersDateofBirth))
        PartnersDetailsArray = [string for string in PartnersDetailsArray if string != ""]
        
        print("")
        
        print("[+] Personal Details:")
        for item in PersonDetailsArray:
            print(item)
        
        print("")
            
        print("[+] Usernames: ")
        countUsersname = 0
        for item in UsernamesArray:
            countUsersname+=1
            print(countUsersname,". ", item)
        
        print("")
        
        print("[+] Pet names: ")
        PetnamesNum = 0
        for item in PetNamesArray:
            PetnamesNum +=1
            print(PetnamesNum,". ", item)
    
        print("")
        
        print("[+] Partner Details: ")
        PartnerCounter = 0
        for item in PartnersDetailsArray:
            PartnerCounter +=1
            print(PartnerCounter,". ", item)
        
        ''' 
        DBQuestion = input("Would like you to do a DB Search for previous passwords y or n: ")
        DBQuestion = DBQuestion.lowercase()
        
        if DBQuestion == 'y':
            continue
    print('[+]')
    '''
        Send2KeyGen = input("Would you like to send these details to the generator y or n: ")
        Send2KeyGen = Send2KeyGen.lower()
        if Send2KeyGen == "y":
            print(KeyXGenerator(PersonDetailsArray,UsernamesArray, PetNamesArray, PartnersDetailsArray))
        
        elif Send2KeyGen == "n":
            ExitorNot = input("would like to exit or reset details y[exit] or n[reset]: ")
            ExitorNot = ExitorNot.lowercase()
            if ExitorNot == "y":
                sys.exit(0)
            if ExitorNot == "n":
                print("Reseting...")
                input("Press enter to continue")
                GenKeyX()
                
GenKeyX()    
