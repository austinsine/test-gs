import gspread

gc = gspread.service_account()

sh = gc.open("test")

print(sh.sheet1.get('A1'))
