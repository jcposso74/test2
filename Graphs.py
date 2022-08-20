import numpy as np
import matplotlib.pyplot as plt

Hours_taken = [1.5,3.1,5.2]
Number_of_Neuron = ['200', '400', '800']

plt.plot(Number_of_Neuron,Hours_taken, color='red', marker='o')
plt.title('Time taken VS Number of Neurons - c0810093')
plt.ylabel('Time taken')
plt.xlabel('Number of Neurons')
plt.show()

Hours_taken= [1.5,0.2,0.2]
Learning_Rate= ['0.0001', '0.001', '0.01']
plt.plot(Learning_Rate,Hours_taken , color='red', marker='o')
plt.title('Time taken VS Learning Rate - c0810093')
plt.ylabel('Time taken')
plt.xlabel('Learning Rate')
plt.show()



Ram_Usage = [275.8,331.0,333.1]
Number_of_Neuron = ['200', '400', '800']

plt.plot(Number_of_Neuron,Hours_taken, color='red', marker='o')
plt.title('Ram Usage VS Number of Neurons - c0810093')
plt.ylabel('Ram Usage')
plt.xlabel('Number of Neurons')
plt.show()


Ram_Usage2 = [275.8,331.0,333.1]
Learning_Rate1 = ['0.0001', '0.001', '0.01']

plt.plot(Learning_Rate1,Ram_Usage2,  color='red', marker='o')
plt.title('Ram Usage VS Learning Rate - c0810093')
plt.ylabel('Ram Usage')
plt.xlabel('Leaning Rate')
plt.show()