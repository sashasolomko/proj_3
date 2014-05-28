##########################################################################
#COMP10001 Foundations of Computing #             25 05 2014             #
#           Project 3               #                                    #
#       Oleksandr Solomko           #                                    #
##########################################################################

from itertools import combinations

v={'3':0,'4':1,'5':2,'6':3,'7':4,'8':5,'9':6,'0':7,'J':8,
   'Q':9,'K':10,'A':11,'2':12
  }

#------------------------------------------------------------------------------

def sort_cards(hand):    
    '''Sorts a hand of cards into descending order'''
    sorted=[]
    for i in "2AKQJ09876543":
        for card in hand:
            if card[0]==i:
                sorted.append(card)
                
    return sorted

#------------------------------------------------------------------------------

def sort_cards_bck(hand):
    '''Sorts a hand of cards into ascending order'''
    sorted=[]
    for i in "34567890JQKA2":
        for card in hand:
            if card[0]==i:
                sorted.append(card)
    return sorted

#------------------------------------------------------------------------------

def check_mode(hand):
    '''This function distinguishes different modes of  plays, 
       such as straights and n of the kind,
       which is used in is_valid_play function'''   

    if hand==None:    # if player plays Pass
        return "NONE"
    
    elif len(hand)==1: # if player plays a single card
        return "n_of_kind"
    else:
        hand=sort_cards_bck(hand) #sorting cards in ascending order
        
        for i in range(len(hand)-1): 
            if v[hand[i][0]]==v[hand[i+1][0]]: #check wether the rank of cards
                return "n_of_kind"             #is equal, if yes this is  
                                               # n of a kind play

            elif len(hand)>=3:                         #checking whether condi-
                if v[hand[i][0]]==(v[hand[i+1][0]]-1):#tions of straight apply, 
                    if hand[i][1]==hand[i+1][1]:      #if yes this is a straight
                         return 'straight'            #play
                       
#------------------------------------------------------------------------------

def swap_cards(hand,pid):
    '''This function swaps the cards between players
       with respect to their player ID'''
    
    hand=sort_cards(hand)
    
    if pid==0:
        swap= hand[:2] # Player0 gives 2 highest cards to Player3
        
    elif pid==1:     
        swap= hand[:1] # Player1 gives one highest card to Player2
        
    elif pid==2:
        swap= hand[12:] # Player2 gives one random (lowest) card to Player1
        
    elif pid==3:
        swap= hand[11:] # Player3 gives two random (lowest) cards to Player0
        
    else:
        return None
    
    return swap         # returns the list of cards to swap
        
#------------------------------------------------------------------------------

def generate_plays(hand):
    '''This function generate the list of all possible plays
       with the given hand of cards'''
    
    plays=[]              
    hand=sort_cards(hand)
    
    for card in hand:          #as single cards itself are possible plays, 
        plays.append([card])   #we append them to the list
        
    for i in combinations(hand,2): #looking for a pair in all possible 
                                   #combinations of 2
        if i[0][0]==i[1][0]:      
            plays.append(list(i))  

        
    for i in combinations(hand,3):#looking for 3 of a kind in all possible 
                                  #combinations of 4
        if i[0][0]==i[1][0]==i[2][0]:
            plays.append(list(i))

        
    for i in combinations(hand,4):             #looking for 4 of a kind in all
        if i[0][0]==i[1][0]==i[2][0]==i[3][0]: #possible combinations of 4
            plays.append(list(i))
            
