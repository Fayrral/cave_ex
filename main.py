answer = input('Would you like to play Cave Explorer?: (yes/no) ').lower().strip()

if answer == "yes":

    answer = input("You are walking through the forest in search of an abandoned mine said to contain large quantities of gold.\n\
    It's night time and very difficult to see, however you approach a fork in the trail. Choose to go right or left: (right/left) ").lower().strip()
    
    if answer == 'right':
       
        print("You continue walking the path and choose to go right. Ahead, you can see what appears to be a small campfire in the distance.")
        
        answer = input("As you approach the campfire, you see that there is a small tent. You can't hear anyone near by but the fire is still quite large.\n\
        Do you approach the camp site or sneak around? (approach/sneak) ").lower().strip()
        
        if answer == 'sneak':
            print("You tried to sneak around the campsite but stepped in a bear trap. With no help in sight, you succumbed to your injury. The End")

        elif answer == 'approach':
            print("You approached the campsite and found it to be abandoned. You've searched the tent and found a small flask")
 
            take_kerosene = input("The flask you've located is full, but you're not sure of what. Do you steal it or leave it?: (steal/leave) ") == 'steal'

            if take_kerosene:
                print("You place the flask in your pocket for later and continue down the trail.")
                
            elif not take_kerosene:
                print("You leave the flask behind and continue down the trail.")
                
            answer = input("You've come upon a large mine shaft! Beside the mine shaft, there is a cabin. Do you wish to search the cabin or\n\
            enter the mine shaft?: (cabin/mine) ").lower().strip()
            
            if answer == 'mine':
                print("You enter the mine shaft and fall to your death. The End.")

            elif answer == 'cabin':
                print("You enter the cabin and find a corpse.")

                search_cabin = input("Do you continue to search the cabin despite the corpse?: (yes/no) ") == 'yes'

                if not search_cabin:
                    print("You leave the cabin and enter the mine shaft where you fall to your death. The End.") 

                elif search_cabin:
                    print("You have located a large length of rope and a headlamp. You used the rope to climb down into the mine.")

                    answer = input("You reach the bottom of your rope and are now in the mine shaft. You turn your light on and see two paths ahead.\n\
                    do you climb down the ladder on the right or continue straight to the left?: (ladder/straight) ").lower().strip()
            
                    if answer == ('ladder'):
                        print("You attempt to climb down the ladder, but half way down the wood becomes rotten. The ladder breaks and you fall to your death. The End.")
                    
                    elif answer == ('straight'):
                        print("You avoid the ladder and continue down the path.")

                        answer = input("As you continue down the path, you see the glimmer of a lantern shinning off the wet rock walls of the cave.\n\
                        do you continue down the path with your headlamp on or off?: (on/off) ").lower().strip()
                            
                        if answer == ('off'):
                            print("You sneak up on a chamber containing a large sleeping Ogre. He appears to be guarding a ladder to go deeper into the cave.")

                            answer = input("Do you sneak passed the Ogre to the ladder he is guarding or fight him?: (sneak/fight) ").lower().strip()

                            if answer == ('fight') and take_kerosene:
                                print("You take the flask out of your pocket for one last drink before you fight to the death. \n\
                                You open the flask and smell Kerosene! You think quickly and craft a molotov cocktail with one of your socks and the flask.\n\
                                You light the sock with the Ogre's torch as he wakes up angry. The Ogre raises his arms to bash you with his club.\n\
                                You throw the molotov cocktail right in the Ogre's face! He panick's and falls down the dark cave and you no longer hear him.")  

                                search_ogre = input("You climb down the ladder that the Ogre was guarding. He is on his stomach on the ground and is not moving.\n\
                                Do you search his pockets or continue down the path?: (search/continue) ") == 'search'

                                if search_ogre:
                                    print("You locate a journal and place it in your pocket. You continue down the path to a locked door.")

                                elif not search_ogre:
                                    print("You do not search the Ogre from fear of waking him. You continue down the path to a locked door.")

                                answer = input("You inspect the door and see a combination style lock. Do you try and open it or return to search the Ogre\n\
                                for a clue?: (open/return) ")

                                if answer == ('open') and search_ogre:
                                    print("You have found a combination in the journal you located while searching the Ogre. You try it on the door and it works!\n\
                                    You have found the hidden gold! YOU WIN, thanks for playing :)")

                                elif answer == ('return'):
                                    print("You return to the Ogre but are unable to locate him, he is no longer laying on the ground.\n\
                                        The ladder you took into the cave has been demolished.")
                    
                                    answer = input("You are trapped. Do you want to return to the door and try a random combination?: (yes/no) ").lower().strip()

                                    if answer == ('yes'):
                                        print("You attempt a random combination on the door. The door is booby trapped and you are impaled by large spikes from the ceiling.\n\
                                        The End.")

                                    elif answer == ('no'):
                                        print("You are trapped and starve to death. You spend the remainder of your days praying you're not devoured by the Ogre.\n\
                                        he End.")
                                elif answer == ('open') and not search_ogre:
                                    print("You attempt a random combination on the door. The door is booby trapped and you are impaled by large spikes from the ceiling.\n\
                                    The End.")

                            elif answer == ('fight') and not take_kerosene:
                                print("You charge valiantly towards the Ogre but are empty handed. Unfortunately the Ogre is much stronger than you and bashes you with a club. The End.")

                            elif answer == ('sneak'):
                                print("The Ogre heard you attempting to sneak and bashed you with his club. The End.")

                        elif answer == ('on'):
                            print("An Ogre charges you and clubs you to death. The End.")

    elif answer == 'left':
        print("You continue walking the path and choose to go left. The path is so dark you can't see more than three feet ahead you hear the sound of coyote's not far away searching for their next meal.\n\
        Unfortunately, that meal is you. The End.")

elif answer == 'no':
    print("You must be fun at parties!")
