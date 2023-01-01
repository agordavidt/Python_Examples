zip_code = '1234x'
res = []
for i in zip_code:
    if i.isdigit():
        res.append(i)
if len(res) == 5:
    print(True)
else:
    print(False)