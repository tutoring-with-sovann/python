user_login_credential = {
  'thavarak': 'i_am_a_swimmer_168',
  'thanak': 'thanak_cool_hacker_168',
}
print(user_login_credential)

print('Adding another user credential.')
username = input('Enter your username: ')
password = input('Enter your password: ')
user_login_credential.update({ username: password })

print(user_login_credential)
