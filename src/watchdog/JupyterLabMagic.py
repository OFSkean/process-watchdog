from IPython.core.magic import register_cell_magic
import watchdog.Email as Email
import traceback

@register_cell_magic('completion_watchdog')
def handle(line, cell):
    try:
        result = get_ipython().run_cell(cell)
        result.raise_error()
    except Exception as e:
        Email.send(traceback.format_exc(), is_error=True)
        raise
    else:
        Email.send("Cell completed without errors!")

@register_cell_magic('exception_watchdog')
def handle(line, cell):
    try:
        result = get_ipython().run_cell(cell)
        result.raise_error()
    except Exception as e:
        Email.send(traceback.format_exc(), is_error=True)
        raise

# this function will be called on exceptions in any cell
def custom_exception_handler(shell, etype, evalue, tb, tb_offset=None):
    # still show the error within the notebook, don't just swallow it
    shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)

    Email.send(''.join(traceback.format_tb(tb)), is_error=True)

# this function will be called on completions in any cell
def custom_completion_handler():
    Email.send("Cell is finished running. Maybe it errored, maybe not...")