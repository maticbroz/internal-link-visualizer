# Internal Link Visualizer

This project visualizes internal links of a website using data from a CSV file. It uses `pandas` to handle the CSV data and `pyvis` to create an interactive network graph.

## Features

- Reads internal link data from a CSV file
- Handles multiple encodings
- Generates an interactive HTML graph

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/internal-link-visualizer.git
    cd internal-link-visualizer
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your `links.csv` file in the project directory.
2. Run the script:
    ```bash
    python main.py
    ```
3. Open the generated `link_graph.html` file in a web browser to view the interactive graph.

## Example

An example `links.csv` file is provided for testing purposes.

## Dependencies

- pandas
- pyvis

## License

This project is licensed under the MIT License.
