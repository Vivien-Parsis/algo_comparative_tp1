# Mini TP Data Structure

## Complexité théorique

| opération        | Dynamic array | Linked list | Hash Table | Gagnant prévu |
|------------------|---------------|-------------|------------|---------------|
| get(index)       | O(1)          | O(n)        |            | Dynamic array |
| find(value)      | O(n)          | O(n)        | O(n)       | Hash Table    |
| insert_front     | O(n)          | O(1)        |            | Linked list   |
| insert_back      | O(1)          | O(n)        |            | Dynamic array |
| remove_front     | O(n)          | O(1)        |            | Linked list   |
| parcours complet | O(n)          | O(n)        | O(n)       | Dynamic array |

## Prediction avant benchmark

### accès à l'élément n/2

Selon moi, le dynamic array est le plus rapide pour effectuer cette opération que linked list vu leur complexité temporel.

### recherche d'une valeurs absente

Selon moi le plus rapide est dynamic array, suivi du linked list et enfin du hash table.

### insertion en début

Selon moi le linked list est le plus rapide que le dynamic array vu leur complexité temporel.

### insertion en fin

selon moi le dynamic array est le plus rapide que le linked list vu leur complexité temporel.

### parcours avec somme

Selon moi le plus rapide est dynamic array, suivi du linked list et enfin du hash table.

## resultat console benchmark

```none
taille 1000
occurence de test 10

temps moyen pour accès à l'élément n/2
---
linked_list : 2.3698806762695314e-05
dynamic_array : 3.814697265625e-07

temps moyen pour recherche d'un élément absent
---
linked_list : 3.726482391357422e-05
dynamic_array : 3.983974456787109e-05
hash_table : 5.483627319335937e-07

temps moyen pour faire la somme des éléments
---
linked_list : 4.510879516601562e-05
dynamic_array : 4.596710205078125e-05
hash_table : 0.0002534151077270508

temps moyen pour insertion en début
---
linked_list : 1.1920928955078125e-06
dynamic_array : 5.7363510131835936e-05

temps moyen pour insertion en fin
---
linked_list : 2.3102760314941408e-05
dynamic_array : 3.337860107421875e-07
==========
==========

taille 10000
occurence de test 10

temps moyen pour accès à l'élément n/2
---
linked_list : 0.00023202896118164064
dynamic_array : 3.337860107421875e-07

temps moyen pour recherche d'un élément absent
---
linked_list : 0.0003160715103149414
dynamic_array : 0.00033957958221435546
hash_table : 7.152557373046875e-07

temps moyen pour faire la somme des éléments
---
linked_list : 0.00034372806549072267
dynamic_array : 0.00039734840393066404
hash_table : 0.000527191162109375

temps moyen pour insertion en début
---
linked_list : 1.2636184692382812e-06
dynamic_array : 0.0004917860031127929

temps moyen pour insertion en fin
---
linked_list : 0.00023865699768066406
dynamic_array : 5.245208740234375e-07
==========
==========

taille 100000
occurence de test 10

temps moyen pour accès à l'élément n/2
---
linked_list : 0.0019630670547485353
dynamic_array : 1.33514404296875e-06

temps moyen pour recherche d'un élément absent
---
linked_list : 0.0029705524444580077
dynamic_array : 0.003194379806518555
hash_table : 2.2411346435546876e-06

temps moyen pour faire la somme des éléments
---
linked_list : 0.003944706916809082
dynamic_array : 0.00414888858795166
hash_table : 0.0037524938583374024

temps moyen pour insertion en début
---
linked_list : 3.7670135498046877e-06
dynamic_array : 0.004240942001342773

temps moyen pour insertion en fin
---
linked_list : 0.0021629095077514648
dynamic_array : 1.0728836059570312e-06
==========
==========

taille 1000000
occurence de test 10

temps moyen pour accès à l'élément n/2
---
linked_list : 0.019638609886169434
dynamic_array : 2.4318695068359373e-06

temps moyen pour recherche d'un élément absent
---
linked_list : 0.028326034545898438
dynamic_array : 0.0306427001953125
hash_table : 2.932548522949219e-06

temps moyen pour faire la somme des éléments
---
linked_list : 0.03230814933776856
dynamic_array : 0.03501348495483399
hash_table : 0.032085299491882324

temps moyen pour insertion en début
---
linked_list : 4.363059997558594e-06
dynamic_array : 0.04034116268157959

temps moyen pour insertion en fin
---
linked_list : 0.018842625617980956
dynamic_array : 1.5974044799804688e-06
==========
==========
```

## Recommendation finale

### Solution A

Mon choix portera sur le hash table. La recherche sur la collection est importante mais rarement modifier, la performance sur la recherche prime, malgré le fait qu'elle est plus couteuse en construction et plus difficile a implementé que les autre.
