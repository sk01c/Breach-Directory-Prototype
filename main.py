self_declared = []
nature_of_discovery = []
dates = []
entities = []
department = []
breach_category = []
MNPI = []
root_cause_analysis = []
dlfl = []
internal_conflict = []
intentional_misuse_of_confidential_data = []
customer_detriment = []
market_impact = []
reputational_impact = []

input("Breach Directory. Press enter to continue")

sd = input("Firstly, could you tell me if this incident was self declared or not? Type yes/no\n").lower()
if sd == "yes":
    self_declared.append(1)
    nature_of_discovery.append("Self declared")
    pass
elif sd == "no":
    self_declared.append(0)
    nat_d = input("Please enter the nature of discovery given the following options:\n1) Data from HR \n"
                  "2) Data from internal audit \n3) Data from external audit \n4) Other\nPlease select a number\n")
    nature_of_discovery.append(nat_d)
else:
    print("Please enter yes or no")

d = input("Please enter the date of the incident in the form dd/mm/yyyy\n")
dates.append(d)

e = input("Please enter the entity in which this incident took place\n")
entities.append(e)

dep = input("Please enter the department in which this took place\n")
department.append(dep)

b = input("Please enter which KRI this event had breached\n")

ITSD = input("Before we continue, we need to clarify if this breach resulted in data loss. "
             "Please enter yes or no\n").lower()
if ITSD == "yes":
    input("Please contact ITSD to ensure this issue has been dealt with before returning. "
          "Press enter to continue once contacted\n")
elif ITSD == "no":
    pass

insider = input("Was this a case of MNPI (insider information involved)? Please enter yes or no\n").lower()

if insider == "yes":
    input("Please contact the compliance advisory team to ensure this issue has been dealt with before returning. "
          "Press enter to continue once contacted\n")
    MNPI.append(1)
elif insider == "no":
    MNPI.append(0)

rca = input("Please enter which root cause you see as most apt for this breach: \n1) Human Error \n2) Negligence\n"
            "3) Intentional\n4) Process Error\n5) Other\nPlease select a number to continue\n")
root_cause_analysis.append(rca)

input("Now we will assign a score to the breach severity\nFor the following criterium, "
      "enter 1 if they occurred in the breach, 0 otherwise\nPress enter to continue")

data_financial = input("Data/Financial loss\n")
dlfl.append(data_financial)

ic = input("Internal conflict\n")
internal_conflict.append(ic)

imd = input("Intentional misuse of data\n")
intentional_misuse_of_confidential_data.append(imd)

cd = input("Customer detriment\n")
customer_detriment.append(cd)

mi = input("Market impact\n")
market_impact.append(mi)

ri = input("Reputational impact\n")
reputational_impact.append(ri)

print("**HERE BASED ON WEIGHTINGS, WE CAN CALCULATE AND ASSIGN RATING")












