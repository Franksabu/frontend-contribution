import random

import datetime


class random_reference:
    @staticmethod
    def new_numero(prefixe=None):

        reference = ""
        if prefixe:
            # Générer un nombre aléatoire entre 1000 et 9999
            reference = f'{prefixe}-{datetime.datetime.now().year}-{datetime.datetime.now().month}-'
           
        else:
            reference = f'{datetime.datetime.now().year}{datetime.datetime.now().month}'

        reference += str(random.randint(1000, 9999))

        return reference
