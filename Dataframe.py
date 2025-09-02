# create DataFrame using Array
Data=np.random.randint(1,5,(10,9))
Data
df=pd.DataFrame(Data, index=['Panipuri','Samosa','Vadapav','misal','chilli','pohe','masala_bhat','bhaji','Dosa','idli'],columns=['teja','yash','vija','nikita','akshu','sani','misal','pinki','gayu'])
df
