# Pune’s Architectural Evolution (1940s–1990s)

**Pune’s Architectural Evolution** is an interactive, data-driven platform offering a curated journey through the city’s architectural landscape from the 1940s to the 1990s. This repository presents a historical narrative enriched by visual galleries, archival images, and geospatial analytics, highlighting the transition from colonial-era influences to modernist design philosophies, sustainable construction methods, and postmodern aesthetics that shaped Pune’s skyline.

## Overview

- **Era-by-Era Narrative:** Explore architectural trends and planning initiatives decade-by-decade, from the roots of modern Pune in the 1940s to the technology-driven influences of the 1990s.
- **Visual Galleries & Detailed Projects:** Access photographic archives of significant structures, accompanied by in-depth project profiles, including architects, construction details, stylistic notes, and historical context.
- **Interactive 3D Map:** Experience the spatial distribution of architectural landmarks through a dynamic, 3D map visualization powered by PyDeck and Mapbox.
- **Contextual Insights:** Each segment provides historical background and thematic commentary, connecting architectural achievements with broader societal, economic, and cultural forces.

## Getting Started

### Prerequisites

- **Python 3.9+**
- **pip** for package installation

### Dependencies

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Pillow (PIL)](https://pillow.readthedocs.io/)
- [PyDeck](https://pydeck.gl/)

A complete list of dependencies is provided in the `requirements.txt`.

### Mapbox Access Token

This application requires a Mapbox API token for map rendering. Obtain a token by [signing up for Mapbox](https://www.mapbox.com/) and update the `pdk.settings.mapbox_api_key` variable in `app.py`.

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sppumdes/poona_ae.git
   cd poona_ae
   ```
   
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Data & Assets:**
   - Place primary data in `data/architecture_data.csv`.  
     Required columns:
     - `title`
     - `decade`
     - `image_path`
     - `location` (latitude,longitude)
     - `architect`
     - `year_built`
     - `style`
     - `description`
   - Store images (e.g., building photos) in `images/`.

4. **Run the Application:**
   ```bash
   streamlit run website.py
   ```
   Access the interface at [http://localhost:8501](http://localhost:8501).

## Project Structure

```
pune-architectural-evolution/
├─ data/
│  └─ architecture_data.csv
├─ assets/
│  ├─ logo.png
├─ images/
│  └─ [other images]
├─ requirements.txt
└─ README.md
```

- **`website.py`**: Core Streamlit application.
- **`data/architecture_data.csv`**: Source data file including descriptive and geographical attributes.
- **`images/`**: Image assets used in the application.
- **`requirements.txt`**: Python dependencies.

## Contributing

Contributions, including historical data enhancements, corrected information, or UI/UX improvements, are welcome. Open an issue or submit a pull request to help expand the dataset and refine the overall experience. Contributions should adhere to the project’s style guidelines and maintain data integrity.

## License

This repository is available under the [MIT License](LICENSE). Refer to the license file for permissions and restrictions.

## Contact

For questions, suggestions, or collaboration proposals, please open an issue on GitHub or reach out via [email](mailto:kaustubhdevang16@gmail.com).

---

**Pune Architectural Archive**  
Preserving the Past, Inspiring the Future
