import numpy as np
import random
import copy


class LA:
    last_action = 0
    lambda1 = 0
    lambda2 = 0
    pvector = np.array(0)
    r = 0
    ptempt = np.array(0)
    nvector = np.array(0)
    zvector = np.arange(0)
    dvector = np.array(0)

    def __init__(self, r, lambda1, lambda2):
        self.r = r
        self.lambda1 = lambda1
        self.lambda2 = lambda2
        self.pvector = np.zeros(r)
        self.nvector = np.zeros(r)
        self.zvector = np.zeros(r)
        self.dvector = np.zeros(r)
        for i in range(len(self.pvector)):
            self.pvector[i] = 1 / r
        # print (self.pvector)

    def make_decision(self):
        wheel = random.random()
        self.ptempt = copy.deepcopy(self.pvector)

        # print (self.ptempt)
        for i in range(len(self.ptempt)):
            if i != len(self.ptempt) - 1:
                self.ptempt[i + 1] += self.ptempt[i]
            else:
                self.ptempt[i] += 0

        for i in range(len(self.ptempt)):
            if wheel < self.ptempt[i]:
                self.last_action = i
                self.nvector[self.last_action] += 1
                # print ("Last action in VSLA:",self.last_action)
                # print ("Nvector: ",self.nvector)
                return i

    def update(self, beta):
        # print ("BETA",beta)
        self.zvector[self.last_action] += beta
        # print ("Zvector",self.zvector)
        for i in range(len(self.dvector)):
            if self.nvector[i] == 0:
                self.dvector[i] = 0
            else:
                self.dvector[i] = self.zvector[i] / self.nvector[i]
        # print ("Dvector",self.dvector)
        # print (type(self.dvector))
        # self.last_action = np.argmax(self.dvector)        # for pursuit, uncomment it.
        # print ("Max index in dvector",np.argmax(self.dvector))
        for i in range(len(self.pvector)):
            if i == self.last_action:
                self.pvector[i] = self.pvector[i] + self.lambda1 * beta * (1 - self.pvector[i]) - self.lambda2 * (
                            1 - beta) * self.pvector[i]
            else:
                self.pvector[i] = self.pvector[i] - self.lambda1 * beta * self.pvector[i] + self.lambda2 * (
                            1 - beta) * ((1 / (self.r - 1)) - self.pvector[i])

        # print ("-----------",self.pvector)

    def entropy(self):
        import math
        entropy = 0
        for i in range(self.r):
            if self.pvector[i] != 0:
                entropy += self.pvector[i] * math.log(self.pvector[i], self.r)
        return -1 * entropy

    def set_last_action(self, action):
        self.last_action = action

