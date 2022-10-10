import csv

def csvToDictByLine(filePath: str) -> list :
  FinalArray = []
  with open(filePath, 'r', encoding='utf8', newline='') as file :
    reader = csv.DictReader(file, delimiter=";")
    for line in reader :
      FinalArray.append(line)
  return FinalArray
