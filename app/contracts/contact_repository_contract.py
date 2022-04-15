from abc import ABC, abstractmethod

class ContactRepositoryContract(ABC):
  
    @abstractmethod
    def save(self, contact):
      raise NotImplementedError()