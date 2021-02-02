#!/usr/bin/python
import sys
import os
import json
import random
random.seed()

class Restaurants:
    def __init__(self, filename):
        self.filename = filename
        if os.path.exists(self.filename):
            file = open(self.filename, "r")
        else:
            file = open(self.filename, "x")
        try:
            self.restaurants = json.loads(file.read())
        except:
            self.restaurants = {}
        file.close()

    def save(self):
        file = open(self.filename, "w")
        file.write(json.dumps(self.restaurants, sort_keys=True, indent=4, separators=(',', ': ')))
        file.close()

    def add(self, name):
        new_weight = 1
        found = False
        for r in self.restaurants:
            if r == name:
                print(name + " already in the list")
                found = True
                break
            if self.restaurants[r] > new_weight:
                new_weight = r[0]
        if not found:
            self.restaurants[name] = new_weight
            print(name + " added to the list")

    def remove(self, name):
        found = False
        for r in self.restaurants:
            if r == name:
                del(self.restaurants[r])
                print(name + " removed from the list")
                found = True
                break
        if not found:
            print(name + " is not in the list")

    def pick(self):
        bag = []
        for r in self.restaurants:
            for _ in range(self.restaurants[r]):
                bag.append(r)
        p = bag[random.randrange(len(bag))]
        for r in self.restaurants:
            if p != r:
                self.restaurants[r] += 1
        self.restaurants[p] = 1
        print(p + " is picked")

    def reset(self):
        for r in self.restaurants:
            self.restaurants[r] = 1
        print("list reseted")
        self.list();

    def list(self):
        print(str(len(self.restaurants)) + " restaurants in the list")
        for r in self.restaurants:
            print("{0:20s} {1:2d}".format(r, self.restaurants[r]))
        

if __name__ == "__main__":
    restaurants = Restaurants("restaurants.json")
    if sys.argv[1] == "add":
        restaurants.add(sys.argv[2])
    elif sys.argv[1] == "remove":
        restaurants.remove(sys.argv[2])
    elif sys.argv[1] == "pick":
        restaurants.pick()
    elif sys.argv[1] == "list":
        restaurants.list()
    elif sys.argv[1] == "reset":
        restaurants.reset()
    restaurants.save()
