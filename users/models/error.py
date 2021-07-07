class Error():

    def __init__(self, error):
        self.error = error

    def getError(self):
        """ Método de retorno de error. """
        return [
            {
                'response': None,
                'error': str(self.error)
            }
        ]
