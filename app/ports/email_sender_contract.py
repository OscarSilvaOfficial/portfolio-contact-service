from abc import ABC, abstractmethod

class EmailSenderContract(ABC):
  
  @abstractmethod
  def send(self, subject, message):
    raise NotImplementedError()
    