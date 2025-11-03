def gen_otp_4():
    return "1234"

def verify_otp(guess, secret_otp):
    return guess == secret_otp

def brute_force_otp(secret_otp):
    tries = 0
    fake_timer = 0

    for i in range(10000):
        guess = f"{i:04d}"
        tries += 1
        fake_timer += 1  
        if verify_otp(guess, secret_otp):
            return guess, tries, fake_timer

    return None, tries, fake_timer

if __name__ == "__main__":
    secret = gen_otp_4()
    print("Generated OTP (secret):", secret)
    found_pin, attempts_count, duration = brute_force_otp(secret)
    print("Found OTP:", found_pin)
    print("Attempts:", attempts_count)
    print("Simulated time units:", duration)
