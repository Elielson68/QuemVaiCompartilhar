from datetime import datetime

class ShareToday:

  def __init__(self, names):
    self.today = datetime.today().minute
    self.names = names
    self.index = 0
    self.pending_workers = []
    self.use_pending_worker = False
    self.worker = self.names[self.index]
    self.last_pending_removed = None

  def WhoShareToday(self, jump=False):
    day_changed = self.today != datetime.today().minute
    self.today = datetime.today().minute
    is_pending_workers = len(self.pending_workers) > 0

    if jump:
      if self.last_pending_removed == self.worker:
        self.pending_workers.insert(0, self.worker)
      else:
        self.pending_workers.append(self.worker)
      self.index = (self.index + 1) % len(self.names)
      self.worker = self.names[self.index]
      return self.worker
      
    elif day_changed and is_pending_workers:
      self.worker = self.last_pending_removed = self.pending_workers.pop(0)

    elif day_changed:
      self.index = (self.index + 1) % len(self.names)
      self.worker = self.names[self.index]
    
    return self.worker



  def PendingWorkers(self):
    return self.pending_workers