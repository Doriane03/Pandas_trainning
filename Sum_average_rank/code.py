import pandas as pd
#dataframe creation
classeA_initial=pd.DataFrame({
'Nom':['doriane','franck','ariel'],
'Age':[12,14,16],
'Math':[17,5,9],
'Svt':[14,5,7],
'Pc':[12,14,16],
})
#changes implemented
#sum
som=classeA_initial.loc[:,['Math','Svt','Pc']].apply(sum,axis=1)
#moy
moyenne=som.map(lambda x:x/3,na_action='ignore').round(decimals=2)
#rank
rang=moyenne.rank(ascending=False)
#display of classeA initial
print("classeA initial")
print(classeA_initial)

#classeA_initial update to classeA_final
classeA_final=pd.DataFrame({
'Nom':['doriane','franck','ariel'],
'Age':[12,14,16],
'Math':[17,5,9],
'Svt':[14,5,7],
'Pc':[12,14,16],
'sum':som,
'moy':moyenne,
'rank':rang,
})
print("classeA update ")
print(classeA_final)
