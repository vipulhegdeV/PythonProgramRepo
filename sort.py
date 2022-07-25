import os
import math
fre=input("ENTER IF FREIGHT TRAIN IS ON THE LINE\n")
fre.lower()
if fre == 'Y':
     fre_pos=float(("Enter freight train position"))
     float(fre_pos)
else:
     print("FREIGHT TRAIN ABSENT")
passe=input("ENTER Y IF PASSENGER TRAIN IS ON THE LINE\n")
passe.lower()
if passe == 'Y':
     pass_pos=float(input(passe_pos=("Enter passenger train position"))
else :
     print("PASSENGER TRAIN ABSENT")
prem=input("ENTER Y IF PREMIUM TRAIN IS ON THE LINE")
prem.lower()
if prem == 'Y':
     prem_pos=float(input("Enter premium train position"))
else:
     print("PREMIUM TRAIN ABSENT")
if max(prem_pos,fre_pos,passe_pos) == prem_pos:
     print("PREMIUM TRAIN: PROCEED ON MAIN LINE\nPASSENGER TRAIN:WAIT IN LOOP LINE\n FREIGHT TRAIN :WAIT IN LOOP LINE\n ")
elif max(prem_pos,fre_pos,passe_pos) == passe_pos:
      print("PREMIUM TRAIN PROCEED AND OVERTAKE ON MAIN LINE \nPASSENGER TRAIN:WAIT IN LOOP LINE\n FREIGHT TRAIN :WAIT IN LOOP LINE\n")
elif max(prem_pos,fre_pos,passe_pos) == fre_pos:
      print("PREMIUM TRAIN PROCEED AND OVERTAKE ON MAIN LINE \nPASSENGER TRAIN:WAIT IN LOOP LINE\n FREIGHT TRAIN :WAIT IN LOOP LINE\n")
elif max(passe_pos,fre_pos) == fre_pos:
     print("PASSENGER TRAIN PROCEED TO OVERTAKE ON MAIN LINE\n FREIGHT TRAIN HALT AT MAIN LINE")
else:
     print("FREIGHT TRAIN PROCEED ON MAIN LINE")