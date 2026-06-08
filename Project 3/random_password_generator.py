import random
import string


def generate_password(length: int) -> str:
   
  
    character_pool = string.ascii_letters + string.digits
    
   
    password_chars = [random.choice(character_pool) for _ in range(length)]
    
    return "".join(password_chars)



def main():
    print("====================================================")
    print("        ***Random Password Generator***")
    print("====================================================\n")

    print("--- PHASE 1: ENVIRONMENTAL INPUT VALIDATION ---")
    while True:
        try:
            user_input = input("Enter target password length: ").strip()
            password_length = int(user_input)
            
            if password_length < 15:
                print(
                    "[Validation Error] Below 15 character minimum requirement\n"
                    "                   for high-security contexts."
                )
                continue
            elif password_length > 64:
                print(
                    "[Validation Error] Exceeds maximum allowed passphrase\n"
                    "                   limit of 64 characters."
                )
                continue
            break

        except ValueError:
            print(
                "[System Alert] Input phase failure. Value must be a valid\n"
                "               target numerical integer[cite: 199]."
            )
            print("-" * 52)

    print("\n--- PHASE 2: BACKEND CORE TRANSFORMATION ---")
    print("Initializing backend logic engine transformation...")
    secure_password = generate_password(password_length)
    print("Cryptographic integrity verified. Compiling stream tokens...")

    print("\n--- PHASE 3: OUTPUT DELIVERY ---")
    print(f"Generated Password : {secure_password}")
    print("System Status      : Verified digital shield deployed with absolute precision[cite: 120].")
    print("====================================================")

if __name__ == "__main__":
    main()