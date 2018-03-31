#Code to display graph
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import seaborn as sns
from scipy.stats import f


#importing and reading the .csv file to a dataframe
data = pd.read_csv('E:\Yale\sample_data.csv')
#Finding the datatype of each column
data.dtypes
#Finding the count of missing values in each column
data.isnull().sum()
#Finding the statistical distribution for numerical values
data.describe()
#Finding the statistical distribution for categorcial values
data.describe(include=[np.object])

#Finding the distribution of the variables
data[data.dtypes[(data.dtypes=="float64")|(data.dtypes=="int64")]
                        .index.values].hist(figsize=[11,11])
data['akistage'].value_counts()
# Dropping akistage variable as it is of no importance to us
data.drop(['akistage'], axis=1,inplace= True)
data['akitoenroll'].describe()
sns.set_style("whitegrid")
import matplotlib.pyplot as plt
plt.ylim(0, 900)
ax = sns.boxplot( y="akitoenroll", data=data)
plt.show()
import matplotlib.pyplot as plt
plt.ylim(0, 150)
ax = sns.boxplot( y="akitoenroll", data=data)
plt.show()
data['akitoenroll'].isnull().sum()
data['akitoenroll'].fillna(data['akitoenroll'].median(), inplace= True)

#Imputing the 'enrollcreat' values
ay = sns.boxplot( y="enrollcreat", data=data)
plt.show()
plt.hist(data[data['enrollcreat'].notnull().values]['enrollcreat'])
data['enrollcreat'].fillna(data['enrollcreat'].mean(), inplace= True)
#Imputing the 'maxcreatpostenroll' values
az = sns.boxplot( y="maxcreatpostenroll", data=data)
plt.show()
plt.hist(data[data['maxcreatpostenroll'].notnull().values]['maxcreatpostenroll'])
data['maxcreatpostenroll'].fillna(data['maxcreatpostenroll'].median(), inplace= True)

