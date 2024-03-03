import datetime


class Datas:
    def datas(self, *args):
        date1 = datetime.datetime.strptime(args[0], "%d/%m/%Y")
        date1 = datetime.date(date1.year, date1.month, date1.day)

        date2 = datetime.datetime.strptime(args[1], "%d/%m/%Y")
        date2 = datetime.date(date2.year, date2.month, date2.day)

        if date2 > date1:
            return (date2-date1).days
        else:
            return (date1-date2).days
