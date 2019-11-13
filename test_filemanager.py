import bank_func
import victory_func


def test_account_inc():
    assert bank_func.account_inc([0, 0, 0], 1000) == [1000, 0, 0]


def test_buy_operation():
    assert bank_func.buy_operation([1000, [], []], 'еда', 100) == [900, ['еда'], [100]]
    assert bank_func.buy_operation([100, [], []], 'еда', 1000) == [100, [], []]


def test_transformation_date():
    assert victory_func.trasformation_date('01','01','2001')== 'первого января 2001 года'
    assert victory_func.trasformation_date('15', '11', '2019') == 'пятнадцатого ноября 2019 года'


