import subprocess


def set_git_user(name, email):
    try:
        subprocess.run(["git", "config", "--global", "user.name", name], check=True)
        subprocess.run(["git", "config", "--global", "user.email", email], check=True)
        print(f"Switched Git user to: {name} <{email}>")
    except subprocess.CalledProcessError as e:
        print(f"Error setting Git user: {e}")


def get_current_git_user():
    try:
        name = subprocess.run(["git", "config", "--global", "user.name"], capture_output=True, text=True,
                              check=True).stdout.strip()
        email = subprocess.run(["git", "config", "--global", "user.email"], capture_output=True, text=True,
                               check=True).stdout.strip()
        print(f"Current Git user is set to: {name} <{email}>")
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving Git user: {e}")


def switch_user():
    user_profiles = {
        "priv": ("Szymon Private", "szymon.private@mail.com"),
        "pro": ("Szymon Professional", "szymon.professional@mail.com")
    }

    print("Select user to switch:")
    for key, (name, email) in user_profiles.items():
        print(f"{key}: {name} ({email})")

    choice = input("Enter 'priv' or 'pro': ").strip().lower()

    if choice in user_profiles:
        name, email = user_profiles[choice]
        set_git_user(name, email)
        get_current_git_user()
    else:
        print("Invalid choice. Please enter 'priv' or 'pro'.")


if __name__ == "__main__":
    switch_user()
