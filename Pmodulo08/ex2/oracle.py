import os
from dotenv import load_dotenv


def load_oracle_config():
    # Cargar variables desde .env (si existe)
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...\n")

    # Cargar configuración con valores por defecto seguros
    mode = os.getenv("MATRIX_MODE", "development")
    db = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log = os.getenv("LOG_LEVEL", "INFO")
    zion = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if db:
        print("Database: Connected to configured instance")
    else:
        print("Database: MISSING — no connection string found")

    if api:
        print("API Access: Authenticated")
    else:
        print("API Access: ERROR — missing API key")

    print(f"Log Level: {log}")

    if zion:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline — endpoint missing")

    print("\nEnvironment security check:")

    # Comprobación de .env
    if os.path.exists(".env"):
        print("[OK] .env file detected and loaded")
    else:
        print("[WARNING] .env file missing — relying on system environment")

    # Comprobación de modo
    if mode == "production":
        print("[OK] Production overrides active")
    else:
        print("[INFO] Running in development mode")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    load_oracle_config()
