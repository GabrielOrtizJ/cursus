import alchemy

print("=== Alembic 4 ===")
print("Testing create_air:", alchemy.create_air())

print("This will raise an exception! "
      "Testing the hidden create_earth:")
try:
    print(alchemy.create_earth())
except Exception as e:
    print("Error:", e)
