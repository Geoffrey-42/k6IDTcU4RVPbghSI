path = ''
poll = pd.read_csv(path+"ACME-HappinessSurvey2020.csv")

print('\nThe 5 first poll answers are:\n')
print(poll.head())
print('\n Description of the poll dataset:\n')
print(poll.describe())
