import pytest
from mpin_validator import evaluate_mpin

@pytest.mark.parametrize("mpin, dob_self, dob_spouse, anniv, expected_strength, expected_reasons", [
    ("1234", "", "", "", "WEAK", ["COMMONLY_USED"]),
    ("0000", "", "", "", "WEAK", ["COMMONLY_USED"]),
    ("1111", "", "", "", "WEAK", ["COMMONLY_USED"]),
    ("1122", "", "", "", "WEAK", ["COMMONLY_USED"]),
    ("123456", "", "", "", "WEAK", ["COMMONLY_USED"]),
    ("000000", "", "", "", "WEAK", ["COMMONLY_USED"]),
    ("111111", "", "", "", "WEAK", ["COMMONLY_USED"]),
    ("654321", "", "", "", "WEAK", ["COMMONLY_USED"]),
    ("0201", "1998-01-02", "", "", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("0102", "", "1998-02-01", "", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
    ("020398", "", "", "1998-03-02", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("020198", "1998-01-02", "", "", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("9802", "1998-02-01", "", "", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("1998", "1998-01-02", "", "", "STRONG", []),
    ("5678", "", "", "", "STRONG", []),
    ("543210", "", "", "", "STRONG", []),
    ("020298", "1998-02-02", "", "", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("310799", "", "", "1999-07-31", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("020396", "", "", "1996-03-02", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("9901", "", "1999-01-01", "", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
    ("010203", "2003-01-02", "", "", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("101090", "", "", "1990-10-10", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("010190", "1990-01-01", "", "", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("010299", "", "1999-02-01", "", "WEAK", ["DEMOGRAPHIC_DOB_SPOUSE"]),
    ("310199", "", "", "1999-01-31", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("020199", "1999-01-02", "", "", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("1111a", "", "", "", "INVALID", ["INVALID_FORMAT"]),
    ("12", "", "", "", "INVALID", ["INVALID_FORMAT"]),
    ("abcdef", "", "", "", "INVALID", ["INVALID_FORMAT"]),
    ("", "", "", "", "INVALID", ["INVALID_FORMAT"]),
    ("12 34", "", "", "", "INVALID", ["INVALID_FORMAT"]),
    ("1@34", "", "", "", "INVALID", ["INVALID_FORMAT"]),
    ("", "1999-01-01", "1999-02-01", "1999-03-01", "INVALID", ["INVALID_FORMAT"]),
    ("4444", "2001-04-04", "", "", "STRONG", []),
    ("0404", "2001-04-04", "", "", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("140220", "2020-02-14", "", "", "WEAK", ["DEMOGRAPHIC_DOB_SELF"]),
    ("241298", "", "", "1998-12-24", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
    ("020498", "", "", "1998-04-02", "WEAK", ["DEMOGRAPHIC_ANNIVERSARY"]),
])
def test_mpin(mpin, dob_self, dob_spouse, anniv, expected_strength, expected_reasons):
    result = evaluate_mpin(mpin, dob_self, dob_spouse, anniv)
    assert result["strength"] == expected_strength
    assert set(result["reasons"]) == set(expected_reasons)
