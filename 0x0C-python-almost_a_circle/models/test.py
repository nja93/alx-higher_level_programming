ass Base:
    """
    class base created, private class attribute initialized to 0

    """
        __nb_objects = 0

            def __init__(self, id = None);

                    if id != None:
                                    self.id = id

                                            else:
                                                            Base.__nb_objects += 1
                                                                        self.id = self.__nb_objects
                                                                        ~                                         
