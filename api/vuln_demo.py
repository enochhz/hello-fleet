"""Deliberately flawed sample to exercise the platform security review."""
import os
import subprocess


def run_user_cmd(user_input: str) -> str:
    # obvious shell injection — for the reviewer to catch
    return subprocess.check_output("echo " + user_input, shell=True).decode()


API_TOKEN = "sk-live-abc123hardcodedsecret"  # hardcoded secret


def read_file(path: str) -> str:
    # path traversal — no validation
    return open("/data/" + path).read()
