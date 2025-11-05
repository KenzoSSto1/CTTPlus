# compile_ctt.py
# CTT+ Mini Compiler v1.0
# Author: Kenzo (CoDev Studios)

import sys
import time
from cttplus import printy, waity, notify, sayy, scan_system

def run_cttplus(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    print(f"🔧 Running CTT+ Script: {file_path}\n")

    for line in lines:
        line = line.strip()
        if line.startswith("#") or not line:
            continue  # skip comments and empty lines

        try:
            exec(line)
        except Exception as e:
            print(f"⚠️ Error in line: {line}\n   {e}")
            continue

    print("\n✅ Execution finished successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compile_ctt.py <path_to_file.ctt+>")
        sys.exit(1)

    script_path = sys.argv[1]
    run_cttplus(script_path)
