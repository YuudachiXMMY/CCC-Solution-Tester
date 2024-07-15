# !/usr/local/bin/python
# -*- coding: utf-8 -*-
import CCCs_test

def is_alternating_heavy_light(s):
    # Step 1: Count the frequency of each letter
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Step 2: Determine whether each letter is heavy or light
    heaviness = []
    for char in s:
        if freq[char] > 1:
            heaviness.append('H')  # Heavy
        else:
            heaviness.append('L')  # Light

    # Step 3: Check if the string alternates between heavy and light
    for i in range(1, len(heaviness)):
        if heaviness[i] == heaviness[i - 1]:
            return False
    return True

def solution():
    T, N = map(int, input().split())

    for i in range(T):
        s  = input()
        if is_alternating_heavy_light(s):
            print("T")
        else:
            print("F")

def run():
    solution()

if __name__ == '__main__':
    run()
    # CCCs_test.test("s2")