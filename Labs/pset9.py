# Name:         Jillian Quinn
# Course:       CPE 101
# Instructor:   Kauffman
# Assignment:   Problem Set 9
# Term:         Winter 2019


def bubble_pass(List):
    for i in range(1, len(List)):
        if List[i] < List[i - 1]:
            temp = List[i]
            List[i] = List[i - 1]
            List[i - 1] = temp
    return List


def bubble_sort(List):
    for i in List:
        bubble_pass(List)


def selection_pass(List, start):
    if start < len(List):
        smallest = start
        for j in range(start, len(List)):
            if List[smallest] > List[j]:
                smallest = j
        temp = List[start]
        List[start] = List[smallest]
        List[smallest] = temp
    return List


def selection_sort(List):
    for i in range(len(List)):
        selection_pass(List, i)


def insertion_pass(List, start):
    if start < len(List):
        value = List[start]    
        while start > 0 and List[start - 1] > value:
            List[start] = List[start - 1]
            start = start - 1
        List[start] = value
    return List


def insertion_sort(List):
    for i in range(1, len(List)):
        insertion_pass(List, i)


def binary_search(List, n):
    low = 0
    high = len(List) - 1
    while low <= high:
        mid = (low + high) // 2
        if List[mid] == n:
            return mid
        if List[mid] > n:
            high = mid - 1
        if List[mid] < n:
            low = mid + 1
    return -1



