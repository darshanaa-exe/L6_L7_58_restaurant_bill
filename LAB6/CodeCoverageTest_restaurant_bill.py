import pytest
from restaurant_bill import bill_total, split_bill, table_wait


# ---------- bill_total ----------
def test_dine_in_bill():
    assert bill_total("dine_in", 1000, 2, False) == 1155

def test_unknown_section():
    with pytest.raises(ValueError):
        bill_total("balcony", 1000, 2, False)

def test_negative_food_total():
    with pytest.raises(ValueError):
        bill_total("dine_in", -1, 2, False)

def test_zero_guests():
    with pytest.raises(ValueError):
        bill_total("dine_in", 1000, 0, False)

def test_happy_hour_discount():
    assert bill_total("dine_in", 1000, 2, True) == 924

def test_large_group_surcharge():
    assert bill_total("rooftop", 1000, 8, False) == 1417


# ---------- split_bill ----------
def test_even_split():
    assert split_bill(1000, 4, 10) == 275

def test_split_rounds_up():
    assert split_bill(1000, 3, 0) == 334

def test_split_zero_people():
    with pytest.raises(ValueError):
        split_bill(1000, 0, 10)

def test_split_negative_tip():
    with pytest.raises(ValueError):
        split_bill(1000, 4, -5)


# ---------- table_wait ----------
def test_party_too_large():
    assert table_wait(13, 5, False) == "call ahead"

def test_reservation_seats_now():
    assert table_wait(4, 0, True) == "seat now"

def test_no_free_tables():
    assert table_wait(4, 0, False) == "waitlist"

def test_big_party_one_table():
    assert table_wait(8, 1, False) == "waitlist"

def test_small_party_seated():
    assert table_wait(2, 3, False) == "seat now"
