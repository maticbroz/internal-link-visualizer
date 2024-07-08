import pandas as pd
from pyvis.network import Network

def create_link_graph_from_csv(csv_file, encodings):
    """
    Creates a graph representation of internal links from a CSV file.
    Tries multiple encodings until a successful read.
    
    Parameters:
    csv_file (str): The path to the CSV file.
    encodings (list): A list of encodings to try for reading the file.
    
    Returns:
    DataFrame: A pandas DataFrame containing the link data.
    """
    for encoding in encodings:
        try:
            df = pd.read_csv(csv_file, encoding=encoding, sep="\t")
            return df
        except UnicodeDecodeError:
            pass
    raise ValueError("Unable to read the CSV file with the provided encodings.")

def visualize_link_graph(df, output_file='link_graph.html'):
    """
    Visualizes the link graph using pyvis.
    
    Parameters:
    df (DataFrame): A pandas DataFrame containing the link data.
    output_file (str): The name of the output HTML file.
    """
    net = Network(height="1000px", width="100%", bgcolor="#222222", font_color="white")
    
    sources = df['Referring page URL']
    targets = df['Target URL']
    
    edge_data = zip(sources, targets)
    
    for src, dst in edge_data:
        net.add_node(src, src, title=src)
        net.add_node(dst, dst, title=dst)
        net.add_edge(src, dst)
    
    net.show(output_file)

if __name__ == "__main__":
    csv_file_path = 'links.csv'
    encodings = ['utf-8', 'utf-16']  # Add more encodings if needed
    
    link_df = create_link_graph_from_csv(csv_file_path, encodings)
    visualize_link_graph(link_df)
