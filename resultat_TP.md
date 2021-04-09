#### TP de performance: On a réalisé les test de performance avec deux fichiers un de 32.7 MB (32,677,698 bytes) pour le mode slow du server et un autre de 183.5 MB (183,456,778 bytes) pour le mode fast

## Un client et un serveur

# 1- Prise en main du serveur et du client
Après execution du server et du client nous avons les performance ci-après

- Execution de la version lente du server et du client
Un long temps d'execution est noté pour un time de plus de 1200.
Lors de l'execution de la version lente du server et du client, on constacte déjà qu'au niveau du server que le temps d'envoi est très important.
Après un time de 500, le débit reste constant jusqu'à la fin et y'a que les logs de reception.
Côté client, nous avons les deux logs: reception et envoi. Lors de l'envoi, le débit le plus de 0.064 et reste constant jusqu'à la fin de l'execution.
A la reception, le débit au niveau du client est moins de 0.05 et reste constant jusqu'à la fin de l'execution.
On peut conclure que les performance du reseau sont plus sollicité lors de l'envoi au niveau du client.

- Execution de la version rapide du server et du client
Un temps d'execution relativement plus court est noté avec un time de plus de 14 côté client.
Lors de l'execution de la version rapide du server et du client, on constacte au niveau du server qu'il n'y a pas les logs de reception et d'envoi.
Côté client, nous avons uniquement les logs de d'envoi. On constacte que le débit est très elevé soit de plus de 11 relativement à la version lente du server qui était moins de 0,1. Continuant dans cet efficacité, nous avons un traitement environ 50 fois plus rapide que la version lente u server.
Le debit d'envoi au niveau du client reste plutôt constant jusqu'à la fin de l'execution.

# Version rapide uniquement
# 2- Variation du délai

Après variation du delai, nons constactons que, déjà on est présence de la version rapide du server et du client donc un débit très elevé, puis avec un delai de 20 le temps de traitement avoisine les 20 et lorsqu'on passe à des delai de 30-40-50 jusqu'a 100, le débit est très constant et le temps de traitement est moins de 17.
Plus le delai est elevé plus le débit du réseau est très constant.

# 3- Vartiation du taux de pertes

Après variation du taux de pertes, nons constactons qu'a 0,1%, malgré qu'on soit dans la version rapide du server et du client, le temps de traitement à augmenter et on constacte que le débit est instable. Au début il était à près de 12 puis chuter à moins de la moitié dans un premier temps et descendre à 4.
A 2% de taux de perte, on note un temps de traitement plus long soit 10 fois plus long que lorsque le taux de perte était à 0,1%. La débit reste toujours instanble mais très faible en dessous de 1.
Le taux de perte joue enormément sur le débit et le temps de traitement dans le réseau.
Plus le taux de perte est elevé plus le temps de traitement est long et moins le débit est.

# 4- Variation du jitter

Lorsqu'on fait varié le jitter de 0,1% à 2%, le temps de traitement est rapide, le débit avoisine 12 sauf que lorsque le jitter est à 2% le débit est instanble mais reste dans la fourchette de 11,75 et 12.

## Plusieurs clients et un seul serveur (execution manuelle)
# 1- Prise en main du serveur et du client
Exécuter la version rapide et la version lente du client et du serveur. 
Tracer dans chaque cas les graphes des  fichiers de log de réception et des 
fichier de log d’envois. Interprèter et commenter les différence de performance.
Prendre les valeurs `delay=10`, `bw=100`, `loss_rate=0%` et `jitter=0%`

Après execution du server et du client nous avons les performance ci-après

- Execution de la version lente du server et du client

- Execution de la version rapide du server et du client

# 2- Variation du délai
Faire varier le délai d'un pas de 10 jusqu'à 100 et excécuter le serveur et le
client. Commenter les graphes obtenus à partir des fichiers de logs.

# 3- Vartiation du taux de pertes
Faire varier le taux de perte d'un pas de `0.1%` à `2%`. Commenter les graphes.

# 4- Variation du jitter
Faire varier le jitter d'un pas de `0.1%` à `2%`. Commenter les graphes.



## All in one

Automatiser tout cela dans le script python `gbeffasarl.py` de façon qu'à laide 
de la commande suivante il soit possible de générer les tests et les graphes
pour cahque cas.

```
 $ sudo python3 gbeffasarl.py <delay> <bw> <loss_rate> <jitter> 
```