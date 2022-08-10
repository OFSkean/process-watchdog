# Motivation
I'm sure most programmers know the terrible feeling of starting a long-running piece of code to go overnight, only to find out it errored 5 minutes in. It's not a fun thing to discover in the morning. To ensure that doesn't happen to us anymore, I've created this library to alert if something unsavory happens.

# Features
Current

1. Custom IPython magic-commands for Jupyter Notebooks that fire when a cell either errors or completes. When it does, it sends an email to a specified address with information.
2. Can use the magic-commands on single cells, or automatically apply them to every cell in the notebook.

Planned

1. Similar functionality for standard .py scripts. Most likely this will check for when the PID is finished.
2. Other alert mechanisms besides email

# Installation Instructions:
Below are two different methods of installation. The first is simpler, while the second allows you to use and modify the library files in-place. Note that only one method is required.

## Installation Directly from Github
```
python -m pip install git+https://github.com/OFSkean/process-watchdog.git
```

## Editable Installation
Following this procedure, the git repository is clone and editably installed. This lets you edit or add to the library files without having to reinstall.

1) Download git repository: ```git clone https://github.com/OFSkean/process-watchdog.git```

2) Move to folder:  ```cd process-watchdog```

3) Install with pip:  ```pip install -e .```


# Imports
```
import watchdog.Notifier as watchdog
watchdog.start("fake@fakeemail.com")
```

# Documentation
```
watchdog.start(email, universal_completion_notifier=False, universal_exception_notifier=False):

Inputs:
- email - Where will the email send
- universal_completion_notifier - if completion_handler should be placed automatically on all cells
- universal_exception_notifier - if exception_handler should be placed automatically on all cells
```

```
%%completion_handler
```



# Examples
In the examples folder are a few easy notebooks with example code.