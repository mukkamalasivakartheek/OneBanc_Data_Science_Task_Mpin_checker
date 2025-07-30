def evaluate_mpin(mpin: str, dob_self: str = "", dob_spouse: str = "", anniversary: str = "") -> dict:
    COMMON_4 = {"1234", "0000", "1111", "1122", "1212", "7777", "1004", "2000"}
    COMMON_6 = {"123456", "000000", "111111", "654321", "121212"}

    if not mpin or not mpin.isdigit() or len(mpin) not in [4, 6]:
        return {"strength": "INVALID", "reasons": ["INVALID_FORMAT"]}

    reasons = []

    if (len(mpin) == 4 and mpin in COMMON_4) or (len(mpin) == 6 and mpin in COMMON_6):
        reasons.append("COMMONLY_USED")

    def date_variants(date):
        if not date or len(date.split("-")) != 3:
            return set()
        y, m, d = date.split("-")
        yy = y[2:]
        return {
            d + m, m + d,
            yy + m, m + yy,
            d + m + yy, yy + m + d, m + d + yy, yy + d + m,
            d + m + y, y + m + d, m + d + y, y + d + m,
            d + yy + m, m + yy + d, yy + d, d + yy,
        }

    def check_date(label, date):
        if mpin in date_variants(date):
            reasons.append(label)

    check_date("DEMOGRAPHIC_DOB_SELF", dob_self)
    check_date("DEMOGRAPHIC_DOB_SPOUSE", dob_spouse)
    check_date("DEMOGRAPHIC_ANNIVERSARY", anniversary)

    return {
        "strength": "WEAK" if reasons else "STRONG",
        "reasons": reasons
    }
