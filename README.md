# Datathon24

Aquest és el projecte del grup lliurament2.sh per la activitat Datathon 2024 repte 3 (Caronte).

## Membres de l'equip

1. Gerard Puig Ortega (1er Enginyeria informàtica, grup 41)
2. Giuseppe Vega Cieza (1er Enginyeria informàtica, grup 41)
3. Jordi Roman Martin (1er Enginyeria informàtica, grup 41)
4. Joel Castillo Nieto (1er Enginyeria informàtica, grup 41)

## Projecte

El projecte escollit és el del Caronte, fer una proposta que satisfaci els següents objectius:
- Model de predicció de notes finals.
- Recomanador d'activitats de reforç.
- Marcador de projecció de rendiment acadèmic.
- Anàlisi de patrons d'estudi i rendiment.
- Desenvolupar visualitzacions de l'evolució acadèmica

### Objectius del grup

Som un grup format per dos estudiants provinents de cicle fomratiu de grau superior, administració de sistemes en xarxa, i dos estudiants de batxillerat de ciencies/tecnologia. El nostre objectiu principal no és competir, sinó aprendre de l'experència, tenir les nostres primeres aproximacions amb temes que no coneixem, i així, aprendre noves coses. 

Encara que no acabem una solució convincent, el nostre aprenentatge és aprendre a treballar en equip, espabilar-nos i veure com funciona una mica el big data.

### Planing

Per començar, hem planificat com seria un script que pogués solucionar el primer objectiu, fer un model de predicció de notes finals. Una vegada dissenyat aquest algorisme com funcionaria, només s'hauria de modificar i adaptar-ho per les demés solucions, per exemple, si aconseguim un model de prediccions, significa que sabem quins valors i paràmetres afecten al resultat de manera positiva i negativament, per  tant, amb aquestes variables es pot recomanar activitats per reforç.

## Elaboració del projecte

Hem fet servir el programa Microsoft Power Bi per representar la informació dels 3 arxius CSV, i interpretar-los. Això ja que degut a l'experiència nul·la amb machine learning, la nostra solució serà interpretar les dades, i fer una funció matemàtica a la que poguem posar dades i fer una predicció molt idealista, ja que hi ha molts detalls que poden influir al resultat i no els tenim en compte ja que ho complicaria tot.

A continuació algunes gràfiques que hem fet per analitzar les dades:
![Mitjana de nota](https://github.com/Joel-Castillo-Nieto/Hackathron24/blob/main/img/mitjana.png)
![Mitjana de nota classificat per assignatura(aula)](https://github.com/Joel-Castillo-Nieto/Hackathron24/blob/main/img/media%20de%20nota%20final%20por%20assignaturas.png)

Per fer la fòrmula, hem fet servir ChatGpt que ens ha fet un codi que ens retorna uns coeficients de com afecten alguns valors a les notes parcials/finals/recuperacions, i seguidament muntem una fòrmula amb aquests coeficients.

La fòrmula que ens interesa és una regresió lineal multiple(o multivariable).
Una regresió lineal múltiple és un model de regresió que inclou dues o més variables independents. Básicament és un model estadístic que permet relacionar múltiples variables explicatives amb una variable resposta de manera lineal, un exèmple de regresió lineal multiple:
![Exemple de regressió lineal multivariable](https://d20ohkaloyme4g.cloudfront.net/img/document_thumbnails/66f57d6438f24d6f2e85bd4ed542516e/thumb_1200_900.png)

Una vegada creada la fòrmula, nosaltres disenyem la solució:

## Creació de la solució

Per començar, hem de pensar com podem rebre la informació, i hem pensat en tres propostes:
1. Pàgina web amb CRUD.
2. Una API oberta.
3. Llibreria.

La pàgina web l'hem descartat ja que segurament seria una pàgina web externa al Caronte i això dificultaria l'entrada d'informació, habent d'iniciar sessió un altre cop, entre d'altes dificultats que ens podria causar.

Una API oberta podria ser una opció interesant, ja que d'aquesta manera, el caronte només hauria de fer una ruta al servidor, i que treballi en els càlculs. EL problema principal és que ningú del grup ha treballat amb APIs, no he treballat tampoc amb CORS, i això seria ja una dificultat mig-alta d'entrada per començar a crear el projecte, i per tant l'hem descartat per aquesta mateixa raó.

Finalment, hem pensat en una llibreria, de manera que sigui portable, i que es pugui fer servir al Caronte, i també de múltiples maneres. L'única dificultat seria crear una documentació, i fer-ho de manera portable el codi. Finalment, aquesta opció va ser la que menys problemes ens aportaba, així que hem escollit aquesta.

## SISTEMA DE RECOMANACIONS DE PATRONS D'ESTUDIS I RENDIMENT 

Aquesta proposta és un primer pas cap al desenvolupament d’un sistema de recomanacions de patrons d’estudi per a estudiants tant d’un baix rendiment acadèmic com d’alt. Cal subratllar que a causa de les nostres limitacions actuals en coneixements i experiència en aquest tipus de sistemes estem com en una fase preliminar. La idea principal és assentar les bases perquè aquest projecte quedi obert a l’evolució i una millora contínua en el futur.  

Anàlisi d’activitats i filtració d’activitats recomanades: 
Aquesta proposta està dividit en diferents fases. La primera seria identificar als estudiants que tenen un rendiment per sota o per dalt de les qualificacions finals i parcials. 
Segons el promig de qualificacions i el nombre d’intents de les activitats, el programa analitzaria un patró d’estudi. Les recomanacions es basarien segons alguns factors : 
-	Activitats d’alt rendiment: Es recomanen activitats amb una mitjana de qualificacions superior a un llindar, cosa que indica que han estat efectives per a altres estudiants.
-	Activitats amb un baix nombre d’intents: aquest tipus d’activitats es podrien excloure com a recomanacions perquè indiquen que no són molt difícils i no serien tan efectives per millorar. 

Personalització recomanacions i futures millores: 
Les recomanacions hauran de ser personalitzades, tenint en compte les àrees específiques de cada estudiant on mostren més dificultats. 
Les futures millores per dur a terme aquesta proposta seria mitjançant la implementació d’algoritmes de machine learning per exemple per tal de fer un sistema de recomanacions més robust. 

