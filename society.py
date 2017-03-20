import random

people = []
for i in range(1000):
    people.append(1000)

for i in range(1000):

    companies = []
    count = 0
    while count < 100:
        company = random.randint(0, 999)
        if company not in companies:
            companies.append(company)
            count += 1

    investors = []
    count = 0
    while count < 100:
        investor = random.randint(0, 999)
        if investor not in (companies or investors):
            investors.append(investor)
            count += 1

    bonds = {}
    for investor in investors:
        bonds[investor] = random.choice(companies)

    lucky_companies = []
    for company in companies:
        if random.randint(0, 99) > 49:
            lucky_companies.append(company)
            people[company] = people[company]*1.1
        else:
            people[company] = people[company]*0.9

    lucky_investors = []
    for lucky_company in lucky_companies:
        for investor in bonds:
            if bonds[investor] == lucky_company:
                lucky_investors.append(investor)
                people[int(investor)] = people[int(investor)]*1.1

    for investor in investors:
        if investor not in lucky_investors:
            people[int(investor)] = people[int(investor)]*0.9

    adventurers = investors + companies
    for i in range(1000):
        if i not in adventurers:
            people[i] = people[i]*1.05

total = 0
for money in people:
    total += money
for i in range(1000):
    people[i] = round(people[i]*1000000/total)

supe_count = 0
rich_count = 0
ordi_count = 0
poor_count = 0
for money in people:
    if money > 4000:
        supe_count += 1
    elif money > 2000:
        rich_count += 1
    elif money > 500:
        ordi_count += 1
    else:
        poor_count += 1

print(supe_count, rich_count, ordi_count, poor_count)