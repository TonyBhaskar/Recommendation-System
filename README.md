# Movie Recommendation System

This is a Movie Recommendation System built using Streamlit, which recommends movies based on the similarity to a selected movie. The system provides the top 5 recommendations along with their posters.

## Features

- **Movie Selection**: Select a movie from a dropdown list.
- **Recommendations**: Get the top 5 recommended movies based on similarity.
- **Poster Display**: View the posters of the recommended movies.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/TonyBhaskar/Recommendation-System.git
    cd Recommendation-system
    ```

2. **Install Dependencies**:
    Ensure you have Python installed, then install the required packages:
    ```bash
    pip install streamlit pandas requests
    ```

3. **Download Required Files**:
   - Ensure you have the `movies.pkl` and `similarity.pkl.gz` files in the root directory.

## Usage

1. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

2. **Select a Movie**:
    - Use the dropdown to select a movie.
    
3. **Get Recommendations**:
    - Click the "Recommend" button to see the top 5 movie recommendations along with their posters.

## File Structure

- **app.py**: Main application script for the Streamlit app.
- **movies.pkl**: Pickle file containing the list of movies.
- **similarity.pkl.gz**: Gzipped pickle file containing the similarity matrix.
- **Main.ipynb**: Jupyter notebook file, presumably used for data preprocessing or model building.

## Dependencies

- **streamlit**: For building the interactive web application.
- **pandas**: For handling movie data.
- **requests**: For fetching movie posters from the TMDB API.
- **gzip**: For decompressing the similarity matrix file.
- **pickle**: For loading serialized data.

## API

- **The Movie Database (TMDB)**: Used to fetch movie posters.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
