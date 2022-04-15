from abc import ABC, abstractmethod

class DBContract(ABC):
  
  @abstractmethod
  def create(self):
    raise NotImplementedError()