import operator

class Mahasiswa:
  def __init__(self) -> None:
    self.db = []
    self.alphabetTable = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  def encrypt(self, data:str): # -- encrypt data
    data = data.lower()
    data = list(data)
    for letter in data:
      index = self.alphabetTable.index(letter) + 3
      data[data.index(letter)] = self.alphabetTable[index if index <= len(self.alphabetTable) - 1 else index - len(self.alphabetTable)]    
    return ''.join(data)

  def decrypt(self, data:str): # -- decrypt data
    data = data.lower()
    data = list(data)
    for letter in data:
      index = self.alphabetTable.index(letter) - 3
      data[data.index(letter)] = self.alphabetTable[index if index >= 0 else len(self.alphabetTable) + index]

    return ''.join(data)

  def validate(self, nama, umur, nilai): # -- validator
    if not umur.isnumeric():
      return ['ERROR : Umur harus berupa angka']

    if not nilai.isnumeric():
      return ['ERROR : Nilai harus berupa angka']

    return [None, {'nama':nama, 'umur':umur, 'nilai':nilai}]

  def create(self, nama, umur, nilai): # -- create value to database
    validation = self.validate(nama, umur, nilai)
    
    if validation[0] is not None:
      return [validation[0]]

   
    mahasiswa = {'nama':self.encrypt(validation[1]['nama']), 'umur':int(validation[1]['umur']),'nilai':int(validation[1]['nilai'])}
    
    self.db.append(mahasiswa)
    
    return [None, {'nama':self.decrypt(mahasiswa['nama']), 'umur':mahasiswa['umur'], 'nilai': mahasiswa['nilai']}]


  def query(self): # -- query data
    return self.db

  def all(self, encrypted = True): # -- grab all data
    mahasiswaList = self.query()
    if encrypted:
      return mahasiswaList

    for i in range(len(mahasiswaList)):
      mahasiswaList[i]['nama'] = self.decrypt(mahasiswaList[i]['nama'])

    return mahasiswaList

  def find(self, collumn, search):
    mahasiswaList = self.all(False)
    searched = [x for x in mahasiswaList if x[collumn] == search] 
    return None if len(searched) < 1 else searched[0]

  def where(self, collumn, op, filter):
    ops = {
      '==': operator.eq,
      '!=': operator.ne,
      '>': operator.gt,
      '<': operator.lt,
      '>=': operator.ge,
      '<=': operator.le
    }
    query = self.query()
    return [x for x in query if ops[op](x[collumn], filter)]
    