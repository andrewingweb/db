import pandas as pd

dataset = pd.read_csv('DBNetz.csv', sep=';')

data = dataset[['RL100-Code', 'RL100-Langname', 'Typ Kurz', 'Regionalbereich']]
# print(data)

def searchByBcode():
    betr = input("Enter Betriebsstelle Abk: ").upper()

    print(data.loc[data['RL100-Code'] == betr])


def searchByBname():
    bname=str(input('Enter Betirebsstelle Name: ').title())

    print(data.loc[data['RL100-Langname'] == bname])

print('Enter 1 to search by Betriebsstelle Abkürzung ')
print('Enter 2 to search by Betriebsstelle Name ')

src=int(input('Enter here: '))

if src == 1:
    searchByBcode()
elif src == 2:
    searchByBname()
else:
    print('Falsche Eingabe!')

