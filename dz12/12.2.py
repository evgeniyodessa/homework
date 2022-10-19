# Дано два словаря
# Необходимо написать код который будет их объединять
# Но нужно так-же учитывать коллизии, например ситуация когда у нас два одинаковых ключа и чтобы
# не потерять значения нужно записать в один ключ список в котором будут находится значения
# Записать результат в файл result.json в формате JSON.

import json

good_crypto = {
    'coin': 'btc',
    'ath': '69000'
}
bad_crypto = {
    'coin': 'sol',
    'price': '32'
}
same_keys = {}
for key, value in good_crypto.items():
    for key1, value1 in bad_crypto.items():
        if key == key1:
            same_keys[key1] = [value, value1]
        else:
            break

diff_keys = good_crypto | bad_crypto
result = diff_keys | same_keys

json_result = json.dumps(result)
with open('result.json', 'w') as file:
    file.write(json_result)
