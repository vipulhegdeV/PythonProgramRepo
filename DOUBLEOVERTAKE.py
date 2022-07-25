import os
import time
#setting up parameters

strech=int(input("Enter the STRECTH length  MAX= 30KM :\t"))
premdis=int(input("Enter the premium train distance from S end:\t"))
premspeed=int(input("Enter the MPS of premium train in kmph: "))
leaddis=int(input("Enter the lead train distance from S end:\t"))
next_statdis=int(input("Enter the distance from lead train to next first looping station available:\t"))

#computations

reldist=0
reldist=premdis-leaddis
print("DISTANCE OF PREMIUM TRAIN TO LEAD TRAIN IS (IN KM)=",reldist)

#Decisionmaking

if reldist<=30 and reldist>=10:   #IF RELATIVE TRAIN DISTANCE IS MORE THAN 10KM AND LESS THAN 30 KM OR MORE THAN 30 KM FLOW
    if next_statdis<=10:
        response=input("IS LOOP LINE ONE FREE Y =YES \nN=SECONDLINE, \nNO LOOP LINE FREE ENTER ZERO : ")
        response.upper()
        
        if response=='Y':
          print("LEAD TRAIN MOVE TO LOOP LINE ONE, SET SIGNAL L1 : RED\nPREMIUM TRAIN PROCEED AT MPS TO NEXT STRECH, SET SIGNAL ML: GREEN")
          overtake_time=0.0
          overtake_time=reldist/premspeed
          print("OVERTAKING TIME : SIGNAL L1:RED:",overtake_time," hrs")
          signal_time=0.0
          signal_time=overtake_time+0.02
          print("SIGNAL L1: GREEN IN hrs ",signal_time)
        
        elif response=='N':
            print("LEAD TRAIN MOVE TO LOOP LINE TWO, SET SIGNAL L2 : RED\n SIGNAL L1: RED \n PREMIUM TRAIN PROCEED AT MPS TO NEXT STRECH, SET SIGNAL ML: GREEN")
            overtake_time=reldist/premspeed
            print("OVERTAKING TIME in hrs:  L1:RED:",overtake_time)
            signal_time=overtake_time+0.02
            print("SIGNAL L2: GREEN IN ",signal_time)

        elif response=='ZERO':
            print("NO LOOP LINE IS FREE AT THE MOMENT , PREMIUM AND LEAD TRAIN STOP L1 & ML LINES SIGNAL RED TILL EITHER LOOP LINES CLEAR")
        else:
            print("invalid response enter only options mentioned above")   
    else: 
        print("OVERTAKE  SET TO  NEXT LOOPING STATION  ALL SIGNAL: GREEN") 
        
elif reldist<=10:                  #FOR RELATIVE  DISTANCE IS LESS THAN 10 KM FLOW
    
  lspeed=int(input("Enter the Lead train speed in kmph: "))
  suc_statdis=int(input("Enter the distance from lead train to next second sucessive looping station available: "))
  premsetsp_time=(suc_statdis/lspeed)+0.02
  print("PREMIUM TRAIN REDUCE SPEED TO HALF THE MPS ",premspeed/2," kmph till in hrs:",premsetsp_time)
  print("\nML SIGNAL:YELLOW, LEAD TRAIN LOOP INTO NEXT SUCESSIVE LOOP LINE L1 FOR CROSSING, L1 SIGNAL:RED ")
  overtake_time=0.0
  overtake_time=reldist/(premspeed/2)
  print("OVERTAKING TIME : SIGNAL L1:RED:",overtake_time," hrs")
  signal_time=overtake_time+0.02
  print("SIGNAL L2: GREEN IN ",signal_time)
else:
    print("OVERTAKE NOT POSSIBLE IN THIS STRECTH, BOTH TRAINS PROCEED AS USUAL")
    
    #endofprogram
