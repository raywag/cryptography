

def secret_part(p, g, secret):
    return pow(g, secret, p)


def send(p, secret, sec_part):
    return pow(sec_part, secret, p)



if __name__ == '__main__':
    alice_params = [23, 5, 6]
    bob_params = [23, 5, 15]

    alice_secret_part = secret_part(*alice_params)
    bob_secret_part = secret_part(*bob_params)

    alice_shared_key = send(alice_params[0], alice_params[2], bob_secret_part)
    bob_shared_key = send(bob_params[0], bob_params[2], alice_secret_part)

    print(f'Alce\'s secret part: {alice_secret_part}\n Alice\'s shared key: {alice_shared_key}')
    print(f'Bob\'s secret part: {bob_secret_part}\n Bob\'s shared key: {bob_shared_key}')



