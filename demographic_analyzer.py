import pandas as pd

file_data = r'C:\Users\USER\Desktop\PROJECT FILE\dataset\adult.csv'

data = pd.read_csv(file_data)
print(data.head())

# Q1 numbers of race---
count_race = data["race"].value_counts()
print(count_race)

# Q2 the average age of men--
average_age_men = data.groupby('sex')['age'].mean() ['Male']


print(average_age_men)

# calculate the percentage of people with bachelors degree---
count_of_education = data['education'].count()
parcentage_of_bachelors = (data['education'].value_counts(normalize=True)['Bachelors'])* 100
print(parcentage_of_bachelors)

# parcentage of people with advanve education in [doctorate,masters, bachelors] that makes more than 50k
advance_degree = ["Doctorate" ,"Masters", "Bachelors"]
advance_educated=data[data['education'].isin(advance_degree)]
percentage_advance_degree = round(advance_educated["income"].value_counts(normalize=True)[">50K"] * 100,1)
print(percentage_advance_degree)


# percentage of people without advanced education that earn more than 50k
nonadvanced_degree = ["some-college","preschoo","prof-school", "Assoc-acdm"," Assoc-voc","HS-grad","9th","7th-8th","5th-6th","1th-4th","12th",
"11th", "10th"]
nonadvanced_educated =data[data['education'].isin(nonadvanced_degree)]
percecentage_nonadvance_educated = round(nonadvanced_educated["income"].value_counts(normalize=True)[">50K"] * 100,1)
print(percecentage_nonadvance_educated)

# whats the minimum number of hours a person works per week
min_work_hour =data["hours.per.week"].min()
print(min_work_hour)

# what percentage of the people who work the min number of hours perweek have a salary of more than 50K
min_hours_worker =data["hours.per.week"] ==min_work_hour
percentage_min_workers= data.loc[min_hours_worker,"income"].eq(">50K").mean() * 100
print (percentage_min_workers)

# What country has the highest percentage of people that earn >50K and what is that percentage?
more_than_50k_count_per_country = data[data["income"] == ">50K"]["native.country"].value_counts()
total_per_country = data["native.country"].value_counts()
max_percentage = ((more_than_50k_count_per_country / total_per_country) * 100).max()
print(max_percentage)
max_percentage_country = ((more_than_50k_count_per_country / total_per_country) * 100).idxmax()
print(max_percentage_country)


#  most popular occupation among those earning more than 50K in India
earning_more_than_50K_india = data[(data["income"] == ">50K") & (data["native.country"] == "India")]
most_popular_occupation = (earning_more_than_50K_india["occupation"]).value_counts().idxmax()
print(most_popular_occupation)