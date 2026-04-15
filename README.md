# Message Count

A simple Python utility that analyzes chat or text files and counts the number of messages sent by each person.

## Overview

This project reads a text file containing chat messages and provides statistics on how many messages each user has sent. It's designed to work with chat exports where messages are prefixed with the sender's name followed by a colon (e.g., `Alice: message text`).

## Features

- 📊 **Message Count Analysis**: Count total messages per user
- 🔍 **User Lookup**: Query message count for a specific person
- 🛡️ **Robust Parsing**: Handles UTF-8 encoding with error tolerance
- ⚡ **Simple & Lightweight**: Easy to use command-line interface

## Requirements

- Python 3.x
- A text file containing chat messages

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dabhishek9035-ui/message-count.git
cd message-count
```

2. Ensure your chat file is named `text1.txt` in the same directory (or modify the filename in `chat.py`)

## Usage

1. **Prepare your chat file**: The text file should contain messages in the format:
   ```
   Username: message content here
   Another User: another message
   ```

2. **Run the script**:
   ```bash
   python chat.py
   ```

3. **Enter the person's name** when prompted (use the format `Username:` without the colon):
   ```
   name of the person: Username
   ```

4. The script will display the total number of messages sent by that person

## Example

**Input file (text1.txt):**
```
Alice: Hello everyone
Bob: Hi Alice!
Alice: How are you?
Bob: I'm doing great
Alice: That's awesome
```

**Running the script:**
```
$ python chat.py
writing the name in the format (name:)will give u no of messages sent by them
name of the person: Alice:
3
```

## File Structure

```
message-count/
├── README.md       # This file
└── chat.py         # Main Python script
```

## How It Works

1. Opens and reads the text file with UTF-8 encoding
2. Splits the content into words
3. Identifies lines with speakers (words ending in `:`)
4. Builds a frequency dictionary of message senders
5. Searches for and displays the count for the requested user

## Error Handling

- **User not found**: If the entered name doesn't exist in the file, the script displays `please use the proper format / no user found`
- **Encoding issues**: UTF-8 decoding errors are ignored for compatibility with various chat exports

## Future Enhancements

- Support for multiple file formats (Telegram, WhatsApp, Messenger exports, etc.)
- Generate statistics for all users
- Export results to CSV or JSON
- Visualize message distribution with charts
- Handle different message formatting patterns

## License

This project is open source and available for anyone to use and modify.

## Contributing

Feel free to submit issues or pull requests to improve this project!

## Author

**dabhishek9035-ui**

---

*This is a lightweight tool for quick chat analysis. For large-scale data analysis, consider using specialized tools like pandas or data visualization libraries.*