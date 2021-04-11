from subprocess import Popen, PIPE, STDOUT

def action(path: str, *action: str) -> tuple:
    if not action:
        tg_action = 'plan'
    else:
        tg_action = action[0]

    process = Popen(
        ['terragrunt', tg_action, '--terragrunt-working-dir', path],
        stderr=STDOUT, stdout=PIPE
    )

    return process.communicate()[0].decode('utf-8'), process.returncode