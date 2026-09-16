from src.extract import Extract
from src.load import Load

ext = Extract()
data = ext.pnadc()

ld = Load()
ld.insert_in_mongo(data, "IBGE", "pnadc")
