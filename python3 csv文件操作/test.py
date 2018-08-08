import csv

class csvOperat():
	"""docstring for csv"""
	def __init__(self):
		pass
		
	def createAndWrite(self,fileName,rowHeader,rowData=[]):

		csvFile = open(fileName,'w')
		writer  = csv.writer(csvFile)
		writer.writerow(rowHeader)
		if len(rowData) > 0:
			writer.writerows(rowData)
		csvFile.close()

def main():
	newCSV = csvOperat()
	header = ['id','name','content']
	data   = [
		('1','CcphAmy','Oh'),
		('2','CcphAmy','shit'),
		('3','CcphAmy','success')
	]
	newCSV.create('test.csv',header,data)
if __name__ == '__main__':
	main()