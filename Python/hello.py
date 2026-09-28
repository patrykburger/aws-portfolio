hourly_rate = float(input("Enter your hourly rate: "))
hours_per_week = int(input("Enter hours per week: "))
weeks_per_year = int(input("Enter weeks per year: "))

weekly_salary = hourly_rate * hours_per_week
yearly_salary = weekly_salary * weeks_per_year
monthly_salary = yearly_salary / 12

print(f"Weekly salary: £{weekly_salary:.2f}")
print(f"Yearly salary: £{yearly_salary:.2f}")
print(f"Monthly salary: £{monthly_salary:.2f}")

if hourly_rate < 20:
    print("Your hourly rate is below £20.")
elif hourly_rate == 20:
    print("Your hourly rate is exactly £20.")
else:
    print("Your hourly rate is above £20.")

if hourly_rate >= 20 and hours_per_week >= 40:
    print("Good hourly rate and full-time hours.")

if hourly_rate >= 20 or hours_per_week >= 40:
    print("At least one condition is met.")

if not hours_per_week >= 40:
    print("You are not working full-time hours.")

name = input("Enter your name: ")
print(name.strip().title())

company = "Amazon"
new_company = "Microsoft"

print(f"I work at {company}")
print(f"My name is {name.strip().title()} and I work at {new_company}")

companies = ["Amazon", "Microsoft", "Google", "Apple"]

print(companies)

print(companies[0])
print(companies[2])

companies[1] = "Tesla" 
print(companies)

companies.append("Meta")
companies.insert(1, "Microsoft")
print(companies)

companies.remove("Tesla")
print(companies)

companies.pop(3)
print(companies)

print(len(companies))

print("Amazon" in companies)

print("Tesla" in companies)

print("Tesla" not in companies)

print(companies[0:2])

print(companies[1:3])

print(companies[-2:])

print(companies[:])

if "Google" in companies:
    print("Google is in the company list.")

if "Tesla" in companies:
    print("Tesla is in the company list.")
else:
    print("Tesla is not in the company list.")

for company in companies:
    print(company)

for company in companies:
    if company == "Amazon":
        print(company)

for company in companies:
    if company != "Amazon":
        print(company)

count = 0
for company in companies:
    count = count + 1

print(count)

count = 10
count += 5
print(count)

count = 0
for company in companies:
    count += 1

print(count)

for company in companies:
    if len(company) > 5:
        print(company)

for company in companies:
    if len(company) <= 5:
        print(company)

for company in companies:
    if len(company) > 5:
        print(company, "Long name")
    else:
        print(company, "Short name")

for company in companies:
    if len(company) > 7:
        print(company, "Very long")
    elif len(company) >= 6:
        print(company, "Medium")
    else:
        print(company, "Short")

scores =[95, 72, 91, 58, 83]

for score in scores:
    print(score)

for score in scores:
    if score >= 70:
        print(score)

count = 0
for score in scores:
    if score >= 70:
        count += 1

print(count)

total = 0
for score in scores:
    total += score

print(total)

average = total / len(scores)
print(average)

if average >= 90:
    print("Excellent")
elif average >= 70:
    print("Pass")
else:
    print("Fail")

highest = max(scores)
print(highest)

lowest = min(scores)
print(lowest)

total_scores = sum(scores)
print(total_scores)

sorted_scores = sorted(scores)
print(sorted_scores)

scores.sort()
print(scores)