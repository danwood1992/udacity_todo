import utils

utils.insert_row("users", "name email", "'Jason Bourne' 'jason@mail.com'")
utils.insert_row("users", "name email", "'James Bond' 'jamesbong@£gmail.com'")

user_rows = utils.fetch_all("users")

for row in user_rows:
    for user in row:
        print(f"Seeded: {user}")








