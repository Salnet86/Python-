
import os
import subprocess
import subprocess 
  
'''
devices = subprocess.check_output(['netsh','wlan','show','network']) 
  

devices = devices.decode('ascii') 
devices= devices.replace("\r","") 
  

print(devices)
'' '


#subprocess.run(["sudo", "pacman", "-Syu"])



Il modulo subprocess supporta tre API per lavorare con processi. La funzione run(),
aggiunta in Python 3.5 è una 
API ad alto livello per eseguire 
un processo con opzione per 
catturare il suo output. 
Le funzioni call(), check_call(), e check_output() sono tre precedenti API di alto livello, portate dalla versione 2 di Python. Esse sono ancora supportate e largamente usate in programmi esistenti. La classe Popen è una API di basso livello usata per costruire le altre API e utile per interazioni di processo più complesse. Il costruttore per Popen riceve argomenti 
per impostare il nuovo processo in modo che il genitore
possa comunicare con esso tramite pipe. Fornisce tutte
le funzionalità degli altri moduli e funzioni che rimpiazza, e altro ancora. L'API è consistente per tutti gli utilizzi, e molti dei passi supplementari necessari (tipo la chiusura di descrittori di file extra e l'assicurare che le pipe siano chiuse) sono "incorporate" invece che essere gestite dal codice dell'applicazione separatamente.

Il modulo subprocess è concepito per sostituire funzioni tipo os.system(), os.spawn(), le varianti di popen() nei moduli os e popen2, così come il modulo commands. Per facilitare il confronto di subprocess con questi altri moduli, molti degli esempi di questa sezione ricreano quelli usati per os e popen2.

L'API per lavorare con Unix e Windows è grossomodo la stessa, ma l'implementazione sottostante è leggermente diversa a causa della differenza nei modelli di processo nei sistemi operativi. Tutti gli esempi qui mostrati sono testati su MAC Os X. L'esperienza personale in un sistema operativo diverso da Unix potrebbe essere diversa.
Eseguire un Comando Esterno
Per eseguire un comando esterno senza interagire con esso, proprio come si farebbe con os.system(), si usa la funzione run().





#completed = subprocess.run(['ls', '-1'])
#print('returncode:', completed.return



addizionali

Il modulo subprocess supporta tre API per lavorare con processi. La funzione run(), aggiunta in Python 3.5 è una API ad alto livello per eseguire un processo con opzione per catturare il suo output. Le funzioni call(), check_call(), e check_output() sono tre precedenti API di alto livello, portate dalla versione 2 di Python. Esse sono ancora supportate e largamente usate in programmi esistenti. La classe Popen è una API di basso livello usata per costruire le altre API e utile per interazioni di processo più complesse. Il costruttore per Popen riceve argomenti per impostare il nuovo processo in modo che il genitore possa comunicare con esso tramite pipe. Fornisce tutte le funzionalità degli altri moduli e funzioni che rimpiazza, e altro ancora. L'API è consistente per tutti gli utilizzi, e molti dei passi supplementari necessari (tipo la chiusura di descrittori di file extra e l'assicurare che le pipe siano chiuse) sono "incorporate" invece che essere gestite dal codice dell'applicazione separatamente.

Il modulo subprocess è concepito per sostituire funzioni tipo os.system(), os.spawn(), le varianti di popen() nei moduli os e popen2, così come il modulo commands. Per facilitare il confronto di subprocess con questi altri moduli, molti degli esempi di questa sezione ricreano quelli usati per os e popen2.

L'API per lavorare con Unix e Windows è grossomodo la stessa, ma l'implementazione sottostante è leggermente diversa a causa della differenza nei modelli di processo nei sistemi operativi. Tutti gli esempi qui mostrati sono testati su MAC Os X. L'esperienza personale in un sistema operativo diverso da Unix potrebbe essere diversa.
Eseguire un Comando Esterno
Per eseguire un comando esterno senza interagire con esso, proprio come si farebbe con os.system(), si usa la funzione run().

# 

import subprocess

completed = subprocess.run(['ls', '-1'])
print('returncode:', completed.returncode)
Gli argomenti di riga di comando sono passati come lista di stringhe, che consente di evitare l'escape di apici o altri caratteri speciali che potrebbero essere interpretati dalla shell. run() ritorna una istanza di CompletedProcess con informazioni circa il processo tipo il codice di uscita e l'output



import subprocess

completed = subprocess.run('echo $HOME', shell=True)
print('returncode:', completed.returncode)




