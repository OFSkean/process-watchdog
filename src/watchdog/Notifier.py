import watchdog.JupyterLabMagic as jlm
import watchdog.Email as Email

def is_notebook() -> bool:
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter

def start(email_address, universal_completion_notifier=False, universal_exception_notifier=False):
    if universal_completion_notifier and universal_exception_notifier:
        raise ValueError("It's currently unwise to have both universal completion and exception activated. Because the former encompasses the latter.")
        
    if is_notebook():
        Email.sendable_email_address = email_address
        
        if universal_exception_notifier:
            get_ipython().set_custom_exc((Exception,), jlm.custom_exception_handler)

        if universal_completion_notifier:
            get_ipython().events.register("post_execute", jlm.custom_completion_handler)

    else:
        # todo: start process watchdog
        raise ValueError('Terminal python functionality is not implemented yet!')
