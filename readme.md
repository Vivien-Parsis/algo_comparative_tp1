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

## resultat benchmark
