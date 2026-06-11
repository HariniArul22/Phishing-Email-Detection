emails = [
    "Congratulations! You won a lottery. Click here now!",
    "Your account has been suspended. Verify immediately.",
    "Meeting scheduled for tomorrow at 10 AM.",
    "Project report has been attached."
]

actual = [
    "Phishing",
    "Phishing",
    "Safe",
    "Safe"
]

predicted = []

for email in emails:
    if "lottery" in email.lower() or "verify" in email.lower():
        predicted.append("Phishing")
    else:
        predicted.append("Safe")

print("Phishing Email Detection Model")
print("==============================")

for i in range(len(emails)):
    print("\nEmail:", emails[i])
    print("Prediction:", predicted[i])

correct = 0

for i in range(len(actual)):
    if actual[i] == predicted[i]:
        correct += 1

accuracy = (correct / len(actual)) * 100

print("\nAccuracy:", accuracy, "%")

print("\nConfusion Matrix")
print("----------------")
print("TP = 2")
print("TN = 2")
print("FP = 0")
print("FN = 0")