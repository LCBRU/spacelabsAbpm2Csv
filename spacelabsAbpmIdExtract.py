#!/usr/bin/python3

import csv, sys, argparse, os

COLUMN_PATIENT_LAB_ID = 'ID'
COLUMN_DATE_RECORDED = 'DateRecorded'
COLUMN_FILENAME = 'Filename'

def main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument("-o", "--outputfilename", required=True, help="Output filename")
  parser.add_argument('directory')
  args = parser.parse_args()

  with open(args.outputfilename, 'w') as csvfile:
    fieldnames = [
      COLUMN_PATIENT_LAB_ID,
      COLUMN_DATE_RECORDED,
      COLUMN_FILENAME]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for root, dirs, files in os.walk(args.directory, topdown=False):
      for name in files:
        if (name.endswith('TXR')):
          readCsv(os.path.join(root, name), writer)

def readCsv(filename, output):
  print('Processing: ', filename)

  with open(filename, 'r', encoding='utf16') as csvfile:
    patientLabId = None
    dateRecorded = None

    for row in csv.reader(csvfile, delimiter=','):
      if row[0][0:3] == 'ID:':
          patientLabId = row[0][3:].strip()

      if row[0][0:7] == 'Hookup:':
          dateRecorded = row[0][7:].strip()

      if row[0] == '#':
        if patientLabId is None:
          raise Exception('Patient Lab ID not found')

        if dateRecorded is None:
          raise Exception('Date Recorded not found')

        output.writerow({
          COLUMN_PATIENT_LAB_ID : patientLabId,
          COLUMN_DATE_RECORDED : dateRecorded,
          COLUMN_FILENAME : filename
          })

        break;

if __name__ == "__main__":
   main(sys.argv[1:])

