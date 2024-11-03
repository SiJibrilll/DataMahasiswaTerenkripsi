import os

class View:
  def __init__(self) -> None:
    pass

  @staticmethod # -- dash styling
  def dash():
    print('------------------')
  
  @staticmethod # ---- header method
  def header():
    print('==========================')
    print('\n         SISTEM         ')
    print('DATA MAHASISWA TERENKRIPSI         \n')
    print('==========================\n')

  
  @staticmethod # ----- new page method
  def newPage(title : str):
    os.system('clear')
    View.header()
    print(title)
    View.dash()
  
  @staticmethod # ----- ordered list method
  def orderedList(*item):
    for i in range(len(item)):
      print(f'{i+1}. {item[i]}')

  @staticmethod # ----- ordered list method
  def unorderedList(*item):
    for i in item:
      print(i)
      
    