#------------------------------------------------------------------------------    
    
    for i in combinations(hand,3):   #looking for a straight of lenght 3 cards
        i=sort_cards_bck(i)
        
        value=v[i[0][0]] #checking if cards' value increasing by 1 without gaps 
        if value==(v[i[1][0]]-1) and\
            value==(v[i[2][0]]-2):
        
            suit=i[0][1]                  #checking if cards' suit is the same
            if suit==i[1][1] and\
               suit==i[2][1]:
                plays.append(list(i))
    
                

    for i in combinations(hand,4): #same as with combinations of 3, we now look
        i=sort_cards_bck(i)        #for the straights of the lenght 4 and more,  
                                   #checking whether conditions of straight 
        value=v[i[0][0]]           #are met 
        if value==(v[i[1][0]]-1) and\
           value==(v[i[2][0]]-2) and\
           value==(v[i[3][0]]-3):
            
            suit=i[0][1]
            if suit==i[1][1] and\
               suit==i[2][1] and\
               suit==i[3][1]:
                plays.append(list(i))

                
                
    for i in combinations(hand,5):
        i=sort_cards_bck(i)
    
        value=v[i[0][0]]
        if value==(v[i[1][0]]-1) and\
           value==(v[i[2][0]]-2) and\
           value==(v[i[3][0]]-3) and\
           value==(v[i[4][0]]-4):
        
            suit=i[0][1]
            if suit==i[1][1] and\
               suit==i[2][1] and\
               suit==i[3][1] and\
               suit==i[4][1]:
                plays.append(list(i))

            
        
    for i in combinations(hand,6):
        i=sort_cards_bck(i)
        
        value=v[i[0][0]]
        if value==(v[i[1][0]]-1) and\
           value==(v[i[2][0]]-2) and\
           value==(v[i[3][0]]-3) and\
           value==(v[i[4][0]]-4) and\
           value==(v[i[5][0]]-5):
            
            suit=i[0][1]
            if suit==i[1][1] and\
               suit==i[2][1] and\
               suit==i[3][1] and\
               suit==i[4][1] and\
               suit==i[5][1]:
                plays.append(list(i))

                

    for i in combinations(hand,7):
        i=sort_cards_bck(i)
    
        value=v[i[0][0]]
        if value==(v[i[1][0]]-1) and\
           value==(v[i[2][0]]-2) and\
           value==(v[i[3][0]]-3) and\
           value==(v[i[4][0]]-4) and\
           value==(v[i[5][0]]-5) and\
           value==(v[i[6][0]]-6):
        
            suit=i[0][1]
            if suit==i[1][1] and\
               suit==i[2][1] and\
               suit==i[3][1] and\
               suit==i[4][1] and\
               suit==i[5][1] and\
               suit==i[6][1]:
                plays.append(list(i))
            
            
            
    for i in combinations(hand,8):
        i=sort_cards_bck(i)
    
        value=v[i[0][0]]
        if value==(v[i[1][0]]-1) and\
           value==(v[i[2][0]]-2) and\
           value==(v[i[3][0]]-3) and\
           value==(v[i[4][0]]-4) and\
           value==(v[i[5][0]]-5) and\
           value==(v[i[6][0]]-6) and\
           value==(v[i[7][0]]-7):
        
            suit=i[0][1]
            if suit==i[1][1] and\
               suit==i[2][1] and\
               suit==i[3][1] and\
               suit==i[4][1] and\
               suit==i[5][1] and\
               suit==i[6][1] and\
               suit==i[7][1]:
                plays.append(list(i))    



    for i in combinations(hand,9):
        i=sort_cards_bck(i)
    
        value=v[i[0][0]]
        if value==(v[i[1][0]]-1) and\
           value==(v[i[2][0]]-2) and\
           value==(v[i[3][0]]-3) and\
           value==(v[i[4][0]]-4) and\
           value==(v[i[5][0]]-5) and\
           value==(v[i[6][0]]-6) and\
           value==(v[i[7][0]]-7) and\
           value==(v[i[8][0]]-8):
        
            suit=i[0][1]
            if suit==i[1][1] and\
               suit==i[2][1] and\
               suit==i[3][1] and\
               suit==i[4][1] and\
               suit==i[5][1] and\
               suit==i[6][1] and\
               suit==i[7][1] and\
               suit==i[8][1]:
                plays.append(list(i))                                                         
    
    return plays
     
