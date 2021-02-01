#!/usr/bin/python
import sys
import os
import json
import random
random.seed()

class Resturants:
    def __init__(self, filename):
        self.filename = filename
        if os.path.exists(self.filename):
            file = open(self.filename, "r")
        else:
            file = open(self.filename, "x")
        try:
            self.resturants = json.loads(file.read())
        except:
            self.resturants = {}
        file.close()

    def save(self):
        file = open(self.filename, "w")
        file.write(json.dumps(self.resturants, sort_keys=True, indent=4, separators=(',', ': ')))
        file.close()

    def add(self, name):
        new_weight = 1
        found = False
        for r in self.resturants:
            if r == name:
                print(name + " already in the list")
                found = True
                break
            if self.resturants[r] > new_weight:
                new_weight = r[0]
        if not found:
            self.resturants[name] = new_weight
            print(name + " added to the list")

    def remove(self, name):
        found = False
        for r in self.resturants:
            if r == name:
                del(self.resturants[r])
                print(name + " removed from the list")
                found = True
                break
        if not found:
            print(name + " is not in the list")

    def pick(self):
        bag = []
        for r in self.resturants:
            for _ in range(self.resturants[r]):
                bag.append(r)
        p = bag[random.randrange(len(bag))]
        for r in self.resturants:
            if p != r:
                self.resturants[r] += 1
        self.resturants[p] = 1
        print(p + " is picked")

    def reset(self):
        for r in self.resturants:
            self.resturants[r] = 1
        print("list reseted")
        self.list();

    def list(self):
        print(str(len(self.resturants)) + " resturants in the list")
        for r in self.resturants:
            print("{0:20s} {1:2d}".format(r, self.resturants[r]))
        

if __name__ == "__main__":
    resturants = Resturants("resturants.json")
    if sys.argv[1] == "add":
        resturants.add(sys.argv[2])
    elif sys.argv[1] == "remove":
        resturants.remove(sys.argv[2])
    elif sys.argv[1] == "pick":
        resturants.pick()
    elif sys.argv[1] == "list":
        resturants.list()
    elif sys.argv[1] == "reset":
        resturants.reset()
    resturants.save()
