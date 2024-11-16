#importing matplotlib
import matplotlib.pyplot as plt
#importing pandas 
import pandas as pd
#importing seaborn
import seaborn as sns
#reading dataframe
rdf=pd.read_csv("gappy.csv")
print(rdf.head(10))
#making barplot
#plt.figure(figsize=(14,16))
plots=sns.barplot(rdf,x='continent',y='life_exp')
for bar in plots.patches:
    x=bar.get_x() + bar.get_width()/2
    y=bar.get_height()
    plots.annotate(format(y, '.2f'),(x, y), ha='center', va='center',size=12,xytext=(0, 8),textcoords='offsetpoints')
plt.title("ANNOTATED BARPLOT FOR LAZY PEOPLE.")
plt.xlabel='continent'
plt.ylabel='life_exp'
plt.show()