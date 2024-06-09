import csv
# with open('C:/Disks/Desktop18_09_22/NewPythonPresentation/Topic_14/file/csv/email.csv', encoding="utf-8") as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#     for index, row in enumerate(reader, 1):
#         if index > 3:
#             break
#         print(row)

################################################
with open('C:/Disks/Desktop18_09_22/NewPythonPresentation/Topic_14/file/csv/email.csv', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    expensive = sorted(reader, key=lambda x: int(x['Identifier']), reverse=True)
    for record in expensive[:10]:
        print(record)