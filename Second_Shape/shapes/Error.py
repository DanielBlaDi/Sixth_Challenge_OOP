class UserError(Exception):
  """
  Exeption that appear when the user enter the same vertex many times

  Args:
    message: You use the same vertex more than 1 time
  """

  def __init__(self, message):
    super().__init__(message)