#Plotting scatter plot for numerical data
from pandas.plotting import scatter_matrix
scatter_matrix(data)
correlations = data.corr()
# plotting correlation matrix
# Generate a mask for the upper triangle
mask = np.zeros_like(correlations, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(correlations, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
#Question 1
data['alert'].value_counts()

#question 2
#Plotting box plot to see if there is any significant difference between enrollcreat for control and test group
sns.set_style("whitegrid")
import matplotlib.pyplot as plt
plt.ylim(0, 5)
ax = sns.boxplot(x="alert", y="enrollcreat", data=data)

#creating new variables for control and test groups
test_enrollcreat = data[data['alert'] == 1]['enrollcreat']
control_enrollcreat = data[data['alert'] == 0]['enrollcreat']

#Plotting histogram to check if the distribution is approximate to normal
plt.hist(test_enrollcreat, color= None, edgecolor= 'green')
plt.title('test_enrollcreat')
plt.hist(control_enrollcreat, color= None, edgecolor= 'blue')
plt.title('control_enrollcreat')

#F-test to test equality of variances
stats.f_oneway(test_enrollcreat,control_enrollcreat)
#T-test to test equality of means
stats.ttest_ind(test_enrollcreat, control_enrollcreat, equal_var= True) 

#question 3
#Plotting box plot to see if there is any significant difference between maxcreatpostenroll for control and test group
sns.set_style("whitegrid")
ax = sns.boxplot(x="alert", y="maxcreatpostenroll", data=data)

#creating new variables for control and test groups
test_maxcreatpostenroll = data[data['alert'] == 1]['maxcreatpostenroll']
control_maxcreatpostenroll = data[data['alert'] == 0]['maxcreatpostenroll']

#Plotting histogram to check if the distribution is approximate to normal
plt.hist(test_maxcreatpostenroll, color= None, edgecolor= 'green')
plt.title('test_maxcreatpostenroll')
plt.hist(control_maxcreatpostenroll, color= None, edgecolor= 'blue')
plt.title('control_maxcreatpostenroll')

#F-test to test equality of variances
stats.f_oneway(test_maxcreatpostenroll,control_maxcreatpostenroll)
#T-test to test equality of means
stats.ttest_ind(test_maxcreatpostenroll, control_maxcreatpostenroll, equal_var= True)

#Question 4- As 38% of the 'los' data is null lets heck the proportion of test and control groups data available
sns.set_style("whitegrid")
ax = sns.boxplot(x="alert", y="los", data=data)

#As most of the data has missing values, creating new variables for control and test groups with  'los' data not null
data1= data[data['los'].notnull()]
test_los = data1[data1['alert'] == 1]['los']
control_los = data1[data1['alert'] == 0]['los']
test_los.count() #25
control_los.count()#23

#Plotting histogram to check if the distribution is approximate to normal
plt.hist(test_los, color= None, edgecolor= 'green')
plt.title('test_los-green')
plt.hist(control_los, color= None, edgecolor= 'blue')
plt.title('control_los-blue')

#F-test to test equality of variances
stats.f_oneway(test_los,control_los)
#T-test to test equality of means
stats.ttest_ind(test_los, control_los, equal_var= True)

#Question 5- As 38% of the 'disch_disposition' data is null lets check the proportion of test and control groups data available
sns.barplot(y="alert", hue="disch_disposition", data=data1)
sns.countplot(y="disch_disposition", hue="alert", data=data1, palette="Greens_d")

#As most of the data has missing values, creating new variables for control and test groups with  'los' data not null
#we are considering the data1 with missing 'los' for missing 'disch_disposition', as only the records with missing los has missing disch_disposition
test_disch_disposition= data1[data1['alert'] == 1]['disch_disposition']
control_disch_disposition = data1[data1['alert'] == 0]['disch_disposition']
test_disch_disposition.count() #25
control_disch_disposition.count()#23
Expired = data1[data1['disch_disposition']=='Expired']
Percent_test_expired=(Expired['alert']==1).count()*100/(data1['alert'] == 1).count()
Percent_control_expired=Expired[Expired['disch_disposition']=='Expired'].count()*100/data1[data1['alert'] == 0].count()


#Question 6- 
sns.set_style("whitegrid")
import matplotlib.pyplot as plt
ax = sns.boxplot(x="alert", y="akitoenroll", data=data) 
#
plt.ylim(0, 120)
ax = sns.boxplot(x="alert", y="akitoenroll", data=data) 

test_akitoenroll = data[data['alert'] == 1]['akitoenroll']
control_akitoenroll = data[data['alert'] == 0]['akitoenroll']
test_akitoenroll.count() #37
control_akitoenroll.count()#40

#Plotting histogram to check if the distribution is approximate to normal
plt.hist(test_akitoenroll, color= None, edgecolor= 'green')
plt.title('test_akitoenroll-green')
plt.hist(control_akitoenroll, color= None, edgecolor= 'blue')
plt.title('control_akitoenroll-blue')

Outlier_records= data[data['akitoenroll']>800]
print(Outlier_records)

#Checking the randomness of admittoenroll variable distribution for test and control group
sns.set_style("whitegrid")
import matplotlib.pyplot as plt
ax = sns.boxplot(x="alert", y="admittoenroll", data=data) 

test_admittoenroll = data[data['alert'] == 1]['admittoenroll']
control_admittoenroll = data[data['alert'] == 0]['admittoenroll']

#Plotting histogram to check if the distribution is approximate to normal
plt.hist(test_admittoenroll, color= None, edgecolor= 'green')
plt.title('test_admittoenroll-green')
plt.hist(control_admittoenroll, color= None, edgecolor= 'blue')
plt.title('control_admittoenroll-blue')
#F-test to test equality of variances
stats.f_oneway(test_admittoenroll,control_admittoenroll)
#T-test to test equality of means
stats.ttest_ind(test_admittoenroll,control_admittoenroll, equal_var= True)

#Checking the randomness of totalalertspt variable distribution for test and control group
sns.set_style("whitegrid")
import matplotlib.pyplot as plt
ax = sns.boxplot(x="alert", y="totalalertspt", data=data) 

test_totalalertspt = data[data['alert'] == 1]['totalalertspt']
control_totalalertspt = data[data['alert'] == 0]['totalalertspt']

#Plotting histogram to check if the distribution is approximate to normal
plt.hist(test_totalalertspt, color= None, edgecolor= 'green')
plt.title('test_totalalertspt-green')
plt.hist(control_totalalertspt, color= None, edgecolor= 'blue')
plt.title('control_totalalertspt-blue')
#F-test to test equality of variances
stats.f_oneway(test_totalalertspt,control_totalalertspt)
#T-test to test equality of means
stats.ttest_ind(test_totalalertspt,control_totalalertspt, equal_var= True)








