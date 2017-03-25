import csv
import json

def run():
    with open('data.csv', 'r', newline='') as datafile, \
        open('template.html', 'r') as htmlfile, \
        open('index.html', 'w') as resultfile:
        data_reader = csv.reader(datafile, delimiter=',')
        data = list(row for row in data_reader if row)
        for i in range(1, len(data)):
            data[i][3] = float(data[i][3])
            data[i][4] = float(data[i][4])
        html = htmlfile.read()
        rendered = html.replace('<datafile>', json.dumps(data))
        resultfile.write(rendered)


if __name__ == '__main__':
    run()
