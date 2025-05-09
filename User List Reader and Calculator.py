import pandas as pd

# Διαβάζει το αρχείο Excel
df = pd.read_excel("users.xlsx")

# Φιλτράρει τους ενεργούς χρήστες άνω των 30 ετών
active_over_30 = df[(df["Ηλικία"] > 30) & (df["Ενεργός"] == "Ναι")]

# Εμφάνιση των ενεργών χρηστών άνω των 30
print("Active user over 30:")
print(active_over_30)

# Υπολογισμός μέσου όρου ηλικίας όλων των χρηστών
mean_age = df["Ηλικία"].mean()
print(f"\nAverage age of users: {mean_age:.2f} years")

# Υπολογισμός μέσου όρου μισθού των ενεργών χρηστών
active_users = df[df["Ενεργός"] == "Ναι"]
mean_salary_active = active_users["Salary (€)"].mean()
print(f"Average salary of active users: {mean_salary_active:.2f} €")

# Αποθήκευση των ενεργών χρηστών άνω των 30 σε νέο αρχείο
active_over_30.to_excel("active_users_over30.xlsx", index=False)

print("\nThe file active_users_over30.xlsx has been successfully created.")
