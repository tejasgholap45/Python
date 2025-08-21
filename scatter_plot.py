import matplotlib.pyplot as plt
import numpy as np

x=[3,4,5,7,5,6,7,9,7,8,9,7]
y=[4,3,5,4,6,7,8,2,1,6,4,2]
plt.scatter(x,y,marker='+',color ='r',s=150)
plt.title('data distribution')
plt.xlabel('income')
plt.ylabel('spending score')
plt.show()
