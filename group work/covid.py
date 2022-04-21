#data source from https://data.go.th/dataset/covid
import pandas as pd
import matplotlib.pyplot as plt

x = [] #date
x1 = ['12/4/2022','13/4/2022','14/4/2022','15/4/2022','16/4/2022','17/4/2022','18/4/2022','19/4/2022']
y = [] #amount
 
data = pd.read_csv('covid19.csv')
lines = data["announce_date"].values.tolist()
    
print('start x')
    
for row in lines:
    x.append(row)
    
print('start y')   

y.append(x.count('12/4/2022'))
y.append(x.count('13/4/2022'))
y.append(x.count('14/4/2022'))
y.append(x.count('15/4/2022'))
y.append(x.count('16/4/2022'))
y.append(x.count('17/4/2022'))
y.append(x.count('18/4/2022'))
y.append(x.count('19/4/2022'))    

'''print(x)
print(y)'''
 
plt.plot(x1,y, color = 'g', linestyle = 'dashed',
        label = "Covid Data")
  
plt.xlabel('Dates')
plt.ylabel('Amount')
plt.title('Covid Report', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
