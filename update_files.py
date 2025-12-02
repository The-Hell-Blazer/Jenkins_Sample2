import re
import os

def update_memlay():
    file_path = "memlay.h"

    if not os.path.exists(file_path):
        print(f"ERROR: {file_path} not found")
        return False

    with open(file_path, "r") as f:
        content = f.read()

    updated_content = re.sub(
        r"STUBBING ACTIVE *= *0",
        "STUBBING ACTIVE = 1",
        content
    )

    with open(file_path, "w") as f:
        f.write(updated_content)

    print("✔ Updated memlay.h successfully")
    return True


def update_data():
    file_path = "data.txt"

    if not os.path.exists(file_path):
        print(f"ERROR: {file_path} not found")
        return False

    with open(file_path, "r") as f:
        content = f.read()

    updated_content = re.sub(
        r"BSW *= *N851",
        "BSW = N85A",
        content
    )

    with open(file_path, "w") as f:
        f.write(updated_content)

    print("✔ Updated data.txt successfully")
    return True


if __name__ == "__main__":
    print("=== Running Update Script ===")

    ok1 = update_memlay()
    ok2 = update_data()

    if ok1 and ok2:
        print("✔ File modifications completed.")
    else:
        print("⚠ Some files were not updated.")
