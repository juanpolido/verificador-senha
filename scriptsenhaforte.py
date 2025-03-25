import re

sequencias_proibidas = [
    "12345", "abcdef", "qwerty", "password", "senha", "09876", "qazwsx",
    "123456", "654321", "abc123", "pass123", "admin", "letmein", "welcome",
    "123456789", "987654321", "111111", "222222", "333333", "123123", "112233", "123321", "13579", "24680",
    "qwertyuiop", "asdfghjkl", "zxcvbnm", "poiuytrewq", "lkjhgfdsa", "mnbvcxz", "abcdefgh", "ijklmnop", "uvwxyz",
    "senha1", "admin123", "letmein", "welcome123", "test123", "user123", "root123", "login123", "pass1234",
    "senha123",
    "qwerty123", "abcd1234", "euteamo", "leao", "dragao", "arcoiris", "futebol", "sombra", "batman",
    "1990", "2000", "2010", "2023", "2024", "1999", "1987", "7777777", "88888888", "99999999"
]


def verificar_senha(senha):
    erros = []

    if len(senha) < 10:
        erros.append(" A senha NÃO possui a quantidade mínima de 10 caracteres!")

    if not re.search(r"[A-Z]", senha):
        erros.append("A senha não possui letras maiúsculas!")

    if not re.search(r"[a-z]", senha):
        erros.append("A senha não possui letras minúsculas!")

    if not re.search(r"\d", senha):
        erros.append("A senha não possui números!")

    if not re.search(r"[^A-Za-z0-9]", senha):
        erros.append("A senha não possui símbolos!")

    for seq in sequencias_proibidas:
        if seq in senha.lower():
            erros.append(f"A senha contém a sequência proibida: '{seq}'. Escolha algo menos previsível.")

    if erros:
        return "\n".join(erros)

    return "Senha forte!"


senha_teste = input("Digite uma senha: ")
print(verificar_senha(senha_teste))


