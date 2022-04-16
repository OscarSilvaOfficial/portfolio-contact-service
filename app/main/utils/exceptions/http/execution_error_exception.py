from fastapi import HTTPException


class ExecutionErrorException(HTTPException):
  
  def __init__(self, message):
    super(ExecutionErrorException, self).__init__(status_code=500, detail=message)