from Controller import Controller

def main():
  state = '0'
  control = Controller()
  
  while True: # ===================== state machine ======================
    control.main() # show the main menu
      
    state = input('Pilih menu: ') # select action

    if not state.isnumeric(): # validation : must be numeric
      state = 0
      continue

    if int(state) < 1 or int(state) > 8: # default to main menu
      state = '0' 
      continue

    # ------------------------ states ---------------------------------
    if state == '1': # ====== main menu state
      control.createMahasiswa()

    if state == '2': # ====== display encrypted data
      control.listMahasiswa()

    if state == '3': # =========== display non encrypted data
      control.listMahasiswa(False)

    if state == '4': # ============ find mahasiswa
      control.findMahasiswaByName()

    if state == '5': # ============= average score
      control.rataRataNilai()

    if state == '6': # ============= mahasiswa that graduates
      control.mahasiswaLulus()

    if state == '7':
      control.tertuaTermuda()

    if state == '8':
      control.exit()
      

main()