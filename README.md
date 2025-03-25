# 🔐 Verificador de Senhas Seguras  

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)  
Um verificador de senhas que analisa a força da senha com base em critérios de segurança e impede o uso de sequências previsíveis.  

---

## 📜 Requisitos de Segurança  
O script verifica se a senha atende aos seguintes critérios:  
✔️ Pelo menos **10 caracteres**  
✔️ Pelo menos **uma letra maiúscula (A-Z)**  
✔️ Pelo menos **uma letra minúscula (a-z)**  
✔️ Pelo menos **um número (0-9)**  
✔️ Pelo menos **um caractere especial (!@#$%^&* etc.)**  
✔️ **Não pode conter padrões comuns ou sequências previsíveis** (exemplo: `"12345"`, `"senha123"`, `"qwerty"`, etc.)  

---

## 🚀 Como Usar  
### 📥 Clonar o repositório  

git clone https://github.com/juanpolido/verificador-senha
cd verificador-senha

2️⃣ Executar o script
Certifique-se de ter o Python instalado e execute o arquivo:

python verificador_senha.py

🛠 Estrutura do Projeto
verificador-senha/
│── verificador_senha.py  # Código principal do verificador
│── README.md             # Documentação do projeto

🔥 Exemplo de Uso

❌ Senha fraca

Digite uma senha: Pass@123
A senha deve ter pelo menos 10 caracteres.

✅ Senha forte

Digite uma senha: SenhaSuperForte@2024
Senha forte!

🤝 Contribuindo
Contribuições são bem-vindas! Se quiser sugerir melhorias:

Fork o repositório

Crie uma branch com sua melhoria (git checkout -b minha-melhoria)

Faça um commit (git commit -m "Melhoria na validação de senha")

Faça um push para a branch (git push origin minha-melhoria)

Abra um Pull Request

📜 Licença
Este projeto está sob a licença MIT.

