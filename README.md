# Datathon24

Aquest és el projecte del grup lliurament2.sh per la activitat Datathon 2024 repte 3 (Caronte).

## Membres del equip

1. Gerard Puig Ortega (1er Enginyeria informàtica, grup 41)
2. Giuseppe Vega Cieza (1er Enginyeria informàtica, grup 41)
3. Jordi Roman Martin (1er Enginyeria informàtica, grup 41)
4. Joel Castillo Nieto (1er Enginyeria informàtica, grup 41)

## Projecte

El projecte escollit és el del Caronte, fer una proposta que satisfà els següents objectius:
- Model de predicció de notes finals.
- Recomanador d'activitats de reforç.
- Marcador de projecció de rendiment acadèmic.
- Anàlisi de patrons d'estudi i rendiment.
- Desenvolupar visualitzacions de l'evolució acadèmica

### Objectius del grup

Som un grup format per dos estudiants provinents de cicle fomratiu de grau superior, administració de sistemes en xarxa, i dos estudiants de batxillerat de ciencies/tecnològic. El nostre objectiu principal no és competir, sinó aprendre de la experència, tenir les nostres primeres aproximacions amb temes que no coneixem, i així, aprendre noves coses. 

Encara que no acabem una solució convincent, la nostra experiencia és aprendre a treballar en equip, espabilar-nos i veure com funciona una mica el big data.

### Planing

Per començar, hem planificat com seria un script que pogués solucionar el primer objectiu, fer un model de predicció de notes finals. Una vegada dissenyat aquest algorisme com funcionaria, només s'hauria de modificar i adaptar-ho per les demés solucions, per exemple, si aconseguim un model de prediccions, significa que sabem quins valors i paràmetres afecten al resultat de manera positiva i negativament, per  tant, amb aquestes variables es pot recomanar activitats per reforç.

## Elaboració del projecte

Hem fet servir Power Bi per representar la informació dels 3 CSV, i interpretar-los, ja que degut a l'experiencia nul·la amb machine learning, la nostra solució serà interpretar les dades, i fer una funció matemàtica que puguem posar dades i fer una predicció molt idealista, ja que hi han molts detalls que poden influir al resultat i no els tenim en compte ja que ho complicaria tot.

Per fer la fòrmula, hem fet servir ChatGpt que ens ha fet un codi que ens retorna uns coeficients de com afecten alguns valors a les notes parcials/finals/recuperacions, i seguidament muntem una fòrmula amb aquests coeficients.

Una vegada creada la fòrmula, nosaltres disenyem la solució:

## Creació de la solució

