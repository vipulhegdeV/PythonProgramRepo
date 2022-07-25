import os 
no_stop=input("DOES NORTHBOUND AND SOUTHBOUND TRAINS HALT HERE\n")
# INPUT IF NORTH OR SOUTH BOUND TRAINS HALT HERE
if no_stop == 'N':

 x=input("Enter the distance of NORTHBOUND train from  station in kms=\n")
 x=int(x)
 y=input("Enter the distance of SOUTHBOUND TRAIN from  station in Kms=\n")
 y=int(y)
 if max(x,y) == y:
  print(" SOUTHBOUND TRAIN  will cross NORTHBOUND train \n NORTHBOUND train = HALT AT STATION LOOP LINE\n  SOUTHBOUND TRAIN= MOVE ON MAIN LINE")
 elif max(x,y) == x:
  print(" NORTHBOUND train will cross SOUTHBOUND TRAIN \n NORTHBOUND train = MOVE ON MAIN LINE \n SOUTHBOUND TRAIN = HALT AT STATION LOOP LINE")
#INPUT IF ANY OF SOUTH/NORTH BOUND TRAINS HALT HERE
elif no_stop == 'Y':
 north_stop=input("DOES NORTHBOUND TRAIN HAVE STOP AT THE STATION\n INPUT IN YES OR NO ONLY\n")

 if north_stop == 'Y':
   print("NORTHBOUND TRAIN = PROCEED TO LOOP LINE\nSOUTHBOUND TRAIN HALT AT MAIN LINE UPON ARRIVAL")
   #NORTHBOUND TRAIN HALT ^^
 else:
  south_stop=input("DOES SOUTHBOUND TRAIN HAVE STOP AT THE STATION\n INPUT IN YES OR NO ONLY\n")
  if south_stop == 'Y':
    print("SOUTHBOUND TRAIN = PROCEED TO LOOP LINE\nNORTHBOUND TRAIN HALT AT MAIN LINE UPON ARRIVAL")
    #SOUTHBOUND TRAIN HALT ^^
else:
  print("INVALID ANSWER")