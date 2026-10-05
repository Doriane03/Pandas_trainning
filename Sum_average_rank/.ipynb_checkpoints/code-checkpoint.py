#importing pandas
import pandas as pd
#DataFrame creation
classeA_initial=pd.DataFrame({
'Nom':['doriane','franck','ariel'],
'Age':[12,14,16],
'Math':[17,5,9],
'Svt':[14,5,7],
'Pc':[12,14,16],
})
#changes implemented
#Sum of each student's grades
sum_grades=classeA_initial.loc[:,['Math', 'Svt', 'Pc']].apply(sum,axis=1)
#overall average
overall_average=sum_grades.map(lambda x:x/3,na_action='ignore').round(decimals=2)
#Rank based on the average
rank_average=overall_average.rank(ascending=False)
#classeA_initial update to classeA_final
classeA_final=pd.DataFrame({
'Nom':['doriane','franck','ariel'],
'Age':[12,14,16],
'Math':[17,5,9],
'Svt':[14,5,7],
'Pc':[12,14,16],
'sum':sum_grades,
'overall_average':overall_average,
'rank':rank_average,
})
#display of classeA initial
print("classeA initial")
print(classeA_initial)
#display of classeA update
print("classeA update ")
print(classeA_final)