#------------------------------------------------------------------------------

def is_valid_play(play,rnd):
    ''' This function checks whether a possible play can be made
        in the contest of the round of plays played before'''    
    
    if rnd==[]:            #If player has the lead, a pass cannot be made,
        if play==None:     #therefore FALSE if tries to pass. 
            return False
        if play!=None:     #Any play will be allowed if player has the lead,
            return True    #therefore TRUE
        
    elif play==None:      
        return True

    else:
        
        play=sort_cards_bck(play)        #Sorting cards in increasing order and 
        rnd= [sort_cards_bck(i) for i in rnd if i]#getting rid of Nones in rnd
        
                
        if check_mode(play)!= check_mode(rnd[-1]): 
                                                  #if mode of play is different 
                                                  #to mode in rnd - FALSE
            return False
        

        elif check_mode(play)==check_mode(rnd[-1]) and\
             check_mode(play) in 'straight':     
                                               #if mode of play matches to 
                                               #the mode of rnd and is straight
            if v[play[-1][0]]>v[rnd[-1][-1][0]]: 
                                               #checking if value of the highest 
                                               #card in play is greater than
                                               #the highest card in the last
                                               #play in rnd 
                    
                if len(rnd)==1:                #as that is the only condition
                                               #the play has to meet if there
                                               #is one play in rnd, return TRUE
                    return True
            
            
                elif len(rnd)>=2:
                    if rnd[0][0][1]!=rnd[1][0][1]: #if the suit of first play
                                                   #in rnd differs to the suit 
                                                   #of the second play in rnd
                        return True
                    
                    elif rnd[0][0][1]==rnd[1][0][1] and\
                         rnd[0][0][1]==play[0][1]: 
                         return True               #checking if there is one 
                                                   #possible suit can be played
                                                   #and if suit of play matches
                    else:
                        return False

            else:
                return False
    

    
                    
        elif check_mode(play)==check_mode(rnd[-1]) and\
             check_mode(play) in 'n_of_kind':   #checking whether mode of play 
                                                #matches to the mode of rnd 
                                                #and if the mode is n of kind
                                                
            if v[play[-1][0]]>v[rnd[-1][-1][0]]: #checking whether highest card
                                                 #in suit is higher than the 
                                                 #highest card in last rnd
            
                if len(play)!=len(rnd[-1]):     #FALSE if lenght of play
                    return False                #differs to lenght of last
                                                #play in rnd
                elif len(rnd)==1:
                    if len(play)==len(rnd[-1]):    
                        return True
                
                elif len(rnd)>=2:                    #if len(rnd)>=2,check
                    if rnd[0][0][1]==rnd[1][0][1]:   #whether the same suit 
                        if play[0][1]==rnd[0][0][1]: #have to be played
                            return True
                        else:
                            return False
                    elif rnd[0][0][1] != rnd[1][0][1]:
                        
                        return True                  
            else:                               
                return False                    
                                                 
             
#------------------------------------------------------------------------------            
                          
def play(rnd,hand,discard,holding,generate=generate_plays,valid=is_valid_play):
    
    valid_plays=[]            
    
    hand=generate_plays(hand) #obtaining possible plays with provided 
                              #hand of cards
    
    if discard[-1]==[]:       #If player has the lead, any play from 
        return hand[-1]       #generate_plays would be valid
    
    else:

        for i in range(len(hand)-1):       
            
            if is_valid_play(hand[i],rnd):  #if the play in hand is valid in 
                valid_plays.append(hand[i]) #the context of rnd, we append it 
                                            #to the list of possible plays.
                
        if valid_plays==[]: #if there are no possible plays, pass
            return None 
                   
        return valid_plays[-1]  #return a play of lowest value 
                    
    
    
#------------------------------------------------------------------------------         
    
    
    

                        
                

                                            
                    

        
        

    






















​
