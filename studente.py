import pickle
import datetime
from enum import Enum


class Class(Enum):
    QUARTA_F_INF = 1
    QUARTA_A_MEC = 2


class Studente:
    IMMUNITY_DAYS = 1

    def __init__(self, name: str, surname: str, classe: Class):
        self.name: str = name
        self.surname: str = surname
        self.classe: Class = classe
        self.last_extracted_date: datetime = datetime.datetime.now() - datetime.timedelta(days=7)
        self.path = "UNSAVED"

    def save(self):
        classe = "quarta_f_inf" if self.classe == Class.QUARTA_F_INF else "quarta_a_mec"
        with open(f"classi/{classe}/{self.surname}@{self.name}.st", "wb") as outfile:
            pickle.dump(self, outfile)
            self.path = f"classi/{classe}/{self.surname}@{self.name}.st"
            outfile.close()

    def is_immune(self) -> bool:
        # Se l'ultima volta che lo studente è stato estratto più un giorno è piu grande della data di adesso
        # allora lo studente è immune, altrimenti può essere estratto
        return self.last_extracted_date + datetime.timedelta(days=self.IMMUNITY_DAYS) > datetime.datetime.now()


def load_student(path) -> Studente:
    return pickle.load(open(path, "rb"))
