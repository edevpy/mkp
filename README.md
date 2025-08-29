# mkp - MaKe Password

**mkp** is a command-line tool for generating strong, random passwords.
It's designed to be simple and efficient, allowing you to quickly create secure
passwords with customizable options.


## Features

- **Random Generation:** Creates passwords using a mix of uppercase letters,
lowercase letters, numbers and symbols.

- **Customizable Length:** Easily specify the desired password length.

- **Character Exclusion:** Exclude specific characters you don't want in your
password.

- **Clipboard Integration:** Automatically copy the generated password to your
clipboard for easy pasting.

- **Silent Mode:** Prevent the password from being printed to the console for
added security in scripts or automated tasks.


## Installation

### Prerequisites

You need the following installed on your system:

- **Python 3.13** or higher.

- **xclip** (for clipboard functionality on Linux).

To install **xclip**, use your system's package manager:

```bash
# On Debian/Ubuntu
sudo apt-get install xclip
```

### Clone repository

```bash
git clone https://github.com/edevpy/mkp.git
cd mkp
python3 -m venv .venv
pip install -r requirements.txt
```


## Usage

### Basic Usage

To generate a password with the default length of 16 characters:

```bash
python3 mkp.py
```

### Options

|Option         |Shorthand|Description                                               |Default    |
|:-------------:|:-------:|:---------------------------------------------------------|:---------:|
|```--length``` |```-l``` |The desired length of the password.                       |```16```   |
|```--delete``` |```-d``` |Characters to exclude from the password.                  |```''```   |
|```--copy```   |```-c``` |Copies the generated password to the clipboard.           |```False```|
|```--silence```|```-s``` |Does not print the password to the console. Useful with -c|```False```|


## Examples

### 1. Generate a 24-character password:

```bash
python3 mkp.py --length 24
```

### 2. Generate a password and exclude certain characters:

This example excludes ```a```, ```b``` and ```1``` from the password.

```bash
python3 mkp.py --delete "ab1"
```

### 3. Generate a password and copy it to the clipboard:

```bash
python3 mkp.py --copy
```

### 4. Generate a password, copy it and don't print it to the console:

This is ideal for scripting, as the password won't be visible in your terminal
history.

```bash
python3 mkp.py --copy --silence
```


## Dependencies

- **pyperclip**: A cross-platform Python module for copy and paste functions.

- **xclip**: A command-line utility for the X11 clipboard. This is a system
dependency required for ```pyperclip``` to work on Linux.


## License

This project is licensed under the **MIT License**.
See the [LICENSE.md](./LICENSE.md) for details.
