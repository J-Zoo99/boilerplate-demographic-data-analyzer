import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    print(df)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = round((df.loc[df["sex"] == "Male"].mean()["age"]),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(((df.loc[df["education"] == "Bachelors"].size) / df.size ) * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.query("education == 'Bachelors' | education == 'Masters' | education == 'Doctorate'")
    lower_education = df.query("(education == 'Bachelors' | education == 'Masters' | education == 'Doctorate') == False")

    # percentage with salary >50K
    he_rich_no = higher_education.loc[higher_education['salary'] == ">50K"]
    print(len(he_rich_no))
    higher_education_rich = round(len(he_rich_no) / len(higher_education) * 100, 1)
    lw_rich_no = lower_education.loc[lower_education['salary'] == ">50K"]
    lower_education_rich = round(len(lw_rich_no) / len(lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.sort_values("hours-per-week", ascending = True)['hours-per-week'].iloc[0]

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df["hours-per-week"] == min_work_hours]
    min_rich = num_min_workers.loc[num_min_workers['salary'] == ">50K"]
    rich_percentage = len(min_rich) / len(num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    df_countries = df.groupby(['native-country',"salary"]).count()
    highest_earning_country = ""
    highest_earning_country_percentage = 0

    country_name = ""
    less_than_50k = 0
    for row in df_countries.index:
        if (country_name == row[0]):
            more_than_50k = df_countries.loc[row]["age"]
            country_percentage = round((more_than_50k / (less_than_50k + more_than_50k)) * 100, 1 )
            if (country_percentage > highest_earning_country_percentage):
                highest_earning_country_percentage = country_percentage
                highest_earning_country = row[0]
        else:
            country_name = row[0]
            less_than_50k = df_countries.loc[row]["age"]

        



    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
