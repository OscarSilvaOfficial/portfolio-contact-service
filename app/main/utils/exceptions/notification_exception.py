class NotificationException(Exception):
  def __init__(self, message="Erro ao notificar o usuário"):
    super(NotificationException, self).__init__(message)