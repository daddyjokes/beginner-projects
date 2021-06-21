import random

def main():
    character = False
    hp = 100
    maxhp = 100
    defe = 0
    stm = 15
    maxstm = 15
    
    strx = 0
    defx = 0
    stmx = 0
    luck = 0
    gold = 100
    
    #BOOLEANS
    bash = False
    overhead = False
    levelup = True
    move = True
    search = False
    shop = False
    bshield = False
    gshield = False
    tshield = False
    lwish = False
    ewish = False
    rwish = False
    cwish = False
    
    n_enemy = 0
    room = 0
    target_index = 0
    enemy_desc = []
    enemy_names = []
    enemies = []
    
    inv = ['antidote','antidote','potion of healing']
    w_armor = 'leather armor'
    w_ring = []
    lweapon = ''
    rweapon = 'rusty iron sword'
    latk = 1
    ratk = 1
    
    starting_items = ('shortsword','bow','spear','buckler shield','chainmail armor','platemail armor','antidote','torch')
    choices = 3
    
    print starting_items
    start = True
    while hp > 0:
        #HP,DODGE CHANCE,%COMMON,%RARE,%EPIC,%LEGENDARY,DEBUFFED?,DESCRIPTION,NAME (LEN=10)
        slime = [int(random.randint(1,8)),1,10,0,0,0,'','a small green slime','slime','divide'] #4,10. 100-0-0-0
        chicken = [int(random.randint(1,6)),1,10,0,0,0,'','a chicken','chicken',''] #3,10. 100-0-0-0
        spider = [int(random.randint(1,10)),0,10,0,0,0,'','a black, spooky, giant spider','spider',''] #5,00. 100-0-0-0
        crab = [int(random.randint(1,6)),1,10,0,0,0,'','a swol mudcrab','crab',''] #3,00. 100-0-0-0
        pixie = [int(random.randint(1,10)),3,8,2,0,0,'','a tiny orb of light','pixie',''] #5,30. 80-20-0-0
        goblin = [int(random.randint(1,10)),1,9,1,0,0,'','a savage goblin','goblin',''] #5,10. 90-10-0-0
        warg = [4*int(random.randint(1,4)),1,8,2,0,0,'','a ferocious, armored feral warg','warg',''] #8,10. 80-20-0-0
        zombie = [3*int(random.randint(1,6)),0,7,3,0,0,'','a rotting zombie','zombie','reincarnation'] #9,00. 70-30-0-0
        skeleton = [2*int(random.randint(1,6)),2,7,3,0,0,'','a S P O O K Y SKELETON','skeleton','reincarnation'] #6,20. 70-30-0-0
        orc = [4*int(random.randint(1,8)),2,4,6,0,0,'','a corrupted, black orc warrior','orc',''] #16,20. 40-60-0-0
        hobgoblin = [4*int(random.randint(1,6)),2,1,7,2,0,'','a superior goblin','hobgoblin',''] #12,20. 10-70-20-0
        ghost = [int(random.randint(1,20)),5,0,0,10,0,'','a S P O O K Y GHOST','ghost','reincarnation'] #10,50. 0-0-100-0
        troll = [10+int(4*int(random.randint(1,8))),0,0,7,3,0,'','a hairy, tough, smelly troll','troll','regen'] #26,00. 0-70-30-0
        broodmother = [15+int(3*int(random.randint(1,10))),1,0,5,5,0,'','egg-infested spider queen','broodmother','divide'] #30,10. 0-50-50-0
        ghoul = [15+int(3*int(random.randint(1,12))),3,0,6,4,0,'','a white, wiry, hairless undead','ghoul','regen'] #33,30. 0-60-40-0
        ogre = [15+int(5*int(random.randint(1,10))),0,1,7,2,0,'','an brown-skinned ogre','ogre','regen'] #40,00. 10-70-20-0
        cyclop = [10*int(random.randint(1,10)),0,0,3,6,1,'','a warrior horned cyclop','cyclop',''] #50,00. 0-30-60-10
        griffin = [20+int(2*int(random.randint(1,20))),2,0,1,8,1,'','(a gold-armored wild griffin)','griffin',''] #40,20. 0-10-80-10
        bicorn = [30+int(2*int(random.randint(1,20))),3,0,0,9,1,'','a corrupted bicorn','bicorn',''] #50,30. 0-0-90-10
        vampire = [20+int(5*int(random.randint(1,8))),4,0,0,8,2,'','a vampiric nobleman','vampire','regen'] #40,40. 0-0-80-20
        mummy = [30+int(5*int(random.randint(1,8))),1,0,0,7,3,'','an ancient undead God-King','mummy','reincarnation'] #50,10. 0-0-70-30
        hydra = [int(15*int(random.randint(4,8))),1,0,0,9,1,'','an 8-headed draconic beast','hydra','regen'] #90,10. 0-0-90-10
        giant_chicken = [int(random.randint(1,100)),2,0,0,6,4,'','a GIANT CHICKEN','giant chicken','divide'] #50,20. 0-0-60-40
        giant = [60+int(4*int(random.randint(1,10))),0,0,0,6,4,'','a primordial human','giant',''] #80,00. 0-0-60-40
        fire_elemental = [60+int(random.randint(1,20)),2,0,0,6,4,'','a wrathful flaming essence','fire elemental','explode'] #70,20. 0-0-60-40
        titan = [80+int(4*int(random.randint(1,10))),0,0,0,5,5,'','a collosal primordial guardian','titan',''] #100,00. 0-0-50-50
        lich = [70+int(10*int(random.randint(1,6))),1,0,0,5,5,'','a powerful undead necromancer','lich','reincarnation'] #100,10. 0-0-50-50
        death_knight = [80+int(10*int(random.randint(1,10))),2,0,0,4,6,'','a champion of Death','death knight',''] #130,20. 0-0-40-60
        demon = [50+int(20*int(random.randint(1,10))),3,0,0,7,3,'','an infernal, red-skinned servant','demon','regen'] #150,30. 0-0-70-30
        angel = [50+int(20*int(random.randint(1,10))),3,0,0,7,3,'','a blazing, Light-armored herald','angel','regen'] #150,30. 0-0-70-30
        wyvern = [20*int(random.randint(1,10)),5,0,0,6,4,'','a protodraconic beast','wyvern',''] #100,50. 0-0-60-40
        elder_lich = [150+int(10*int(random.randint(1,4))),1,0,0,2,8,'','a scholar of Death','elder lich','reincarnation'] #170,10. 0-0-20-80
        dragon = [200+int(10*int(random.randint(1,10))),0,0,0,0,10,'','a DRAGON','dragon',''] #250,00. 0-0-0-100
        archdemon = [100+int(10*int(random.randint(1,20))),3,0,0,1,9,'','the Abyssal','archdemon','regen'] #200,30. 0-0-10-90
        archangel = [100+int(10*int(random.randint(1,20))),3,0,0,1,9,'','the Radient','archangel','regen'] #200,30. 0-0-10-90
        demigod = [200+int(10*int(random.randint(1,20))),4,0,0,0,10,'','the Divine','demigod','regen'] #300,40. 0-0-0-100
        room1 = (slime,slime,chicken,crab,spider)
        room2 = (spider,spider,pixie,goblin)
        room3 = (goblin,goblin,warg,zombie,skeleton)
        room4 = (skeleton,orc,hobgoblin,hobgoblin,ghost)
        room5 = (orc,orc,hobgoblin,ghost,troll,broodmother,ghoul)
        room6 = (broodmother,ghoul,ogre,ogre,cyclop,griffin,bicorn,vampire)
        room7 = (vampire,mummy,hydra,giant_chicken,giant,fire_elemental)
        room8 = (fire_elemental,fire_elemental,giant,titan,lich,death_knight)
        room9 = (death_knight,demon,angel,wyvern,elder_lich)
        room10 = (elder_lich,dragon,archdemon,archangel,demigod)
        list_enemies = ('LIST INDEX PLACEHOLDER',room1,room2,room3,room4,room5,room6,room7,room8,room9,room10)
        
        common = (('shortsword',6),('bow',9),('spear',7),('buckler shield',6),('chainmail armor',8),('antidote',15),('axe',7),('torch',5))
        rare = (('platemail armor',13),('greatsword',12),('greatbow',18),('ghost ring',35),('halberd',15),('potion of healing',25),('veteran armor',16),('crossbow',13),('greatshield',12),('scalemail armor',16))
        epic = (('tower shield',20),('flaming sword',25),('sun bow',30),('bloodied rapier',40),('fire heart',77),('demonscale armor',56),('drumstick',50),('necroatic spear',45),('celestial armor',55),('life ring',70),('flight ring',70),('cannon',95),('dark armor',75),('saints flail',120),('greater potion of healing',50),('warden armor',85),('rune armor',100))
        legendary = (('pale axe',140),('horned blade',140),('dragonbone armor',130),('ambrosia',200),('soul of greed',150),('soul of wrath',150),('soul of sloth',150),('soul of pride',140),('soul of lust',150),('soul of envy',160),('soul of gluttony',150),('star',200),('hourglass',200),('skull ring',135),('perfection ring',145),('Longinus',190),('collosal dwarven armor',190),('god armor',200))
        
        weapons = (('rusty iron sword',int(2*int(random.randint(1,4))-1),''),('shortsword',2*int(random.randint(1,4)),''),('bow',int(4*int(random.randint(1,6))),''),('spear',2*int(random.randint(1,6)),''),('buckler shield',2*int(random.randint(1,2)),''),('axe',2*int(random.randint(1,8)),''),('torch',2*int(random.randint(1,3)),'flame'),('greatsword',int(4*int(random.randint(1,6))),''),('greatbow',int(6*int(random.randint(1,6))),''),('halberd',int(2*int(random.randint(5,8))+3),''),('crossbow',int(2*int(random.randint(3,8))+2),''),('greatshield',2*int(random.randint(1,8)),''),('tower shield',2*int(random.randint(1,10)),''),('flaming sword',int(4*int(random.randint(5,7))),'flame'),('sun bow',int(5*int(random.randint(3,6))),'flame'),('bloodied rapier',int(5*int(random.randint(5,7))),'lifesteal'),('drumstick',int(2*int(random.randint(10,20))),'CHICKEN'),('necroatic spear',int(8*int(random.randint(3,7))),'lifesteal'),('cannon',int(6*int(random.randint(2,12))),''),('saints flail',int(8*int(random.randint(5,7))),'flame'),('pale axe',int(8*int(random.randint(6,8))),'crit'),('horned blade',int(2*int((int(random.randint(1,20))+int(random.randint(1,20))+int(random.randint(1,20))))),'lifesteal'),('Longinus',int(10*int(random.randint(5,7))),'flame'))
        armor = ('leather armor','chainmail armor','platemail armor','veteran armor','scalemail armor','demonscale armor','celestial armor','dark armor','warden armor','rune armor','dragonbone armor','collosal dwarven armor','god armor')
        rings = ('ghost ring','life ring','flight ring','soul of greed','soul of wrath','soul of sloth','soul of pride','soul of lust','soul of envy','soul of gluttony','skull ring','perfection ring')
        consume = ('antidote','potion of healing','fire heart','greater potion of healing','ambrosia','star','hourglass')
        
        twoweapon = ['bow','greatbow','sun bow','cannon','greatsword','flaming sword','horned blade']
        
        if strx < 0:
            strx = 0
        if stmx < 0:
            stmx = 0
        
        #STARTING ITEMS    
        if character == False:
            if choices > 0:
                choice = raw_input('Choose (' +str(choices) +str(') items to start with: ') +str('(1-') +str(len(starting_items)) +str(') '))
                if choice == 'whosyourdaddy':
                    print '\n\n\nKONAMI CODE ACTIVATED\n\n\n'
                    hp = 999999999
                    maxhp = 999999999
                    stm = 999999999
                    maxstm = 999999999
                    lweapon = 'Longinus'
                    rweapon = 'Longinus'
                    gold = 999999999
                    choices = 0
                    for i in range(len(common)):
                        inv.append(common[i][0])
                    for i in range(len(rare)):
                        inv.append(rare[i][0])
                    for i in range(len(epic)):
                        inv.append(epic[i][0])
                    for i in range(len(legendary)):
                        inv.append(legendary[i][0])
                else:
                    try:
                        if int(choice) <= 8:
                            inv.append(starting_items[int(choice)-1])
                            choices += -1
                            print inv
                        else:
                            print 'Choose an item using numbers 1-' +str(len(starting_items)) +str('.')
                    except ValueError:
                        print 'Choose an item using numbers 1-' +str(len(starting_items)) +str('.')
            else:
                character = True
        else:
            if start == True:
                print '\nCommands:     \n/help: show this menu\n     /attack: show attack commands\n     /use: use/equip an item\n     /gear: shows equipment and stats\n     /search: searches the current room'
                print "Don't forget to equip your items."
                start = False
            else:
                if not enemies:
                    print 'When ready to advance, /ready.'
                
                if room > 0:
                    if enemies:
                        print '\nYou encounter ' +str(enemy_names) +str('!')
                
                
                
                
                
                commands = ['/ready','/help','/attack','/use','/gear','target','/search','al','ar','ahl','ahr','ak','ab','aoh','als','ars']
                command = raw_input('\nCommand: ')
                        
                if command == '/ready':
                    levelup = False
                    stm = maxstm
                    move = True
                    #DUNGEON()
                    if not enemies:
                        search = True
                        room += 1
                        if int(room)%3 == 0:
                            if room != 0:
                                shop = True
                        if room < 10:
                            #ROOM SIZE
                            size = random.randint(1,3)
                            #NUMBER OF ENEMIES IN ROOM
                            n_enemy = int(round(int(size)*1.7))
                            #DIFFICULTY/TYPE OF ENEMIES
                            enemies = []
                            enemy_desc = []
                            enemy_names = []
                            for i in range(n_enemy):
                                enemy = random.choice(list_enemies[room])
                                enemies.append(list(enemy))
                                enemy_desc.append(enemy[7])
                                enemy_names.append(enemy[8])
                        if room == 10:
                            print 'The end is near!'
                            size = 3
                            n_enemy = 5
                            enemies = []
                            enemy_desc = []
                            enemy_names = []
                            for i in range(n_enemy):
                                enemy = random.choice(list_enemies[room])
                                enemies.append(list(enemy))
                                enemy_desc.append(enemy[7])
                                enemy_names.append(enemy[8])
                            
                        room_size = 'small' #DEFAULT = SMALL
                        if size == 1:
                            room_size = 'small'
                        if size == 2:
                            room_size = 'medium'
                        if size == 3:
                            room_size == 'large'
                        print 'You enter a ' +str(room_size) +str(' room with (') +str(n_enemy) +str(') enemies inside. In front of you is ') +str(enemy_desc) +str('.')
                    else:
                        print 'Room is not yet cleared.'
                    
                if command == '/help':
                    print 'Commands:\n     /help: show this menu\n     /attack: show attack commands\n     /use: use an item\n     /search: searches the current room'
                
                if command == '/attack':
                    print 'Commands:\nTo attack, type in the target name then choose an attack option.\n     al: ([attack] left) attack with left hand weapon\n     ar: ([attack] right) attack with right hand weapon\n     ahl: ([attack] heavy left) strong left attack\n     ahr: ([attack] heavy right)strong right attack\n     ak: ([attack] kick) kicks; breaks guard\n     ab: ([attack] bash) defensive blunt attack; most effective with shield (100% hit rate)\n     aoh: ([attack] overhead) two-hands right hand weapon for strong attack; leaves user vulnerable\n     als: ([attack] left sweep) left attack damaging two enemies\n     ars: ([attack] right sweep) right attack damaging multiple enemies'
                
                if command == '/use':
                    print inv
                    use = raw_input('Which item would you like to use? ')
                    print ''
                    if use not in inv:
                        print 'Item not found'
                    else:
                        #EQUIP WEAPONS
                        for i in range(len(weapons)):
                            if use == weapons[i][0]:
                                move = False
                                #TWO HANDED?
                                if weapons[i][0] in twoweapon:
                                    inv.append(lweapon)
                                    inv.append(rweapon)
                                    lweapon = ''
                                    latk = 1
                                    rweapon = weapons[i][0]
                                    inv.remove(rweapon)
                                    ratk = weapons[i][1]
                                    print 'You wield the ' +str(weapons[i][0]) +str(' with your right hand.')
                                else:
                                    hand = raw_input('Which hand would you like to use this weapon with? ')
                                    if hand == 'left':
                                        inv.append(lweapon)
                                        lweapon = use
                                        inv.remove(lweapon)
                                        latk = weapons[i][1]
                                    if hand == 'right':
                                        inv.append(rweapon)
                                        rweapon = use
                                        inv.remove(rweapon)
                                        ratk = weapons[i][1]
                                if lweapon != '':
                                    if rweapon in twoweapon:
                                        inv.append(rweapon)
                                        rweapon = ''
                                        ratk = 1
                                #SHIELD
                                bshield = False
                                gshield = False
                                tshield = False
                                if lweapon or rweapon == 'buckler shield':
                                    defx += 1
                                    bshield = True
                                if lweapon or rweapon == 'greatshield':
                                    defx += 2
                                    gshield = True
                                if lweapon or rweapon == 'tower shield':
                                    defx += 4
                                    stmx += -1
                                    tshield = True
                                if bshield == True:
                                    if lweapon or rweapon != 'buckler shield':
                                        defx += -1
                                        bshield = False
                                if gshield == True:
                                    if lweapon or rweapon != 'great shield':
                                        defx += -2
                                        gshield = False
                                if tshield == True:
                                    if lweapon or rweapon != 'tower shield':
                                        defx += -4
                                        stmx += 1
                                        tshield = False
                                        
                                #DUAL WIELDING
                                dw = False
                                if lweapon == rweapon:
                                    dw = True
                                if dw == True:
                                    if lweapon != rweapon:
                                        strx += -4
                                        dw = False
                                    else:
                                        strx += 4
                        
                        #ARMOR STATS                    
                        if use in armor:
                            move = False
                            #TAKE OFF ARMOR
                            defe = 0
                            if w_armor == 'platemail armor':
                                stmx += +1
                            if w_armor == 'veteran armor':
                                strx += -1
                                stmx += -1
                            if w_armor == 'demonscale armor':
                                strx += -2
                                stmx += -1
                            if w_armor == 'celestial armor':
                                strx += -1
                                stmx += -3
                            if w_armor == 'dark armor':
                                strx += -3
                                stmx += -3
                            if w_armor == 'warden armor':
                                strx += -2
                                stmx += -2
                            if w_armor == 'rune armor':
                                strx += -1
                                stmx += -1
                            if w_armor == 'colossal dwarven armor':
                                strx += -1
                                stmx += +2
                            if w_armor == 'dragonbone armor':
                                strx += -5
                                stmx += -5
                            if w_armor == 'god armor':
                                strx += -7
                                stmx += -7
                            inv.append(w_armor)
                            w_armor = use
                            inv.remove(w_armor)
                            #PUT ON ARMOR
                            if w_armor == 'chainmail armor':
                                defe += 1
                            if w_armor == 'platemail armor':
                                defe += 2
                                stmx += -1
                            if w_armor == 'veteran armor':
                                defe += 2
                                strx += 1
                                stmx += 1
                            if w_armor == 'scalemail armor':
                                defe += 2
                            if w_armor == 'demonscale armor':
                                defe += 3
                                strx += 2
                                stmx += 1
                            if w_armor == 'celestial armor':
                                defe += 2
                                strx += 1
                                stmx += 3
                            if w_armor == 'dark armor':
                                defe += 3
                                strx += 3
                                stmx += 3
                            if w_armor == 'warden armor':
                                defe += 4
                                strx += 2
                                stmx += 2
                            if w_armor == 'rune armor':
                                defe += 5
                                strx += 1
                                stmx += 1
                            if w_armor == 'colossal dwarven armor':
                                defe += 7
                                strx += 1
                                stmx += -2
                            if w_armor == 'dragonbone armor':
                                defe += 5
                                strx += 5
                                stmx += 5
                            if w_armor == 'god armor':
                                defe += 6
                                strx += 7
                                stmx += 7
                        
                        #RING STATS    
                        if use in rings:
                            move = False
                            w_ring.append(use)
                            inv.remove(use)
                            if 'ghost ring' == use:
                                defx += 2
                            if 'life ring' == use:
                                maxhp += 75
                            if 'flight ring' == use:
                                stmx += 3
                            if 'soul of greed' == use:
                                gold += 300
                                luck += 10
                                greedy = random.choice(legendary)
                                inv.append(greedy[0])
                                print 'You have gained a ' +str(greedy[0]) +str('!')
                                print 'You have gained 300 gold!'
                                print 'Gold: ' +str(gold)
                            if 'soul of wrath' == use:
                                strx += 7
                                stmx += 2
                            if 'soul of sloth' == use:
                                stmx += -2
                                maxhp += 200
                                hp += 200
                            if 'soul of pride' == use:
                                hp = maxhp
                                strx += 3
                                luck += 1
                            if 'soul of lust' == use:
                                defx += 2
                                luck += 2
                            if 'soul of envy' == use:
                                print ''
                                for i in range(len(epic)):
                                    print epic[i][0]
                                print ''
                                envious = raw_input('Choose a gift! ')
                                for i in range(len(epic)):
                                    if envious == epic[i][0]:
                                        inv.append(epic[i][0])
                                        print 'You have gained a ' +str(epic[i][0]) +str('!')
                                        break
                                else:
                                    print 'Invalid Item!'
                            if 'soul of gluttony' == use:
                                maxhp += 100
                                hp += 100
                                luck += 2
                            if 'skull ring' == use:
                                strx += 5
                            if 'perfection ring' == use:
                                strx += 3
                                stmx += 3
                                defx += 3
                                maxhp += 100
                                
                        if use in consume:
                            inv.remove(use)
                            if use == 'antidote':
                                hp += 5*int(random.randint(1,10)) + 20
                                print 'You regained ' +str(3*int(random.randint(1,10)) + 20) +str(' health!')
                            if use == 'potion of healing':
                                hp += 7*int(random.randint(1,10)) + 35
                                print 'You regained ' +str(4*int(random.randint(1,10)) + 35) +str(' health!')
                            if use == 'fire heart':
                                maxhp += 100
                                hp += 100
                                defx += 1
                                print 'You regained 100 health!\nYour defense increased!'
                            if use == 'greater potion of healing':
                                hp += 10*int(random.randint(1,10)) + 50
                                print 'You regained ' +str(6*int(random.randint(1,10)) + 50) +str(' health!')
                            if use == 'ambrosia':
                                maxhp += 40
                                hp = maxhp
                                print 'You are fully healed!'
                            lwish = False
                            ewish = False
                            rwish = False
                            cwish = False
                            if use == 'star':
                                print ''
                                for i in range(len(common)):
                                    print common[i][0]
                                print ''
                                for i in range(len(rare)):
                                    print rare[i][0]
                                print ''
                                for i in range(len(epic)):
                                    print epic[i][0]
                                print ''
                                for i in range(len(legendary)):
                                    print legendary[i][0]
                                print ''
                                wish = raw_input('Choose your wish! ')
                                for i in range(len(legendary)):
                                    if wish == legendary[i][0]:
                                        inv.append(wish)
                                        print 'Your wish has been granted! You have gained a ' +str(wish) +str('!')
                                        lwish = True
                                        break
                                    else:
                                        lwish = False
                                for i in range(len(epic)):
                                    if wish == epic[i][0]:
                                        inv.append(wish)
                                        print 'Your wish has been granted! You have gained a ' +str(wish) +str('!')
                                        ewish = True
                                        break
                                    else:
                                        ewish = False
                                for i in range(len(rare)):
                                    if wish == rare[i][0]:
                                        inv.append(wish)
                                        print 'Your wish has been granted! You have gained a ' +str(wish) +str('!')
                                        rwish = True
                                        break
                                    else:
                                        rwish = False
                                for i in range(len(common)):
                                    if wish == common[i][0]:
                                        inv.append(wish)
                                        print 'Your wish has been granted! You have gained a ' +str(wish) +str('!')
                                        cwish = True
                                        break
                                    else:
                                        cwish = False
                                if lwish == False:
                                    if ewish == False:
                                        if rwish == False:
                                            if cwish == False:
                                                inv.append('star')
                                                print 'Your wish failed. Please try again.'
                            if use == 'hourglass':
                                if int(room)-2 < 0:
                                    room = 0
                                else:
                                    room += -2
                                print 'The flow of time winds, stops, then reverses. Kaleidoscopic images, flow, combine, and break apart, and you fall into a daze.\n'
                
                #ATTACKS
                #VALID TARGET?
                if command in enemy_names:
                    for i in range(len(weapons)):
                        if lweapon == weapons[i][0]:
                            latk = weapons[i][1]
                        if rweapon == weapons[i][0]:
                            ratk = weapons[i][1]
                    if lweapon == '':
                        latk = 1
                    if rweapon == '':
                        ratk = 1
                        
                    target = command
                    n = 0
                    for i in range(len(enemy_names)):
                        if enemy_names[n] == target:
                            target_index = i
                            break
                        n += 1
                    attacks = ['al','ar','ahl','ahr','ak','ab','aoh','als','ars']
                    attack = raw_input('How would you like to attack? ')
                    #VALID ATTACK?
                    if attack in attacks:
                        lhit = random.randint(1,10)
                        hhit = int(random.randint(1,10)) - 2
                        if attack == 'al':
                            #ENOUGH STAMINA?
                            if stm >= 2:
                                #ROLL TO HIT
                                if int(lhit) > int(enemies[target_index][1]):
                                    #DAMAGE
                                    if lweapon != '':
                                        if lweapon[2] == 'lifesteal':
                                            hp += int(round(int(latk)/4))
                                            print 'You healed for ' +str(int(round(int(latk)/2))) +str(' health!')
                                        if lweapon[2] == 'flame':
                                            enemies[target_index][8] = 'flame'
                                        if lweapon[2] == 'CHICKEN':
                                            enemies[target_index][8] = 'CHICKEN'
                                        if lweapon[2] == 'crit':
                                            crit = int(random.randint(1,15))
                                            if crit == 1:
                                                enemies[target_index][0] = int(enemies[target_index][0]) - int(latk) - int(strx) - 20
                                                print 'You CRIT!'
                                                print 'You did ' +str(int(latk)+int(strx))+20 +str(' damage to ') +str(target) +str('.')
                                            else:
                                                enemies[target_index][0] = int(enemies[target_index][0]) - int(round(1.5*int(ratk))) - int(strx)
                                                print 'You did ' +str(int(round(1.5*int(ratk)))+int(strx)) +str(' damage to ') +str(target) +str('.')
                                        else:
                                            enemies[target_index][0] = int(enemies[target_index][0]) - int(latk) - int(strx)
                                            print 'You did ' +str(int(latk)+int(strx)) +str(' damage to ') +str(target) +str('.')
                                    else:
                                        enemies[target_index][0] = int(enemies[target_index][0]) - 1
                                        print 'You did 1' +str(' damage to ') +str(target) +str('.')
                                else:
                                    print 'It dodged your attack!'
                                stm += -2
                            else:
                                print 'Not enough stamina'
                        if attack == 'ar':
                            if stm >= 2:
                                if int(lhit) > int(enemies[target_index][1]):
                                    if rweapon != '':
                                        if rweapon[2] == 'lifesteal':
                                            hp += int(round(int(ratk)/4))
                                            print 'You healed for ' +str(int(round(int(ratk)/2))) +str(' health!')
                                        if rweapon[2] == 'flame':
                                            enemies[target_index][8] = 'flame'
                                        if rweapon[2] == 'CHICKEN':
                                            enemies[target_index][8] = 'CHICKEN'
                                        if rweapon[2] == 'crit':
                                            crit = int(random.randint(1,15))
                                            if crit == 1:
                                                enemies[target_index][0] = int(enemies[target_index][0]) - int(ratk) - int(strx) - 20
                                                print 'You CRIT!'
                                                print 'You did ' +str(int(ratk)+int(strx))+20 +str(' damage to ') +str(target) +str('.')
                                            else:
                                                enemies[target_index][0] = int(enemies[target_index][0]) - int(round(1.5*int(ratk))) - int(strx)
                                                print 'You did ' +str(int(round(1.5*int(ratk)))+int(strx)) +str(' damage to ') +str(target) +str('.')
                                        else:
                                            enemies[target_index][0] = int(enemies[target_index][0]) - int(ratk) - int(strx)
                                            print 'You did ' +str(int(ratk)+int(strx)) +str(' damage to ') +str(target) +str('.')
                                    else:
                                        enemies[target_index][0] = int(enemies[target_index][0]) - 1
                                        print 'You did 1' +str(' damage to ') +str(target) +str('.')
                                else:
                                    print 'It dodged your attack!'
                                stm += -2
                            else:
                                print 'Not enough stamina'
                        if attack == 'ahl':
                            if stm >= 4:
                                if int(hhit) > int(enemies[target_index][1]):
                                    if lweapon != '':
                                        if lweapon[2] == 'lifesteal':
                                            hp += int(round(int(latk)/4))
                                            print 'You healed for ' +str(int(round(int(latk)/2))) +str(' health!')
                                        if lweapon[2] == 'flame':
                                                enemies[target_index][8] = 'flame'
                                        if lweapon[2] == 'CHICKEN':
                                            enemies[target_index][8] = 'CHICKEN'
                                        if lweapon[2] == 'crit':
                                            crit = int(random.randint(1,15))
                                            if crit == 1:
                                                enemies[target_index][0] = int(enemies[target_index][0]) - int(round(1.5*int(latk))) - int(strx) - 20
                                                print 'You CRIT!'
                                                print 'You did ' +str(int(round(1.5*int(latk)))+int(strx))+20 +str(' damage to ') +str(target) +str('.')
                                            else:
                                                enemies[target_index][0] = int(enemies[target_index][0]) - int(round(1.5*int(ratk))) - int(strx)
                                                print 'You did ' +str(int(round(1.5*int(ratk)))+int(strx)) +str(' damage to ') +str(target) +str('.')
                                        else:
                                            enemies[target_index][0] = int(enemies[target_index][0]) - int(round(1.5*int(latk))) - int(strx)
                                            print 'You did ' +str(int(round(1.5*int(latk)))+int(strx)) +str(' damage to ') +str(target) +str('.')
                                    else:
                                        enemies[target_index][0] = int(enemies[target_index][0]) - 1
                                        print 'You did 1' +str(' damage to ') +str(target) +str('.')
                                else:
                                    print 'It dodged your attack!'
                                stm += -4
                            else:
                                print 'Not enough stamina'
                        if attack == 'ahr':
                            if stm >= 4:
                                if int(hhit) > int(enemies[target_index][1]):
                                    if rweapon != '':
                                        if rweapon[2] == 'lifesteal':
                                            hp += int(round(int(ratk)/4))
                                            print 'You healed for ' +str(int(round(int(ratk)/2))) +str(' health!')
                                        if rweapon[2] == 'flame':
                                                enemies[target_index][8] = 'flame'
                                        if rweapon[2] == 'CHICKEN':
                                            enemies[target_index][8] = 'CHICKEN'
                                        if rweapon[2] == 'crit':
                                            crit = int(random.randint(1,15))
                                            if crit == 1:
                                                enemies[target_index][0] = int(enemies[target_index][0]) - int(round(1.5*int(ratk))) - int(strx) - 20
                                                print 'You CRIT!'
                                                print 'You did ' +str(int(round(1.5*int(ratk)))+int(strx))+20 +str(' damage to ') +str(target) +str('.')
                                            else:
                                                enemies[target_index][0] = int(enemies[target_index][0]) - int(round(1.5*int(ratk))) - int(strx)
                                                print 'You did ' +str(int(round(1.5*int(ratk)))+int(strx)) +str(' damage to ') +str(target) +str('.')
                                        else:
                                            enemies[target_index][0] = int(enemies[target_index][0]) - int(round(1.5*int(ratk))) - int(strx)
                                            print 'You did ' +str(int(round(1.5*int(ratk)))+int(strx)) +str(' damage to ') +str(target) +str('.')
                                    else:
                                        enemies[target_index][0] = int(enemies[target_index][0]) - 1
                                        print 'You did 1' +str(' damage to ') +str(target) +str('.')
                                else:
                                    print 'It dodged your attack!'
                                stm += -4
                            else:
                                print 'Not enough stamina'
                        if attack == 'ak':
                            if stm >= 3:
                                enemies[target_index][0] = int(enemies[target_index][0]) - int(round(int(int(latk)+int(ratk))/4))
                                print 'You did ' +str(int(round(int(int(latk)+int(ratk))/4))) +str(' damage to ') +str(target) +str('.')
                                #REDUCE DODGE CHANCE
                                if enemies[target_index][8] == '':
                                    enemies[target_index][8] = 'kick'
                                    int(enemies[target_index][1]) - 5
                            else:
                                print 'Not enough stamina'
                        if attack == 'ab':
                            if bshield or gshield or tshield == True:
                                bash = True
                                if bash == True:
                                    defx += 4
                            if latk < ratk:
                                enemies[target_index][0] = int(enemies[target_index][0]) - int(round(int(latk)*3/5))
                                print 'You did ' +str(int(round(int(latk)*3/5))) +str(' damage to ') +str(target) +str('.')
                            else:
                                enemies[target_index][0] = int(enemies[target_index][0]) - int(round(int(ratk)*3/5))
                                print 'You did ' +str(int(round(int(ratk)*3/5))) +str(' damage to ') +str(target) +str('.')
                        if attack == 'aoh':
                            if stm >= 5:
                                overhead = True
                                defx += -2
                                if int(hhit) + 1 > int(enemies[target_index][1]):
                                    if rweapon != '':
                                        if rweapon[2] == 'flame':
                                                enemies[target_index][8] = 'flame'
                                        if rweapon[2] == 'CHICKEN':
                                            enemies[target_index][8] = 'CHICKEN'
                                        if rweapon[2] == 'crit':
                                            crit = int(random.randint(1,15))
                                            if crit == 1:
                                                enemies[target_index][0] = int(enemies[target_index][0]) - int(round(2.5*int(ratk))) - int(strx) - 20
                                                print 'You CRIT!'
                                                print 'You did ' +str(int(round(2.5*int(ratk)))+int(strx))+20 +str(' damage to ') +str(target) +str('.')
                                            else:
                                                enemies[target_index][0] = int(enemies[target_index][0]) - int(round(2.5*int(ratk))) - int(strx)
                                                print 'You did ' +str(int(round(2.5*int(ratk)))+int(strx)) +str(' damage to ') +str(target) +str('.')
                                        else:
                                            enemies[target_index][0] = int(enemies[target_index][0]) - int(round(2.5*int(ratk))) - int(strx)
                                            print 'You did ' +str(int(round(2.5*int(ratk)))+int(strx)) +str(' damage to ') +str(target) +str('.')
                                    else:
                                        enemies[target_index][0] = int(enemies[target_index][0]) - 1
                                        print 'You did 1' +str(' damage to ') +str(target) +str('.')
                                else:
                                    print 'It dodged your attack!'
                                stm += -5
                            else:
                                print 'Not enough stamina'
                        if attack == 'als':
                            if stm >= 7:
                                if int(hhit)+2 > int(enemies[target_index][1]):
                                    if lweapon != '':
                                        if lweapon[2] == 'flame':
                                            enemies[target_index][8] = 'flame'
                                        if lweapon[2] == 'CHICKEN':
                                            enemies[target_index][8] = 'CHICKEN'
                                        if lweapon[2] == 'crit':
                                            crit = int(random.randint(1,15))
                                            #CRIT SUCCESS
                                            if crit == 1:
                                                if int(target_index) + 1 == len(enemies):
                                                    enemies[target_index][0] -= int(latk)/2 - 20
                                                    if len(enemies) > 1:
                                                        enemies[int(target_index)-1][0] -= int(latk)/2 - 20
                                                else:
                                                    enemies[target_index][0] -= int(latk)/2 - 20
                                                    if len(enemies) > 1:
                                                        enemies[int(target_index)+1][0] -= int(latk)/2 - 20
                                                print 'You CRIT!'
                                                print 'You did ' +str(int(latk)/2+20) +str(' damage to ') +str(target) +str(' and the enemy next to it') +str('.')
                                            #CRIT FAILURE
                                            else:
                                                if int(target_index) + 1 == len(enemies):
                                                    enemies[target_index][0] -= int(latk)/2
                                                    if len(enemies) > 1:
                                                        enemies[int(target_index)-1][0] -= int(latk)/2
                                                else:
                                                    enemies[target_index][0] -= int(latk)/2
                                                    if len(enemies) > 1:
                                                        enemies[int(target_index)+1][0] -= int(latk)/2
                                                print 'You did ' +str(int(latk)/2) +str(' damage to ') +str(target) +str(' and the enemy next to it') +str('.')
                                        else:
                                            if int(target_index) + 1 == len(enemies):
                                                enemies[target_index][0] -= int(latk)/2
                                                if len(enemies) > 1:
                                                    enemies[int(target_index)-1][0] -= int(latk)/2
                                            else:
                                                enemies[target_index][0] -= int(latk)/2
                                                if len(enemies) > 1:
                                                    enemies[int(target_index)+1][0] -= int(latk)/2
                                            print 'You did ' +str(int(latk)/2) +str(' damage to ') +str(target) +str(' and the enemy next to it') +str('.')
                                    else:
                                        enemies[target_index][0] = int(enemies[target_index][0]) - 1
                                        print 'You did 1' +str(' damage to ') +str(target) +str('.')
                                    stm += -7
                                else:
                                    print 'It dodged your attack!'
                            else:
                                print 'Not enough stamina'
                        if attack == 'ars':
                            if stm >= 7:
                                if int(hhit)+2 > int(enemies[target_index][1]):
                                    if rweapon != '':
                                        if rweapon[2] == 'flame':
                                            enemies[target_index][8] = 'flame'
                                        if rweapon[2] == 'CHICKEN':
                                            enemies[target_index][8] = 'CHICKEN'
                                        if rweapon[2] == 'crit':
                                            crit = int(random.randint(1,15))
                                            #CRIT SUCCESS
                                            if crit == 1:
                                                if int(target_index) + 1 == len(enemies):
                                                    enemies[target_index][0] -= int(ratk)/2 - 20
                                                    if len(enemies) > 1:
                                                        enemies[int(target_index)-1][0] -= int(ratk)/2 - 20
                                                else:
                                                    enemies[target_index][0] -= int(ratk)/2 - 20
                                                    if len(enemies) > 1:
                                                        enemies[int(target_index)+1][0] -= int(ratk)/2 - 20
                                                print 'You CRIT!'
                                                print 'You did ' +str(int(ratk)/2+20) +str(' damage to ') +str(target) +str(' and the enemy next to it') +str('.')
                                            #CRIT FAILURE
                                            else:
                                                if int(target_index) + 1 == len(enemies):
                                                    enemies[target_index][0] -= int(ratk)/2
                                                    if len(enemies) > 1:
                                                        enemies[int(target_index)-1][0] -= int(ratk)/2
                                                else:
                                                    enemies[target_index][0] -= int(ratk)/2
                                                    if len(enemies) > 1:
                                                        enemies[int(target_index)+1][0] -= int(ratk)/2
                                                print 'You did ' +str(int(ratk)/2) +str(' damage to ') +str(target) +str(' and the enemy next to it') +str('.')
                                        else:
                                            if int(target_index) + 1 == len(enemies):
                                                enemies[target_index][0] -= int(ratk)/2
                                                if len(enemies) > 1:
                                                    enemies[int(target_index)-1][0] -= int(ratk)/2
                                            else:
                                                enemies[target_index][0] -= int(ratk)/2
                                                if len(enemies) > 1:
                                                    enemies[int(target_index)+1][0] -= int(ratk)/2
                                            print 'You did ' +str(int(ratk)/2) +str(' damage to ') +str(target) +str(' and the enemy next to it') +str('.')
                                    else:
                                        enemies[target_index][0] = int(enemies[target_index][0]) - 1
                                        print 'You did 1' +str(' damage to ') +str(target) +str('.')
                                    stm += -7
                                else:
                                    print 'It dodged your attack!'
                            else:
                                print 'Not enough stamina'
                        
                        move = False
                            
                    else:
                        print 'Invalid attack'
                elif command not in commands:
                    print 'Invalid Command'
                
                if command == '/search':
                    if search == True:
                        search = random.randint(1,4)
                        if search + luck > size:
                            print 'You found a treasure chest!'
                            if room <= 7:
                                if room > 4:
                                    treasure = random.choice(epic)
                                    print 'You found a ' +str(treasure[0]) +str('!')
                                    if random.randint(1,4) < 4:
                                        print 'You found a potion of healing!'
                                        inv.append('potion of healing')
                                else:
                                    treasure = random.choice(rare)
                                    print 'You found a ' +str(treasure[0]) +str('!')
                                    if random.randint(1,4) < 4:
                                        print 'You found an antidote!'
                                        inv.append('antidote')
                            else:
                                treasure = random.choice(legendary)
                                print 'You found a ' +str(treasure[0]) +str('!')
                                if random.randint(1,4) < 4:
                                    print 'You found a greater potion of healing!'
                                    inv.append('greater potion of healing')
                            inv.append(treasure[0])
                        else:
                            print 'You have found nothing.'
                        search = False
                    else:
                        print 'You have already searched this room.'
                    move = False
                
                #ENEMY ATTACKS / TURN BASED EFFECTS / LEVEL UP / SHOPS
                if move == False:
                    if room > 0:
                        if enemies:
                            #STATUS EFFECTS
                            if enemies:
                                for i in range(len(enemies)):
                                    if enemies[i][6] == 'flame':
                                         enemies[i][0] -= int(random.randint(5,10))
                                         print enemies[i][8] +str(' burned.')
                                    if enemies[i][6] == 'CHICKEN':
                                        chicken = int(random.randint(1,100))
                                        if chicken == 100:
                                            enemies[i][0] = 1
                                            print '----------'
                                            print enemies[i][8] +str(' became a chicken!')
                                            print '----------'
                                    if enemies[i][6] == 'kick':
                                        remove_debuff = random.randint(1,2)
                                        if remove_debuff == 1:
                                            enemies[i][6] = ''
                                            enemies[i][1] += 5
                                    #ENEMY SPECIALS
                                    if enemies[i][9] == 'regen':
                                        if enemies[i][6] != 'flame':
                                            enemies[i][0] += int(random.randint(5,10))
                                            print 'The ' +str(enemies[i][8]) +str(' regenerated!')
                                
                            #ENEMY KILLED
                            n = len(enemies)-1
                            while n >= 0:
                                if enemies[n][0] <= 0:
                                    if enemies[n][9] == 'reincarnation':
                                        rein = random.randint(1,3)
                                        if rein == 1:
                                            enemies[n][0] = 20
                                            print 'The ' +str(enemies[n][8]) +str(' reincarnated!')
                                    if enemies[n][0] <= 0:
                                        print enemies[n][8] +str(' has been slain!')
                                        #LOOT
                                        lloot = legendary[random.randint(0,len(legendary)-1)][0]
                                        eloot = epic[random.randint(0,len(epic)-1)][0]
                                        rloot = rare[random.randint(0,len(rare)-1)][0]
                                        cloot = common[random.randint(0,len(common)-1)][0]
                                        drop = random.randint(1,10)
                                        if drop <= enemies[n][5]:
                                            inv.append(lloot)
                                            print enemies[n][8] +str(' dropped a ') +str(lloot) +str('!')
                                        else:
                                            if drop <= enemies[n][4]:
                                                inv.append(eloot)
                                                print enemies[n][8] +str(' dropped a ') +str(eloot) +str('!')
                                            else:
                                                if drop <= enemies[n][3]:
                                                    inv.append(rloot)
                                                    print enemies[n][8] +str(' dropped a ') +str(rloot) +str('!')
                                                else:
                                                    if drop <= enemies[n][2]:
                                                        inv.append(cloot)
                                                        print enemies[n][8] +str(' dropped a ') +str(cloot) +str('!')
                                        gold_looted = random.randint(1,5)
                                        gold += gold_looted
                                        print '+' +str(gold_looted) +str(' gold')
                                        
                                        #DIVIDE SPECIAL DEATHRATTLE?
                                        if enemies[n][9] == 'divide':
                                            if enemies[n][8] == 'slime':
                                                spawn = random.randint(1,2)
                                                if spawn == 1:
                                                    enemy_names.append('slime')
                                                    enemies.append([int(random.randint(1,8)),1,10,0,0,0,'','a small green slime','slime','divide'])
                                                print 'The slime divided, spawning (1) slime!'
                                            if enemies[n][8] == 'broodmother':
                                                spawn = random.randint(2,4)
                                                for i in range(spawn):
                                                    enemy_names.append('spider')
                                                    enemies.append([int(random.randint(1,10)),0,10,0,0,0,'','a black, spooky, giant spider','spider',''])
                                                print "The broodmother's eggs burst, spawning (" +str(spawn) +str(') spiders!')
                                            if enemies[n][8] == 'giant chicken':
                                                spawn = random.randint(2,4)
                                                for i in range(spawn):
                                                    enemy_names.append('chicken')
                                                    enemies.append([int(random.randint(1,6)),1,10,0,0,0,'','a chicken','chicken',''])
                                                print "The giant chicken's eggs hatched, spawning (" +str(spawn) +str(') chickens!')
                                        if enemies[n][9] == 'explode':
                                            hp += -20
                                            for i in range(n):
                                                enemies[i][0] += -15
                                            print 'The ' +str(enemies[n][8]) +str(' exploded upon death!')
                                            
                                        enemy_names.remove(enemies[n][8])
                                        enemies.remove(enemies[n])
                                n -= 1
                            
                            #ENEMY ATTACKS
                            enemy_attacks = []
                            atk_list = (('slime',int(random.randint(1,4))),('chicken',int(random.randint(1,4))),('spider',int(random.randint(1,4))),('crab',int(random.randint(1,4))),('pixie',int(random.randint(1,4))),('goblin',int(random.randint(1,6))),('warg',int(random.randint(1,6))),('zombie',int(random.randint(1,6))),('skeleton',int(random.randint(1,6))),('orc',int(random.randint(1,8))),('hobgoblin',int(random.randint(1,10))),('ghost',int(random.randint(1,6))),('troll',int(1+int(random.randint(1,8)))),('broodmother',int(2*int(random.randint(1,6)))),('ghoul',int(2*int(random.randint(1,6)))),('ogre',int(1+int(random.randint(1,8)))),('cyclop',int(1+int(random.randint(1,10)))),('griffin',int(4*int(random.randint(1,4)))),('bicorn',int(4*int(random.randint(1,4)))),('vampire',int(5*int(random.randint(1,4)))),('mummy',int(6*int(random.randint(1,4)))),('hydra',int(6*int(random.randint(1,4)))),('giant chicken',int(10)),('giant',int(3*int(random.randint(1,10)))),('fire elemental',int(1+int(4*int(random.randint(1,8))))),('titan',int(2+int(4*int(random.randint(1,8))))),('lich',int(4*int(random.randint(1,10)))),('death knight',int(4+int(3*int(random.randint(1,10))))),('demon',int(5*int(random.randint(1,10)))),('angel',int(5*int(random.randint(1,10)))),('wyvern',int(2+int(2*int(random.randint(1,20))))),('elder lich',int(6*int(random.randint(3,9)))),('dragon',int(4*int(random.randint(9,14)))),('archdemon',int(7*int(random.randint(3,6)))),('archangel',int(7*int(random.randint(3,6)))),('demigod',int(10+int(7*int(random.randint(4,7))))))
                            for i in range(len(enemies)):
                                enemy_attacks.append(enemy_names[i])
                            for i in range(len(enemies)):
                                for i in range(len(atk_list)):
                                    if atk_list[i][0] in enemy_attacks:
                                        enemy_attacks.remove(atk_list[i][0])
                                        enemy_hit = random.randint(1,20)
                                        if enemy_hit > (defe + defx):
                                            hp -= atk_list[i][1]
                                            print 'The  ' +str(atk_list[i][0]) +str(' dealt (') +str(atk_list[i][1]) +str(') to you!')
                                        else:
                                            print 'You doged the ' +str(atk_list[i][0]) +str("'s attack!")
                            
                            #STM REGEN AND MAXES
                            if stm < maxstm:
                                    stm = stm + 1 + int(stmx)
                            if stm > maxstm:
                                stm = maxstm
                            if hp > maxhp:
                                hp = maxhp
                                
                            #TEMPORARY DEBUFF REMOVAL    
                            if bash == True:
                                bash = False
                                defx += -4
                            if overhead == True:
                                overhead = False
                                defx += 2
                                
                            print 'Health: ' +str(hp) +str('/') +str(maxhp)
                            print 'Stamina: ' +str(stm) +str('/') +str(maxstm)
                            print ''
                            
                        if not enemies:
                            #LEVEL UP
                            if room > 0:
                                if levelup == False:
                                    if room == 2 or 4 or 6 or 8 or 10:
                                        hp += 20
                                        maxhp += 20
                                        strx += 2
                                    else:
                                        hp += 30
                                        maxhp += 30
                                        strx += 1
                                        stm += 2
                                        maxstm += 2
                                    if stm > maxstm:
                                        stm = maxstm
                                    if hp > maxhp:
                                        hp = maxhp
                                    print 'You have grown stronger!'
                                    print 'Health: ' +str(hp) +str('/') +str(maxhp)
                                    print 'Defense: ' +str(defe)
                                    print 'Stamina Points: ' +str(stm) +str('/') +str(maxstm)
                                    print 'Equipment: ' +str(w_armor)
                                    print 'Accessories: ' +str(w_ring)
                                    print 'Left weapon: ' +str(lweapon)
                                    print 'Right weapon: ' +str(rweapon)
                                    print 'Gold: ' +str(gold)
                                    print inv
                                    levelup = True
                            
                            #SHOP
                            if shop == True:
                                print '\n\n'
                                shop = raw_input('\n\n\nYou have encountered a merchant. Would you like to trade? [y/n] ')
                                if shop == 'n':
                                    shop = False
                                    print '\n\n'
                                else:
                                    print 'Use /sell to exchange items for gold. Use /buy to exchange gold for items. Use /exit to leave the shop.'
                                    print str(gold) +str(' gold')
                                    stock = []
                                    if room == 3:
                                        stock.append(('antidote',15))
                                    if room == 6:
                                        stock.append(('potion of healing',25))
                                    for i in range(0,3):
                                        if room == 3:
                                            stock.append(rare[random.randint(0,len(rare)-1)])
                                        if room == 6:
                                            stock.append(epic[random.randint(0,len(epic)-1)])
                                        if room == 9:
                                            stock.append(legendary[random.randint(0,len(legendary)-1)])
                                    print 'Stock: '
                                    for i in range(len(stock)):
                                        print '     ' +str(stock[i][0]) +str(', ') +str(stock[i][1]) +str(' gold')
                                    action = ''
                                    while action != '/exit':
                                        action = raw_input('What would you like to do? ')
                                        print ''
                                        if action == '/sell' or '/buy':
                                            if action == '/sell':
                                                print inv
                                                sell = raw_input('What would you lik