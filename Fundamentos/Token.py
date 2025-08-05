import secrets

# Gerar um token URL-safe de 16 bytes
token = secrets.token_urlsafe(16)

# Exemplo de link de redefinição de senha
reset_link = f"http://example.com/reset-senha/{token}"

print(reset_link)
