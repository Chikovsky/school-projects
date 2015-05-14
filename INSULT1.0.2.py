import random
f = open('Insult.txt','w')
repeat=1
while repeat>=1:
    term1=['artless','bawdy','beslubbering','bootless','churlish','cockered',
       'clouted','craven','currish','dankish','dissembling','droning','errant',
       'fawning','fobbing','froward','frothy','gleeking','goatish','gorbellied',
       'impertint','infectious','jarring','loggerheaded','lumpish','mammering',
       'mangled','mewling','paunchy','pribbling','puking','puny','qualling',
       'rank','reeky','roguish','ruttish','saucy','spleeny','spongy','surly',
       'tottering','unmuzzled','vain','venomed','villainous','warped','wayward',
       'weedy','yeasty']
    term2=['base-court','bat-fowling','beef-witted','beetle-headed','boil-brained',
       'clapper-clawed','clay-brained','common-kissing','crook-pated','dismal-dreaming',
       'dizzy-eyed','doghearted','dread-bolted','earth-vexing','elf-skinned',
       'fat-kidneyed','fen-sucked','flap-mouthed','fly-bitten','folly-fallen','fool-born',
       'full-gorged','guts-griping','half-faced','hasty-witted','hedge-born','hell-hated',
       'idle-headed','ill-breeding','ill-nurtured','knotty-pated','milk-livered',
       'motley-minded','onion-eyed','plume-plucked','pottle-deep','pox-marked','reeling-ripe',
       'rough-hewn','rude-growning','rump-fed','shard-born','sheep-biting','spur-galled',
       'swag-bellied','tardy-gaited','tardy-gaited','tickle-brained','toad-spotted','urchin-snouted',
       'weather-bitten']
    term3=['apple-john','baggage','barnacle','bladder','boar-pig','bugbear','bum-belly','cancker-blossom',
       'clack-dish','clotpole','coxcomb','codpiece','death-token','dewberry','flap-dragon','flax-wench',
       'flirt-gill','foot-licker','fustilarian','giglet','gudgeon','harrard','harpy','hedge-pig',
       'horn-beast','hugger-mugger','joithead','lewdster','lout','maggot-pie','malt-worm','mammet',
       'measle','minnow','micreant','moldwarp','mumble-news','nut-hook','pigeon-egg','pignut',
       'puttock','pumpion','ratsbane','scut','skainsmate','strumpet','varlot','vassal','whey-face','wagtail']
    term4=['Thou art nothing but a','Thou ist','thou art a']
    first=random.choice(term1)
    second=random.choice(term2)
    third=random.choice(term3)
    statement=random.choice(term4)
    output = '%s %s %s %s' %(statement, first, second, third)
    print (output)
    f.write(output + '\n')
    print('===============================================================================')
    again=input ('Does thine wish for thou feelings to be demolished again?')
    
    if again=='yes':
        repeat+=1
    else:
        input('What, too much for your dainty flower girl heart?!')
        repeat=0
f.close()

