# pip install PyJWT
import jwt

headers = {
    'alg': 'HS256',
    'type': 'JWT'
}

payload = {
    'username': 'tester_user',
    'email': 'tester@gmail.com',
    'is_active': False
}

secret = 'secret_1234'

encoded_token = jwt.encode(headers=headers, payload=payload, key=secret)
print(encoded_token)

try:
    decoded_token = jwt.decode(encoded_token, secret, algorithms=['HS256'])
    print(decoded_token)
except Exception as e:
    print(f'There is an error: {e}')



# to start server type in the shell: fastapi dev 16_lesson.py