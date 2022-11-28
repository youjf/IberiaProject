import softest
import csv

from tests.buscar_vuelos import BuscarVuelosTest


class Read_File(softest.TestCase):

     def read_data_from_csv(fileName):
        datalist = []
        csvData = open(fileName, "r")
        dataReader = csv.reader(csvData)
        next(dataReader)
        for rows in dataReader:
            datalist.append(rows)
        return datalist