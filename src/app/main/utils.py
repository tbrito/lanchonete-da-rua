import os


def get_env_variable(name) -> str:
    try:
        return os.environ[name]
    except KeyError:
        message = "Variável de ambiente esperada '{}' não foi configurada.".format(name)
        raise Exception(message)