from kamis.models.common import ResultCode


def test_result_code_succeeded():
    for code in ResultCode:
        if code in (ResultCode.SUCCESS, ResultCode.NO_DATA):
            assert code.succeeded is True
        else:
            assert code.succeeded is False
