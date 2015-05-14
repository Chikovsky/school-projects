print ('Welcome to the scientologist name generator')
print ('==========================================================')
import random
repeat=1
while repeat>=1:
    term1=['klip','garg','iorn','keh','lol','harf','weor','bul','erik','yuorf',
          'hewlon','juhr','aoequ','tom','neor','hedlert','ekpitu','jon','nerlo',
          'husdo','ther','geonbord','mork','mort']
    term2=['werryo','boody','hui','muoi','pohf','star','yoin','lorf','jor',
          'haf','mohte','bop','kor','nerp','hio','ior','sday','fuioe','no',
          'joir','nuiea','resa','hfio','fjio']
    term3=['tnes','suio','ni','rump','bump','nudi','nioo','njarse','bui',
          'quiol','niop','niesg','whw','yhi','mokfe','sre','ewr','oiy',
          'nuir','hui','keo','moae','dio','ashui']
    first=random.choice(term1)
    second=random.choice(term2)
    third=random.choice(term3)
    print ('Your new name is', first, second, third)
    print ('===============================================================================')
    again=input ('Do you wish for a new name?')
    if again=='yes':
        repeat+=1
    else:
        print ('Welcome brother')
