#!/usr/bin/env python3
"""
CTT+ Interpreter by Kenzo

This script interprets a simple custom programming language called CTT+.
It simulates virus detection for fun and educational purposes only.
"""

import time
import os
import sys

class CTTPlus:
    def __init__(self):
        self.commands = {
            'printy': self.printy,
            'waity': self.waity,
            'notify': self.notify,
            'scan_file': self.scan_file,
            'scan_path': self.scan_path,
        }

    def printy(self, text):
        print(text)

    def waity(self, seconds):
        try:
            time.sleep(float(seconds))
        except ValueError:
            print("[CTT+] Invalid wait time")

    def notify(self, message):
        print(f"[NOTIFY] {message}")

    def scan_file(self, filename):
        print(f"[SCAN] Scanning file: {filename}")
        if 'virus' in filename.lower():
            print(f"⚠️  Virus detected in {filename}!")
        else:
            print(f"✅  {filename} is safe.")

    def scan_path(self, path):
        print(f"[SCAN] Scanning directory: {path}")
        if not os.path.exists(path):
            print("[CTT+] Path not found!")
            return
        for root, _, files in os.walk(path):
            for f in files:
                self.scan_file(f)

    def execute_line(self, line):
        line = line.strip()
        if not line or line.startswith('#'):
            return
        if '(' in line and line.endswith(')'):
            name, args = line.split('(', 1)
            args = args[:-1]
            args = [a.strip().strip('"') for a in args.split(',') if a]
            if name in self.commands:
                try:
                    self.commands[name](*args)
                except TypeError:
                    print(f"[CTT+] Wrong arguments for {name}()")
            else:
                print(f"[CTT+] Unknown command: {name}")
        else:
            print(f"[CTT+] Invalid syntax: {line}")

    def run_script(self, filename):
        if not os.path.exists(filename):
            print(f"[CTT+] File not found: {filename}")
            return
        print(f"Running CTT+ script: {filename}\n--------------------")
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                self.execute_line(line)
        print("\n[CTT+] Script finished.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cttplus.py <script.ctt+>")
        sys.exit(1)

    script_file = sys.argv[1]
    interpreter = CTTPlus()
    interpreter.run_script(script_file)
