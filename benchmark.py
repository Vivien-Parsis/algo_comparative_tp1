import time
from dynamicArray import DynamicArray
from hashTable import HashTable
from linkedList import LinkedList

def create_test_sample_dynamicArray(size):
    sample = DynamicArray()
    for i in range(size):
        sample.insert_back(1)
    return sample

def create_test_sample_hashTable(size):
    sample = HashTable()
    for i in range(size):
        sample.hash_insert(1)
    return sample

def create_test_sample_linkedList(size):
    sample = LinkedList()
    for i in range(size):
        sample.insert_front(1)
    return sample

def test(size, occurence_test):
    linkedList = create_test_sample_linkedList(size)
    hashTable = create_test_sample_hashTable(size)
    dynamicArray = create_test_sample_dynamicArray(size)

    time_test_linked_list_half = []
    time_test_dynamic_array_half = []

    time_test_linked_list_absent = []
    time_test_dynamic_array_absent = []
    time_test_hash_table_absent = []

    time_test_linked_list_sum = []
    time_test_dynamic_array_sum = []
    time_test_hash_table_sum = []
    
    time_test_linked_list_front = []
    time_test_dynamic_array_front = []

    time_test_linked_list_back = []
    time_test_dynamic_array_back = []
    for x in range(occurence_test):
        #half
        start = time.time()
        linkedList.get(size//2)
        end = time.time()
        time_test_linked_list_half.append(end-start)

        start = time.time()
        dynamicArray.get(size//2)
        end = time.time()
        time_test_dynamic_array_half.append(end-start)

        #absent
        start = time.time()
        linkedList.find(1000)
        end = time.time()
        time_test_linked_list_absent.append(end-start)

        start = time.time()
        dynamicArray.find(1000)
        end = time.time()
        time_test_dynamic_array_absent.append(end-start)

        start = time.time()
        hashTable.hash_contains(1000)
        end = time.time()
        time_test_hash_table_absent.append(end-start)

        #sum
        total = 0
        start = time.time()
        for i in range(dynamicArray.size):
            total += dynamicArray.data[i]
        end = time.time()
        time_test_dynamic_array_sum.append(end-start)

        total = 0
        start = time.time()
        current = linkedList.head
        while current is not None:
            total += current.value
            current = current.next
        end = time.time()
        time_test_linked_list_sum.append(end-start)

        total = 0
        start = time.time()
        for bucket in hashTable.buckets:
            current = bucket
            while current is not None:
                total += current.value
                current = current.next
        end = time.time()
        time_test_hash_table_sum.append(end-start)

        #insert front
        start = time.time()
        linkedList.insert_front(20)
        end = time.time()
        time_test_linked_list_front.append(end-start)

        start = time.time()
        dynamicArray.insert_front(20)
        end = time.time()
        time_test_dynamic_array_front.append(end-start)

        #insert back
        start = time.time()
        linkedList.insert_back(20)
        end = time.time()
        time_test_linked_list_back.append(end-start)

        start = time.time()
        dynamicArray.insert_back(20)
        end = time.time()
        time_test_dynamic_array_back.append(end-start)

        #resultat
    print(f"taille {size}")
    print(f"occurence de test {occurence_test}")

    print("temps moyen pour accès à l'élément n/2\n---")
    print(f"linked_list : {sum(time_test_linked_list_half)/occurence_test}")
    print(f"dynamic_array : {sum(time_test_dynamic_array_half)/occurence_test}")

    print("\ntemps moyen pour recherche d'un élément absent\n---")
    print(f"linked_list : {sum(time_test_linked_list_absent)/occurence_test}")
    print(f"dynamic_array : {sum(time_test_dynamic_array_absent)/occurence_test}")
    print(f"hash_table : {sum(time_test_hash_table_absent)/occurence_test}")

    print("\ntemps moyen pour faire la somme des éléments\n---")
    print(f"linked_list : {sum(time_test_linked_list_sum)/occurence_test}")
    print(f"dynamic_array : {sum(time_test_dynamic_array_sum)/occurence_test}")
    print(f"hash_table : {sum(time_test_hash_table_sum)/occurence_test}")

    print("\ntemps moyen pour insertion en début\n---")
    print(f"linked_list : {sum(time_test_linked_list_front)/occurence_test}")
    print(f"dynamic_array : {sum(time_test_dynamic_array_front)/occurence_test}")

    print("\ntemps moyen pour insertion en fin\n---")
    print(f"linked_list : {sum(time_test_linked_list_back)/occurence_test}")
    print(f"dynamic_array : {sum(time_test_dynamic_array_back)/occurence_test}")

def main():
    test(1000,10)
    test(10000,10)
    test(100000,10)
    test(1000000,10)



main()