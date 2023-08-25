
# Fitbit Sense BLE Communication

This project provides a script to communicate with a Fitbit Sense smartwatch using the BLE (Bluetooth Low Energy) protocol. It sends a large set of data in chunks to a specified characteristic on the device.

## Requirements

- Python 3.7 or higher
- `bleak` library (install using `pip install bleak`)

## Usage

1. Clone the repository.
2. Update the `fitbit_mac_address` variable with the MAC address of your Fitbit Sense.
3. Run the script using `python main.py`.

## License

MIT License

Copyright (c) 2023 R. Chukwuka Molokwu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
