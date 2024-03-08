# Bingo Sheet and Tick Sheet Generator

This Python script automatically generates a PDF file containing 100 unique bingo sheets with song titles and a tick sheet for the host to keep track of played songs. It's designed to facilitate the organization of bingo games that use song titles instead of numbers.

## Features

- **Custom Bingo Sheets**: Generates 100 unique bingo sheets, each containing 25 unique song titles.
- **Host Tick Sheet**: Creates a tick sheet listing all the song titles for the host to easily mark off played songs.
- **Easy to Customize**: Read song titles from a CSV file, allowing for easy customization of bingo sheets.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your system.
- `reportlab` library installed. If you haven't installed it yet, you can do so by running `pip install reportlab` in your terminal or command prompt.

## Installation

1. Clone this repository or download the source code to your local machine.
2. Ensure you have the required prerequisites installed.
3. Place a CSV file named `songs.csv` in the same directory as the script. The CSV file should contain one song title per line.

## Usage

To generate the bingo sheets and tick sheet, navigate to the directory containing the script and run:

```bash
python bingo_sheet_generator.py
```

This will generate two PDF files:
- `bingo_sheets.pdf`: Contains 100 unique bingo sheets.
- `tick_sheet.pdf`: Contains a tick sheet for the host.

## Customization

To customize the song titles, edit the `songs.csv` file and add or remove song titles as needed. Each title should be on a separate line.

## Contributing

Contributions to this project are welcome! Please feel free to submit issues or pull requests with improvements or new features.

## License

This project is open source and available under the [MIT License](LICENSE).

