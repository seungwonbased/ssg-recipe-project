import locale

locale.setlocale(locale.LC_ALL, "")


# datetime 객체를 문자열로 만들어주는 Template Filter
def format_datetime(value, fmt="%Y년 %m월 %d일 %p %I:%M"):
    return value.strftime(fmt)
