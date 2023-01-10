from HybridLearningAutomata import *
import matplotlib.pyplot as plt
HLA = HybridLearningAutomata(2, 1, 0.1, 0, 1)
HLA4 = HybridLearningAutomata(2, 4, 0.1, 0, 1)
HLA6 = HybridLearningAutomata(2, 50, 0.1, 0, 1)
threshold = 0.9
iteration = 100
i = 0
hybrid_beta = 0
hybrid_beta_curve = []
hybrid_action_switching = 0
hybrid_action_switching_curve = []
hybrid_beta_4 = 0
hybrid_beta_curve_4 = []
hybrid_action_switching_4 = 0
hybrid_action_switching_curve_4 = []
hybrid_beta_6 = 0
hybrid_beta_curve_6 = []
hybrid_action_switching_6 = 0
hybrid_action_switching_curve_6 = []

while i < iteration:
    previous = HLA.last_action
    previous4 = HLA4.last_action
    previous6 = HLA6.last_action
    HLA.action_selection()
    HLA4.action_selection()
    HLA6.action_selection()
    now = HLA.last_action
    now4 = HLA4.last_action
    now6 = HLA6.last_action
    if previous != now:
        hybrid_action_switching += 1
    if previous4 != now4:
        hybrid_action_switching_4 += 1
    if previous6 != now6:
        hybrid_action_switching_6 += 1

    random_number = random.random()
    if HLA.last_action == 0:        #update N=1
        if 0 < random_number < threshold:
            HLA.update(1)
            hybrid_beta += 1
            # print('01')
        else:
            HLA.update(0)
            # print('00')
    else:
        if threshold < random_number < 1.0:
            HLA.update(1)
            hybrid_beta += 1
            # print('11')
        else:
            HLA.update(0)
            # print('10')

    if HLA4.last_action == 0:        #update N=4
        if 0 < random_number < threshold:
            HLA4.update(1)
            hybrid_beta_4 += 1
            # print('01')
        else:
            HLA4.update(0)
            # print('00')
    else:
        if threshold < random_number < 1.0:
            HLA4.update(1)
            hybrid_beta_4 += 1
            # print('11')
        else:
            HLA4.update(0)
            # print('10')

    if HLA6.last_action == 0:
        if 0 < random_number < threshold:
            HLA6.update(1)
            hybrid_beta_6 += 1
            # print('01')
        else:
            HLA6.update(0)
            # print('00')
    else:
        if threshold < random_number < 1.0:
            HLA6.update(1)
            hybrid_beta_6 += 1
            # print('11')
        else:
            HLA6.update(0)
            # print('10')
    # print (HLA.FSLA.decision_vector)
    hybrid_beta_curve.append(hybrid_beta)
    hybrid_action_switching_curve.append(hybrid_action_switching)

    hybrid_beta_curve_4.append(hybrid_beta_4)
    hybrid_action_switching_curve_4.append(hybrid_action_switching_4)

    hybrid_beta_curve_6.append(hybrid_beta_6)
    hybrid_action_switching_curve_6.append(hybrid_action_switching_6)

    i += 1
print (hybrid_beta)
print (hybrid_beta_4)
print (hybrid_beta_6)

# plt.plot(hybrid_action_switching_curve)
# plt.title("Hybrid AS")
# plt.show()

random_beta = 0
random_beta_curve = []
random_action_switching = 0
random_action_switching_curve = []
i = 0
action = random.randint(0,1)
while i<iteration:

    new_action = random.randint(0,1)
    if action != new_action:
        random_action_switching += 1

    random_number = random.random()
    if new_action == 0:
        if 0 < random_number < threshold:
            random_beta += 1

    elif new_action == 1:
        if threshold < random_number < 1.0:
            random_beta += 1
    action = new_action
    random_action_switching_curve.append(random_action_switching)
    random_beta_curve.append(random_beta)
    i += 1


print (random_beta)
plt.plot(random_beta_curve,color='black', label='Pure Chance Automata')
plt.plot(hybrid_beta_curve,color='red', label='Hybrid Automata (N=1)', linestyle='dashed')
plt.plot(hybrid_beta_curve_4,color='blue', label='Hybrid Automata (N=4)', linestyle='dashed')
plt.plot(hybrid_beta_curve_6,color='green', label='Hybrid Automata (N=6)', linestyle='dashed')
plt.xlabel("Iteration")
plt.ylabel("TNR")
plt.title("Ex 1.1")
plt.legend()
plt.savefig("Hybrid Results/1_1_1.png")
plt.show()
plt.close()

plt.plot(random_action_switching_curve,color='black', label='Pure Chance Automata')
plt.plot(hybrid_action_switching_curve,color='red', label='Hybrid Automata (N=1)', linestyle='dashed')
plt.plot(hybrid_action_switching_curve_4,color='blue', label='Hybrid Automata (N=4)', linestyle='dashed')
plt.plot(hybrid_action_switching_curve_6,color='green', label='Hybrid Automata (N=6)', linestyle='dashed')
plt.xlabel("Iteration")
plt.ylabel("TNAS")
plt.title("Ex 1.1")
plt.legend()
plt.savefig("Hybrid Results/1_1_2.png")
plt.show()
plt.close()

print (hybrid_action_switching)
print (hybrid_action_switching_4)
print (hybrid_action_switching_6)