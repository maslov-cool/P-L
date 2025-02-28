import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--per-day', action="store", dest="per_day", default=False, type=str)
parser.add_argument('--per-week', action="store", dest="per_week", default=False, type=str)
parser.add_argument('--per-month', action="store", dest="per_month", default=False, type=str)
parser.add_argument('--per-year', action="store", dest="per_year", default=False, type=str)
parser.add_argument('--get-by', action="store", dest="get_by", default=False, type=str,
                    choices=['day', 'month', 'year'])

args = parser.parse_args()
income, expense = 0, 0

if args.per_day:
    if '-' in args.per_day:
        expense += float(args.per_day)
    else:
        income += float(args.per_day)

if args.per_week:
    if '-' in args.per_week:
        expense += float(args.per_week) / 7
    else:
        income += float(args.per_week) / 7

if args.per_month:
    if '-' in args.per_month:
        expense += float(args.per_month) / 30
    else:
        income += float(args.per_month) / 30

if args.per_year:
    if '-' in args.per_year:
        expense += float(args.per_year) / 360
    else:
        income += float(args.per_year) / 360

if args.get_by:
    if args.get_by == 'day':
        print(int(income + expense))
    elif args.get_by == 'month':
        print(int(30 * (income + expense)))
    elif args.get_by == 'year':
        print(int(360 * (income + expense)))
else:
    print(int(income + expense))
