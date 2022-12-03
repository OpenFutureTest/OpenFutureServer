import os
import sys


if __name__ == "__main__":
    env = sys.argv[1] if len(sys.argv) > 1 else 'Local'
    if env not in ['Local', 'Test', 'Stage', 'Production', 'UnitTest']:
        raise EnvironmentError('The environment variable (OFSENV) is invalid ')
    os.environ['OFSENV'] = env
    from ofs import app
    app.run(host="0.0.0.0", port=8081)