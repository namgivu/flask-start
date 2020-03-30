def torr(
    #param               #param type             #default param value
    expected_condition : 'boolean expression',
    error_message      : str                     = 'We must have :expected_condition true to continue',
    ExceptionType      : 'python exception type' = Exception,  # use Exception if no specific exception type defined
):
    """
    this is similar to
    01 if not expected_condition: raise Exception(error_message)
    02 assert expected_condition, error_message
    """
    if not expected_condition:
        raise ExceptionType(error_message)
