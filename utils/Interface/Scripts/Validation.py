from PyQt6.QtWidgets import QLineEdit
from icecream import ic

class DataValidation():
    allowed = {"string": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%$/=+*°-_., áÁéÉíÍóÓúÚüñÑçÇäëïöü",
                "int": "1234567890",
                "float": "1234567890."}

    def validateData(self, data: tuple[QLineEdit, str]) -> tuple[bool, str]:
        if not self.valEmptySpaces(data[0].text()):
            return False, "Espacio Vacío en"
        
        if not self.validateCharacters(data[0].text(), self.allowed[data[1]]):
            return False, "Carácter Inválido en"
        
        return True, ""

    def valEmptySpaces(self, data: str) -> bool:
        return bool(len(data))
    
    def validateCharacters(self, data: str, tipo: str) -> bool:
        return not ("<" in data or ">" in data) and all(caracter in tipo for caracter in data)
    
validate = DataValidation()
if __name__ == '__main__':
    ic(validate.validateCharacters("fsdg", validate.stringAllowed))