from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
import os
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
watlevl=pd.read_csv("chennai_reservoir_levels.csv")
watlevl['Dat'] = pd.to_datetime(watlevl['Date'])
mean_level = watlevl.groupby(watlevl['Dat'].dt.year).agg(np.mean).reset_index()
X=mean_level.iloc[:,:-4]
y=mean_level.iloc[:,1:5]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
print(X_train)
print(y_train)
print(X_test)
print(y_test)
###################################LinearRegression###################################################
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)
a=regressor.predict(X_test)
sc1=r2_score(a,y_test)
print(sc1)
#####################################DTREE ALGORITHM##################################################
from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor(random_state = 0)
dt.fit(X, y)
y_pred = dt.predict(X_test)
sc2=r2_score(y_pred,y_test)
print(sc2)
####################################RANDOM FOREST#######################################################
from sklearn.ensemble import RandomForestRegressor 
clf=RandomForestRegressor(n_estimators = 100, random_state = 0)
clf.fit(X, y)
data=clf.predict(X_test)
sc3=r2_score(data,y_test)
print(sc3)


#############################################PLOT GRAPH################################################
import matplotlib.pyplot as plt
plt.plot(X,mean_level['POONDI'],color='green',label = 'POONDI')
plt.plot(X,mean_level['CHOLAVARAM'],color='red',label = 'CHOLAVARAM')
plt.plot(X,mean_level['REDHILLS'],color='blue',label = 'REDHILLS')
plt.plot(X,mean_level['CHEMBARAMBAKKAM'],color='black',label = 'CHEMBARAMBAKKAM')
plt.legend()
plt.title("Water Graph")
plt.xlabel("YEAR")
plt.ylabel("water level mcftl")
plt.show()
wat =Tk()

###########################################TK INTERtittle################################################
wat.title("CHENNAI WATER MANAGEMENT")
wat.geometry("500x200")
wat.configure(background="black")



###################################################button action
def pred():
    item1 = (txtnum.get())
    #print(item1)
    if len(item1)<4:
        messagebox.showerror("Input Error","%a is an Invalid Input!,Please Give Proper Input"%item1)
        wat.mainloop()
    elif len(item1)>4:
        messagebox.showerror("Input Error","%a is an Invalid Input!,Please Give Proper Input"%item1)
        wat.mainloop()
    if (item1.isdigit()):
        #print(type(item1))
        fut=np.array(int(item1))
        #print(type(fut))
        #va=int(fut)
        #print(va)
        y_pred1 = regressor.predict([[fut]]) 
        y_pre2 = dt.predict([[fut]])
        y_pre3=clf.predict([[fut]])
       # print(y_pred)
        r=[]
        for i in y_pre3:
            i=i/float(28.3168)
            r.append(i)
        dat=r
        arr=dat[0]
        POONDI_pre=str(arr[0])
        CHOLAVARAM_pre=str(arr[1])
        REDHILLS_pre=str(arr[2])
        CHEMBARAMBAKKAM_pre=str(arr[3])
        print('********************************************************')
        output=print('\n\n\nThe future water level used in the year of',item1,"is \n********************************************************\nfrom POONDI is",POONDI_pre," Millon Cublic Feet\n\nfrom CHOLAVARAM is",CHOLAVARAM_pre," Millon Cublic Feet\n\nfrom REDHILLS is",REDHILLS_pre," Millon Cublic Feet\n \nfrom CHEMBARAMBAKKAM is",CHEMBARAMBAKKAM_pre,"  Millon Cublic Feet")
        output_msg='The future water level used in the year of',item1,"is \n**********************************************************\n from POONDI is",POONDI_pre," Millon Cublic Feet\n from CHOLAVARAM is",CHOLAVARAM_pre," Millon Cublic Feet\n from REDHILLS is",REDHILLS_pre," Millon Cublic Feet\n from CHEMBARAMBAKKAM is",CHEMBARAMBAKKAM_pre,"  Millon Cublic Feet"
        
        messagebox.showinfo("predicted output",output_msg)
yer=StringVar()
#label creation
flabel=Label(wat,text="FUTURE YEAR",fg="white",bg="black",font="verdana 15 bold").place(x=50,y=70)
txtnum=Entry(wat,font="Times 15 bold")
txtnum.place(x=250,y=70)
#button creation
Button2 = Button(text= "prdict",command=pred,font="Times 15 bold").place(x=250,y=150)
wat.mainloop()


