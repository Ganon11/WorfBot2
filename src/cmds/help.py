try:
    import config
    import err
except ImportError:
    sys.exit(err.LOAD_MODULE)

def help(command): # !help
    """Returns a string containing all the available commands

    """
    response = str(len(config.cmds_list)) + ' available commands: '

    for i in config.cmds_list:
        response = response + '!' + i + ' '
    return response
