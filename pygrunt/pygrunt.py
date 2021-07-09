from subprocess import Popen, PIPE, STDOUT
import re

def escape_ansi(line: str) -> str:
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')

    return ansi_escape.sub('', line)

def action(path: str, action: str) -> tuple:
    if action == 'apply':
        process = Popen(
            ['terragrunt', 'apply', '-auto-approve', '--terragrunt-working-dir', path],
            stderr=STDOUT, stdout=PIPE
        )
        message = escape_ansi(process.communicate()[0].decode('utf8')).replace('\\n', '\n')
        return_code = process.returncode
    elif action == 'destroy':
        process = Popen(
            ['terragrunt', 'destroy', '-auto-approve', '--terragrunt-working-dir', path],
            stderr=STDOUT, stdout=PIPE
        )
        message = escape_ansi(process.communicate()[0].decode('utf8')).replace('\\n', '\n')
        return_code = process.returncode
    elif action == 'plan':
        process = Popen(
            ['terragrunt', 'plan', '--terragrunt-working-dir', path],
            stderr=STDOUT, stdout=PIPE
        )
        message = escape_ansi(process.communicate()[0].decode('utf8')).replace('\\n', '\n')
        return_code = process.returncode
    else:
        message = 'ERROR: No suitable commands detected.'
        return_code = 1

    return message, return_code