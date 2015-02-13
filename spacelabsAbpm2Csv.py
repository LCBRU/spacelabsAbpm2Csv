#!/usr/bin/python3

import csv, sys, argparse

COLUMN_DATE_RECORDED = 'Date recorded (Staff)'
COLUMN_PATIENT_LAB_ID = 'Rec'
COLUMN_DAY = 'Day'
COLUMN_MONTH = 'Month'
COLUMN_YEAR = 'Year'
COLUMN_HOUR = 'Time (Hour)'
COLUMN_MINUTES = 'Time (Minutes)'
COLUMN_SYSTOLIC = 'Systolic'
COLUMN_DIASTOLIC = 'Diastolic'
COLUMN_MAP = 'MAP'
COLUMN_PP = 'PP'
COLUMN_HR = 'Heart Rate (HR)'
COLUMN_ECODE = 'Ecode'
COLUMN_ESTATUS = 'Estatus'
COLUMN_DIARY = 'Diary'
COLUMN_MEAN_24HOUR_SBP = 'Mean 24 hour SBP'
COLUMN_MEAN_24HOUR_DBP = 'Mean 24 hour DBP'
COLUMN_MEAN_DAYTIME_SBP = 'Mean daytime SBP'
COLUMN_MEAN_NIGHTIME_SBP = 'Mean nightime SBP'
COLUMN_MEAN_DAYTIME_DBP = 'Mean daytime DBP'
COLUMN_MEAN_NIGHTIME_DBP = 'Mean nightime DBP'

def main(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument("-o", "--outputfilename", required=True, help="Output filename")
  parser.add_argument('files', nargs=argparse.REMAINDER)
  args = parser.parse_args()

  with open(args.outputfilename, 'w') as csvfile:
    fieldnames = [
      COLUMN_DATE_RECORDED,
      COLUMN_PATIENT_LAB_ID,
      COLUMN_DAY,
      COLUMN_MONTH,
      COLUMN_YEAR,
      COLUMN_HOUR,
      COLUMN_MINUTES,
      COLUMN_SYSTOLIC,
      COLUMN_DIASTOLIC,
      COLUMN_MAP,
      COLUMN_PP,
      COLUMN_HR,
      COLUMN_ECODE,
      COLUMN_ESTATUS,
      COLUMN_DIARY,
      COLUMN_MEAN_24HOUR_SBP,
      COLUMN_MEAN_24HOUR_DBP,
      COLUMN_MEAN_DAYTIME_SBP,
      COLUMN_MEAN_NIGHTIME_SBP,
      COLUMN_MEAN_DAYTIME_DBP,
      COLUMN_MEAN_NIGHTIME_DBP]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for arg in args.files:
      readCsv(arg, writer)

def readCsv(filename, output):
  print('Processing: ', filename)

  with open(filename, 'r', encoding='utf16') as csvfile:
    inMainLoop = False
    patientLabId = None
    dateRecorded = None

    for row in csv.reader(csvfile, delimiter=','):
      if inMainLoop:
        output.writerow({
          COLUMN_DATE_RECORDED : dateRecorded,
          COLUMN_PATIENT_LAB_ID : patientLabId,
          COLUMN_DAY : row[3].strip(),
          COLUMN_MONTH : row[2].strip(),
          COLUMN_YEAR : row[4].strip(),
          COLUMN_HOUR : row[5].strip(),
          COLUMN_MINUTES : row[6].strip(),
          COLUMN_SYSTOLIC : row[7].strip(),
          COLUMN_DIASTOLIC : row[8].strip(),
          COLUMN_MAP : row[9].strip(),
          COLUMN_PP : row[10].strip(),
          COLUMN_HR : row[11].strip(),
          COLUMN_ECODE : row[12].strip(),
          COLUMN_ESTATUS : row[13].strip(),
          COLUMN_DIARY : row[14].strip(),
          COLUMN_MEAN_24HOUR_SBP : '',
          COLUMN_MEAN_24HOUR_DBP : '',
          COLUMN_MEAN_DAYTIME_SBP : '',
          COLUMN_MEAN_NIGHTIME_SBP : '',
          COLUMN_MEAN_DAYTIME_DBP : '',
          COLUMN_MEAN_NIGHTIME_DBP : ''
          })
      else:

        if row[0][0:3] == 'ID:':
            patientLabId = row[0][3:].strip()

        if row[0][0:7] == 'Hookup:':
            dateRecorded = row[0][7:].strip()

        if row[0] == '#':
          inMainLoop = True

          if patientLabId is None:
            raise Exception('Patient Lab ID not found')

          if dateRecorded is None:
            raise Exception('Date Recorded not found')

if __name__ == "__main__":
   main(sys.argv[1:])

