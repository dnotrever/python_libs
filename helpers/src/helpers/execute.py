import subprocess

def execute(command, capture=True, show=False, check=False):
    if capture:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=check
        )
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()
        if show:
            if stdout:
                print(stdout)
            if stderr:
                print(stderr)
        return stdout, stderr
    else:
        result = subprocess.run(
            command,
            shell=True,
            check=check
        )
        return '', ''
