name = input("Employee Name: ")
projects = int(input("Number of Projects: "))
completed = int(input("Projects Completed: "))
hours = float(input("Working Hours: "))

completion_rate = (completed / projects) * 100
avg_hours = hours / completed

print("\n--- Performance Report ---")
print(f"Employee: {name}")
print(f"Projects: {projects}")
print(f"Completed: {completed}")
print(f"Working Hours: {hours}")
print(f"Completion Rate: {completion_rate:.2f}%")
print(f"Average Hours per Completed Project: {avg_hours:.2f}")