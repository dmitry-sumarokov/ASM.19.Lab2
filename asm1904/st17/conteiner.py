from animals import Animal, Dog, Cat, Hamster, HamsterBehavior, CatBehavior, DogBehavior, Display
from flask import render_template, request
import pickle
import os

class Container:

  def __init__(self):
    try:
      self.read()
    except:
      self.Mypets =[] 
  
  def newAnimal(self, id):
    List=dict(name = '', age = '',  gender = '')
    List['id']=id
    return render_template("form_New.tpl", **List)

  def add_newAnimal(self):
    Menu = [self.add_Cat, self.add_Dog, self.add_Hamster]
    id = int(request.form.get('id', 0))
    Menu[id]()
    return self.printlist()

  def add_Cat(self):
    newcat = Cat()
    newcat.put()
    self.Mypets.append(newcat)
    #print ('Объект записан')

  def add_Dog(self):
    newdog = Dog()
    newdog.put()
    self.Mypets.append(newdog)
    #print ('Объект записан')

  def add_Hamster(self):
    newhamster = Hamster()
    newhamster.put()
    self.Mypets.append(newhamster)
    #print ('Объект записан')  

  def printlist(self):
    u = ""
    for (i, item) in enumerate(self.Mypets):
      u += item.output(i, "item.tpl")
    u += render_template("add.tpl")
    return u


  def clearlist(self):
    self.Mypets.clear()
    return(self.printlist())

  def remove_elem(self, id):
    self.Mypets.pop(int(id))
    return self.printlist()
    """print('Номер элемента?')
    number=int(input())
    if (number <= len(self.list)):
      del self.list[number-1]
      print('Элемент удален успешно')  
    else:
      print('Элемент уже удален или еще не добавлен')
      print('Выберите 4 пункт меню для просмотра')"""  

  def update_form(self, id):
    return self.Mypets[id].output(id, "form_Update.tpl")

  def edit_elem(self):
    id = int(request.form.get('id', 0))
    self.Mypets[id].put()
    return self.printlist()
    """print('Номер элемента?')
    number=int(input())
    if (number <= len(self.list)):
        self.list[number-1].put()
    else:
      print('Нет такого элемента:( ')
      print('Выберите 4 пункт меню для просмотра')
              
  def recording(self):
    with open('outfile.dat','wb') as fp:
      pickle.dump(self.Mypets,fp)
            #print('Записано!')

  def read(self):
    with open ('outfile.dat', 'rb') as fp:
      self.Mypets.extend(pickle.load(fp)) """ 
            #print('Считано!')
  
  def recording(self):
    with open(os.path.join(os.path.abspath(__name__).replace('\conteiner', '\\'), 'pets.p'), 'wb') as f:
      pickle.dump(self.Mypets, f)
        
  def read(self):
    with open(os.path.join(os.path.abspath(__name__).replace('\conteiner', '\\'), 'pets.p'), 'rb') as f:
      self.Mypets = pickle.load(f)
            

  def different(self, id):
    return(self.Mypets[id].different() + self.printlist())
  
  def PrintHeader(self):
    return render_template("header.tpl")

  def PrintFooter(self):
    return render_template("footer.tpl")
    
          

    
