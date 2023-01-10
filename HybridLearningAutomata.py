import numpy as np
import random
import math
from LA import *
from FixedStructureLearningAutomata import *


class HybridLearningAutomata:
    FSLA = None
    VSLA = None
    mode = ''
    turn = ''
    nvector = np.zeros(0)

    def __init__(self, r, N, lambda1, lambda2, c=0):
        self.VSLA = LA(r, lambda1, lambda2)
        self.FSLA = FixedStructureLearningAutomata(r, N, c)
        self.mode = 'V'
        self.turn = 'V'
        self.last_action = c
        self.nvector = np.zeros(r)

    def action_selection(self):
        if self.mode == 'V':
            self.last_action = self.VSLA.make_decision()
            self.FSLA.set_last_action(self.last_action)
            # self.VSLA.set_last_action(self.last_action)
            self.turn = 'V'
            self.mode = 'F'
            self.nvector[self.last_action] += 1
            return self.last_action
        elif self.mode == 'F':
            self.last_action = self.FSLA.get_color()
            # self.FSLA.set_last_action(self.last_action)
            self.VSLA.set_last_action(self.last_action)
            self.turn = 'F'
            self.nvector[self.last_action] += 1
            return self.last_action

    def update(self, beta):
        if beta == 1:
            if self.turn == 'V':
                # print ('update V1')
                self.VSLA.update(1)
                self.mode = 'F'
            elif self.turn == 'F':
                # print('update F1')
                self.FSLA.update(1)
                self.FSLA.last_action = self.last_action
        elif beta == 0:
            if self.turn == 'V':
                # print('update V0')
                self.VSLA.update(0)
                self.mode = 'V'
            elif self.turn == 'F':
                s = 0
                for i in range(len(self.FSLA.decision_vector)):
                    s += self.FSLA.decision_vector[i]
                if s == 1:  # if we are on edges.
                    # print ('update v0')
                    self.VSLA.update(0)
                    self.mode = 'V'
                    # print ('mode changed to V')
                elif s > 1:  # if we are not on edges.
                    self.FSLA.update(0)
                    # print('update F0')
        else:
            print('Beta is not acceptable. it should be either 1 or 0.')

    def get_action(self):
        return self.last_action

    def entropy(self):
        # print (self.FSLA.entropy())
        # print (self.VSLA.entropy())
        return self.FSLA.entropy() * self.VSLA.entropy()
