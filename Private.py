class Private():
    def __init__(self):
        self._private_attribute = "Valor"

class Real_Private():
    def __init__(self):
        self.__real_private_attribute = "Valor privado"

private = Private()
real_private = Real_Private()
print(private._private_attribute)
print(real_private.__real_private_attribute)