from mpin_validator import evaluate_mpin

def main():
    print("MPIN Strength Checker")
    mpin = input("Enter MPIN (4 or 6 digits): ").strip()
    dob_self = input("Enter DOB (YYYY-MM-DD): ").strip()
    dob_spouse = input("Enter Spouse DOB (YYYY-MM-DD): ").strip()
    anniversary = input("Enter Anniversary (YYYY-MM-DD): ").strip()

    result = evaluate_mpin(mpin, dob_self, dob_spouse, anniversary)
    print("\nResult:")
    print(f"MPIN: {mpin}")
    print(f"Strength: {result['strength']}")
    print(f"Reasons: {result['reasons']}")
    print("Decision:", "REJECT" if result["strength"] == "WEAK" else ("ACCEPT" if result["strength"] == "STRONG" else "INVALID"))

if __name__ == "__main__":
    main()
