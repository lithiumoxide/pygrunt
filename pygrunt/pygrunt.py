import subprocess

def plan(path):
    process = subprocess.Popen(['terragrunt', 'plan', '--terragrunt-working-dir', path])

def apply(path):
    process = subprocess.Popen(['terragrunt', 'apply', '--terragrunt-working-dir', path])