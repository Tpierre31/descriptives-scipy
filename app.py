from webbrowser import get
import pandas as pd
import numpy as np
import pandas.plotting as plotting
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats
import seaborn
from matplotlib import pyplot as plt

data = pd.read_csv('/Users/thierrypierre/Documents/GitHub/descriptives-scipy/data/brain_size.csv')

t = np.linspace(-6, 6, 20)
sin_t = np.sin(t)
cos_t = np.cos(t)

pd.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t}) 

data.shape

data.columns  

print(data['Gender'])

groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['VIQ']:
    print((gender, value.mean()))

plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])

stats.ttest_1samp(data['VIQ'], 0)  

female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']
stats.ttest_ind(female_viq, male_viq) 

stats.ttest_ind(data['FSIQ'], data['PIQ'])

stats.ttest_rel(data['FSIQ'], data['PIQ'])

stats.ttest_1samp(data['FSIQ'] - data['PIQ'], 0)

stats.wilcoxon(data['FSIQ'], data['PIQ']) 

x = np.linspace(-5, 5, 20)
np.random.seed(1)

y = -5 + 3*x + 4 * np.random.normal(size=x.shape)

data = pd.DataFrame({'x': x, 'y': y})

model = ols("y ~ x", data).fit()

print(model.summary()) 

data = pd.read_csv('data/brain_size.csv', sep=';', na_values=".")

model = ols("VIQ ~ Gender + 1", data).fit()
print(model.summary())  

model = ols('VIQ ~ C(Gender)', data).fit()

data_fisq = pd.DataFrame({'iq': data['FSIQ'], 'type': 'fsiq'})
data_piq = pd.DataFrame({'iq': data['PIQ'], 'type': 'piq'})
data_long = pd.concat((data_fisq, data_piq))
print(data_long)  

model = ols("iq ~ type", data_long).fit()
print(model.summary())

stats.ttest_ind(data['FSIQ'], data['PIQ'])

data = pd.read_csv('examples/iris.csv')
model = ols('sepal_width ~ name + petal_length', data).fit()
print(model.summary())  

print(model.f_test([0, 1, -1, 0]))

print(data)  

seaborn.pairplot(data, vars=['WAGE', 'AGE', 'EDUCATION'],
                 kind='reg')

seaborn.lmplot(y='WAGE', x='EDUCATION', data=data)

result = sm.ols(formula='wage ~ education + gender + education * gender',
                data=data).fit()    
print(result.summary()) 


