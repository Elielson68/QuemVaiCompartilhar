from datetime import datetime

SATURDAY = 5
SUNDAY = 6

class ShareToday:

  def __init__(self, names, index=0):
    self.today = self.GetToday()
    self.names = names
    self.index = index
    self.pending_workers = []
    self.use_pending_worker = False
    self.worker = self.names[self.index]
    self.last_pending_removed = None
    self.freeze_worker = False

  def WhoShareToday(self, jump=False):

    if self.WeekDay() in (SATURDAY, SUNDAY):
      print("É sábado ou domingo, não troca de pessoa hoje!", self.WeekDay(), " Trabalhador selecinado: ", self.worker)
      return self.worker

    day_changed = self.today != self.GetToday()
    self.today = self.GetToday()
    is_pending_workers = len(self.pending_workers) > 0

    if day_changed and self.freeze_worker:
      print("Trabalhador congelado! Trabalhador selecinado: ", self.worker)
      self.freeze_worker = False
      return self.worker

    if jump:
      if self.last_pending_removed == self.worker:
        self.pending_workers.insert(0, self.worker)
      else:
        self.pending_workers.append(self.worker)
      self.index = (self.index + 1) % len(self.names)
      self.worker = self.names[self.index]
      self.SaveIndex()
      print("Pulou a vez. Trabalhador selecinado: ", self.worker)
      return self.worker
      
    elif day_changed and is_pending_workers:
      self.worker = self.last_pending_removed = self.pending_workers.pop(0)
      print("Dia alterou e tem pendente. Trabalhador selecinado: ", self.worker)

    elif day_changed:
      self.index = (self.index + 1) % len(self.names)
      self.worker = self.names[self.index]
      self.SaveIndex()
      print("Dia alterou. Trabalhador selecinado: ", self.worker)

    print("Nada mudou. Trabalhador selecinado: ", self.worker)
    return self.worker



  def PendingWorkers(self):
    return self.pending_workers

  def Reset(self):
    self.index = 0

  def WeekDay(self):
    return datetime.today().weekday()

  def GetToday(self):
    return datetime.today().day

  def RequestPause(self):
    self.freeze_worker = True

  def IsPaused(self):
    return self.freeze_worker

  def SaveIndex(self):
    with open("share_data", "w") as file:
        file.write(str(self.index))
