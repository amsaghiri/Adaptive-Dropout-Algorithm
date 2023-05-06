import numpy as np
import random
import math


class FixedStructureLearningAutomata:
    r = 0
    N = 0
    decision_vector = np.zeros(0)
    last_action = 0
    nvector = np.zeros(0)
    # def __init__(self, r, N):
    #     self.r = r
    #     self.N = N
    #     self.decision_vector = np.zeros(r)
    #     self.last_action = random.randint(0, r - 1)
    #     self.decision_vector[self.last_action] = 1
    #     # print(self.decision_vector)

    def __init__(self, r, N, color):
        self.r = r
        self.N = N
        self.decision_vector = np.zeros(r)
        self.last_action = color
        self.decision_vector[self.last_action] = 1
        self.nvector = np.zeros(r)

    def make_decision(self):
        for i in range(len(self.decision_vector)):
            if self.decision_vector[i] != 0:
                self.last_action = i
                self.nvector[i] += 1
                return i

    def make_a_new_decision(self):
        self.last_action = random.randint(0, self.r - 1)
        self.decision_vector[self.last_action] = 1
        return self.last_action

    def update(self, beta):
        if beta == 1:
            for i in range(len(self.decision_vector)):
                if self.decision_vector[i] != 0:
                    if self.decision_vector[i] < self.N:

                        self.decision_vector[i] += 1
                        self.last_action = i

        elif beta == 0:
            for i in range(len(self.decision_vector)):
                if self.decision_vector[i] != 0:
                    # print (i)
                    if self.decision_vector[i] == 1:
                        self.decision_vector[i] = 0
                        # self.decision_vector[int(math.fmod(i + 1, self.r))] = 1   # go to the next state, numeric wise
                        # self.color = int(math.fmod(i + 1, self.r))
                        next = int(random.randint(0, self.r-1))                     # choose a random state as the next
                        self.decision_vector[next] = 1
                        self.last_action = next
                    elif self.decision_vector[i] > 1:
                        self.decision_vector[i] -= 1
                        # self.last_action = i
                    break
        # print(self.decision_vector)

    def get_color(self):
        # print ('Last action in FSLA:',self.last_action)
        return self.last_action

    def set_last_action(self, i):
        self.last_action = i
        for j in range(len(self.decision_vector)):
            if j != i:
                self.decision_vector[j] = 0
            else:
                self.decision_vector[j] = 1

    def entropy(self):
        for i in range (len(self.decision_vector)):
            if self.decision_vector[i] != 0:
                if (self.N - self.decision_vector[i] != 0):
                    # return -1*((self.N - self.decision_vector[i]) / self.N)*math.log(((self.N - self.decision_vector[i]) / self.N),2)
                    return (self.N - self.decision_vector[i]) / self.N
                else:
                    return 0