class SaveContactException(Exception):
  def __init__(self, message="Erro ao salvar contato"):
    super(SaveContactException, self).__init__(message)