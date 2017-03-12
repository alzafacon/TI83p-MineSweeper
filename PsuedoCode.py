
While stack is not empty
    # new index to consider
     
    #onto 0 not revealed yet
    if index is to 0 not revealed yet
        move as far left as possible
        
    #onto !0 not revealed yet
    if index is to !0 not revealed yet
        reveal tile (!0)
        adv to next col
        
    #add to stack (Lbl Z)
    if on 0
        add index above-left and below-left if not processed yet
    
    while index is to 0 and still in bounds
        reveal tile (0)
        
    #adv to !0
    if index is to !0
        #Lbl O/2
        #while loop?
        while index not revealed yet
            #there is possible a zero above or below (but not both)
            #calculate +1 or -1 for above or below is zero or calc 0 if neither is zero
            while index on covered !0 (still in range) and above or below is zero
                reveal !0
                addvance to next col
            
            if index switched to a 0 hidden tile
                #add to stack (Lbl Z)
                if on 0
                    add index above-left and below-left if not processed yet
                
                while index is to 0 and still in bounds
                    reveal tile (0)
            else
                #label F (this has a very tricky behaviour)
                reveal !0
        
    while already revealed 0 or !0
        pop from stack