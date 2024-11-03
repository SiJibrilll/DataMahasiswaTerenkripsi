from View import View
from Mahasiswa import Mahasiswa
mahasiswa = Mahasiswa()

class Controller:
  def __init__(self) -> None:
    pass

  def main(self): # ----- main menu
    View.newPage('Menu utama')
    View.orderedList(
      'Tambah data mahasiswa',
      'Tampilkan data mahasiswa (Terenkripsi)',
      'Tampilkan nama asli mahasiswa',
      'Cari mahasiswa bedasarkan nama',
      'hitung rata-rata nilai mahasiswa',
      'Tampilkan mahasiswa yang lulus',
      'Tampilkan mahasiswa tertua dan termuda',
      'Keluar'
    )
    View.dash()

  
  def createMahasiswa(self): # ---- create mahasiswa
    over = False
    error = None
    data = {}
    while not over: # -- sebelum data valid, tak akan berhenti
      View.newPage(f'Menu tambah data mahasiswa {error if error is not None else ""}')
      
      nama = input('Masukan nama: ')
      nilai = input('Masukan umur: ')
      umur = input('Masukan nilai rata-rata: ')
      
      output = mahasiswa.create(nama, nilai, umur)
      
      if output[0] is not None: # -- jika terjadi error maka ulangi operasi
        error = '\n' + output[0]
        continue
      data = output[1]
      over = True

    
    View.newPage('Mahasiswa berhasil ditambahkan')
    View.unorderedList(
      'Nama: ' + str(data['nama']),
      'Umur: ' + str(data['umur']),
      'Nilai rata-rata: ' + str(data['nilai'])
    )
    
    View.dash()
    View.orderedList(
      'Tambahkan mahasiswa lagi',
      'Kembali'
    )
    View.dash()
    aksi = input('Pilih aksi: ')
    if aksi == '1':
      self.createMahasiswa()
    
      
  
  def listMahasiswa(self, encrypted = True):
    View.newPage(f'Menu Daftar mahasiswa {"(Terenkripsi)" if encrypted else""}')
    mahasiswaList = mahasiswa.all(encrypted)
    if len(mahasiswaList) > 0:
      View.unorderedList(*[f'Nama {"terenkripsi" if encrypted else ""}: {x["nama"]} Umur: {x["umur"]} Nilai: {x["nilai"]}' for x in mahasiswaList])
    else:
      print('Belum ada data')
    View.dash()
    input('Tekan enter untuk kembali')

  def findMahasiswaByName(self):
    View.newPage('Menu cari mahasiswa bedasarkan nama')
    nama = input("Masukan nama untuk dicari: ")
    result = mahasiswa.find('nama', nama) 
    View.newPage('Menu cari mahasiswa bedasarkan nama')
    if result is not None:
      print('Hasil pencarian: ')
      print(f'Nama: {result["nama"]} Umur: {result["umur"]} Nilai: {result["nilai"]}')
    else:
      print(f'Tidak ditemukan mahasiswa bernama "{nama}"')
    print('\nLakukan pencarian lagi?')
    View.orderedList('ya', 'kembali')
    View.dash()
    aksi = input('Pilih aksi: ')
    if aksi == '1':
      self.findMahasiswaByName()

  def rataRataNilai(self):
    mahasiswaList = mahasiswa.query()

    nilai = [data['nilai'] for data in mahasiswaList]
    rataRata = sum(nilai) / len(mahasiswaList)

    View.newPage("Menu rata-rata nilai mahasiswa")
    print(f'Rata-rata nilai seluruh mahasiswa: {rataRata}')
    View.dash()
    input('Tekan enter untuk kembali')

  def mahasiswaLulus(self):
    View.newPage('Menu mahasiswa yang lulus (nama terenkripsi)')
    result = mahasiswa.where('nilai', '>=', 70)
    if len(result) > 0:
      for i in result:
        print(i['nama'], end=' ')
      print()
    else:
      print('Tidak ada mahasiswa yang lulus')
    View.dash()
    input('Tekan enter untuk kembali')

  def tertuaTermuda(self):
    mahasiswaList = mahasiswa.all()

    View.newPage('Menu mahasiswa tertua dan termuda')
    
    if len(mahasiswaList) > 0:
      termuda = min(mahasiswaList, key=lambda x:x['umur'])
      tertua = max(mahasiswaList, key=lambda x:x['umur'])
      
      print(f'Mahasiswa termuda (nama terenkripsi): {termuda["nama"]}')
      print(f'Mahasiswa tertua (nama terenkripsi): {tertua["nama"]}')
    else:
      print('Belum ada mahasiswa')

    View.dash()
    input('Tekan enter untuk melanjutkan')

  def exit(self):
    View.newPage('Sampai jumpa !')
    exit()