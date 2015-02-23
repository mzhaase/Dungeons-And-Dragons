# Copyright 2015@Mattis Haase
# do whatever you want with this
# List of events based on: http://www.reddit.com/r/DnDBehindTheScreen/comments/2uyvxt/a_table_for_random_events_taking_place_in_a_large/
# Because who wants to look all this stuff up.

import random
import sys

actions = {0:{0:{0:'Squad Leader Injured', 
                 1:'Platoon Leader Injured',
                 2:'Battalion Leader Injured',
                 3:'Army Leader Injured'},
              1:{0:'Squad Leader Captured', 
                 1:'Platoon Leader Captured',
                 2:'Battalion Leader Captured',
                 3:'Army Leader Captured'},
              2:{0:'Squad Leader Fled', 
                 1:'Platoon Leader Fled',
                 2:'Battalion Leader Fled',
                 3:'Army Leader Fled'},
              3:{0:'Squad Leader Killed', 
                 1:'Platoon Leader Killed',
                 2:'Battalion Leader Killed',
                 3:'Army Leader Killed'}
              },
           1:{0:{0:'Small Enemy Reinforcements',
                 1:'Medium Enemy Reinforcements',
                 2:'Large Enemy Reinforcements',
                 3:'Gargantuan Enemy Reinforcements'
                 },
              1:{0:'Small Allied Reinforcements',
                 1:'Medium Allied Reinforcements',
                 2:'Large Allied Reinforcements',
                 3:'Gargantuan Allied Reinforcements'
                 }
              },
           2:{0:'Catapult Stone Hitting One Person 5d10 damage',
              1:{0:'Ballista Arrow Hitting One Person 3d10 damage',
                 1:'Ballista Arrow Hitting Two Persons 3d10 damage'},
              2:'Alchemist Fire, 10 foot radius, d4 fire damage on each of creatures turns DC 10 dex save to extinguish flames as action',
              3:{0:'Volley of small rocks hits nearby units, d8 damage',
                 1:'Volley of small rocks misses'},
              },
           3:'Fireball 20 foot radius, 8d6 fire damage',
           4:'A group of soldiers flees the battle. Cha check to rally them',
           5:{0:'Arrow Volley hits the nearest unit, d8 damage',
              1:'Arrow Volley does fail to deal significant damage'},
           6:{0:{0:'Enemy Cavalry Charge, STR check or fall prone',
                 1:'Enemy Cavalry Charge fails to be effective'},
              1:{0:'Allied Cavalry Charge, STR check or fall prone',
                 1:'Allied Cavalry Charge fails to be effective'}
              },
           7:{0:'Rampaging massive unit passes through the area, take damage and knocked prone',
              1:'Rampaging massive unit passes through the area, fails to do damage'},
           8:'Lightning Strike, 3d10 damage in 5 foot radius area',
           9:{0:'Medium Flying Object (10ftx10ft) crashes in area. Dexterity save DC10 or be prone, restrained underneath object and take 2d4 bludgeoning damage',
              1:'Large Flying Object (20ftx20ft) crashes in area. Dexterity save DC12 or be prone, restrained underneath object and take 2d8 bludgeoning damage',
              2:'Huge Flying Object (30ftx30ft) crashes in area. Dexterity save DC14 or be prone, restrained underneath object and take 3d10 bludgeoning damage',
              3:'Gargantuan Flying Object (40ftx40ft) crashes in area. Dexterity save DC16 or be prone, restrained underneath object and take 4d12 bludgeoning damage'},
           10:'Aerial Bombardement Could be rocks, flasks of alchemist fire, spears.',
           11:{0:'Enemy Warhorn sounds, +1 on all rolls for the next 6 rounds',
               1:'Allied Warhorn sounds, +1 on all rolls for the next 6 rounds'},
           12:{0:'Medium Burrowing Creature unburrows (10ftx10ft) in area. Dexterity save DC10 in area equal to twice creatures area or be prone take 1d4 bludgeoning damage',
              1:'Large Burrowing Creature unburrows (20ftx20ft) in area. Dexterity save DC12 in area equal to twice creatures area or be prone take 1d8 bludgeoning damage',
              2:'Huge Burrowing Creature unburrows (30ftx30ft) in area. Dexterity save DC14 in area equal to twice creatures area or be prone take 2d8 bludgeoning damage',
              3:'Gargantuan Burrowing Creature unburrows (40ftx40ft) in area. Dexterity save DC16 in area equal to twice creatures area or be prone take 2d12 bludgeoning damage'},
           13:{0:'Appearance of an old friend the party met before. He is fighting for the enemy',
               1:'Appearance of an old friend the party met before. He is fighting on the parties side'},
           14:{0:'Appearance of an old foe the party met before. He is fighting for the enemy',
               1:'Appearance of an old foe the party met before. He is fighting on the parties side'},
           15:{0:'Enemy reveals secret weapon, shock troops, good tactic: all friendly units in the area take damage equal to half their HP, enemy gets advantage on their next turn',
               1:'Ally reveals secret weapon, shock troops, good tactic: all enemy units in the area take damage equal to half their HP, allies gets advantage on their next turn'},
           16:{0:'Wounded soldier, begging for help',
               1:'Wounded soldier, screaming in pain',
               2:'Wounded soldier, in shock',
               3:'Wounded soldier, limping along, retreating',
               4:'Wounded soldier, unconcious',
               5:'Wounded soldier, unconcious or dead, Dex save or trip over'},
           17:{0:'Combat Medic enters parties area and mass heals enemies',
               1:'Combat Medic enters parties area and mass heals allies'},
           18:{0:'Druid casting Entanglement on allies and party',
               1:'Druid casting Entanglement on enemy'},
           19:{0:'Opposing side suddenly and swiftly retreats',
               1:'Allies suddenly and swiftly retreat'},
           20:'Scavengers enter the area and start picking the dead',
           21:'Bulette, gibbering mouther or similar is drawn to the battle',
           22:'Spells shriek across the battlefield. Where they mix, they interact in unpredictable ways',
           23:'A whirling mass of energy tears at anyone in its area and sucks them inexorably towards its epicentre. Determine the origin point of the vortex randomly. Everyone within a 15ft. by 15 ft. area originating in that space must make a saving throw (by element) or take 9 (3d6) damage of that element. They must also make a Strength saving throw or be pulled to the closest available space to the vortexs epicentre. Move smaller creatures first, and move creatures within the same size category based on their Strength scores (lowest to highest). The vortex disappears after 1 round. Anyone trying to move through the vortex takes automatic damage and must make a Strength saving throw to avoid being sucked into the centre (which immediately ends their movement). 1d20 roll 1-3 Acid damage. Dexterity saving throw. 4-6 Cold damage. Constitution saving throw. 7-9 Fire damage. Dexterity saving throw. 10-12 Lightning damage. Dexterity saving throw. 13-15 Thunder damage. Constitution saving throw. 16-20 Rare damage type. Roll 1d6. 1d6 roll 1-2 Poison damage. Constitution saving throw. 3-4 Necrotic damage. Constitution saving throw. 5-6 Radiant damage. Constitution saving throw.',
           24:'All creatures in the area move slowly and in flashes of movement from one still to the next, as though in stop motion. Determine the origin point of the zone randomly. Everyone within a 30 ft. by 30 ft. area is considered slowed until they leave the zone. Additionally, they cannot act on the turn immediately following the zones appearances and then every other turn after that until the zone disappears or they leave the zone. The zone disappears after 2+1d4 rounds.',
           25:'All creatures in the area suddenly find themselves teleported up into the air, then plummeting to the ground... only to blink back up into the air just before they hit. Determine the origin point of the spell randomly. Everyone within a 10 ft. by 10 ft. area originating on that space is teleported 50 ft. upward in a constant loop for 1d4 turns. On their turn, they may make a Strength saving throw and if they succeed move to the nearest space outside the affected zone, but takes falling damage based on the height they were at the time of their escape, determined at random: 1d10 roll 1-2 50 ft. 5d6 bludgeoning damage. 3-4 40 ft. 4d6 bludgeoning damage. 5-6 30 ft. 3d6 bludgeoning damage. 7-8 20 ft. 2d6 bludgeoning damage. 9-10 10 ft. 1d6 bludgeoning damage.',
           26:'A protective spell and a time-based spell have combined, and while the shield around you makes you safer, moving feels like trying to run through treacle. Determine the origin point of the spell randomly. Everyone within a 10 ft. by 10 ft. area originating in that space gains a +1 bonus to AC and resistance to all damage, but is slowed for the duration of the spell. The spell remains active on all targets for 1 round. '
           }
           
def recurseRand(d):
    if type(d)==type({}):
        random.seed()
        rnd = random.randint(0, len(d)-1)
        recurseRand(d[rnd])
    else:
        print d
    
while True:
    prompt = raw_input('Press enter to generate battle action, or type "done" to leave: ')
    if prompt != "done":
        print('\n___________________________________________\n\n')
        recurseRand(actions)
        print('\n___________________________________________\n')
    else:
        sys.exit()
    
    