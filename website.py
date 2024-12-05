import streamlit as st
import pandas as pd
from PIL import Image
import pydeck as pdk  # For enhanced maps

# **Set Page Configuration**
st.set_page_config(
    page_title="Pune's Architectural Evolution",
    page_icon=":city_sunrise:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# **Custom CSS for styling (make images responsive)**
st.markdown(
    """
<style>
    img {
        max-width: 100%;
        height: auto;
    }
    .centered-text {
        text-align: center;
    }
    .sidebar .sidebar-content {
        background: #F5F5F5;
    }
</style>
""",
    unsafe_allow_html=True,
)

# **Set Mapbox API Key**
pdk.settings.mapbox_api_key = "YOUR_MAPBOX_API_KEY"  # Replace with your token

# **Load Data**
@st.cache_data
def load_data():
    data = pd.read_csv("data/architecture_data.csv")
    return data

# Initialize session state for decade selection
if 'selected_decade' not in st.session_state:
    st.session_state.selected_decade = "Home"

data = load_data()

# **Define Decade Overviews**
decade_overviews = {
    "1940s": """
    The 1940s marked the beginning of Pune's modern architectural journey. 
    Influences from the British colonial era and the gradual introduction of new building materials began shaping the city's structural landscape. 
    Early public buildings, educational institutions, and civic centers showcased a blend of Victorian and vernacular styles.
    """,
    "1950s": """
    In the 1950s, Pune witnessed the steady rise of modernist architecture. 
    Traditional aesthetics started merging with new materials like reinforced concrete and steel. 
    Key municipal projects and residential complexes emerged, reflecting India's post-independence optimism and aspirations for progress.
    """,
    "1960s": """
    The 1960s brought significant urban development to Pune. 
    Architecture began emphasizing functionality, clean lines, and open spaces. 
    Government complexes, research institutes, and expanding educational campuses dominated the cityscape. 
    The decade also saw the first hints of zoning and city planning measures.
    """,
    "1970s": """
    During the 1970s, Pune's architecture started incorporating more sustainable practices. 
    Local materials and climate-responsive designs gained importance, partially influenced by global energy crises. 
    Housing cooperatives flourished, while local architects experimented with environmentally-conscious layouts.
    """,
    "1980s-1990s": """
    The late 20th century witnessed an eclectic fusion of international design philosophies with indigenous traditions. 
    Corporate buildings, IT parks (emerging in the 1990s), and more ambitious civic projects changed the city's skyline. 
    Postmodern elements, glass facades, and innovative design principles began coexisting with the city's cultural heritage.
    """,
}

# **Decades List**
decades = ["Home", "1940s", "1950s", "1960s", "1970s", "1980s-1990s", "About"]

# **Sidebar Navigation**
decade_selection = st.sidebar.selectbox(
    "Navigate through Decades", 
    decades, 
    index=decades.index(st.session_state.selected_decade)
)

# Update session state when selection changes
if decade_selection != st.session_state.selected_decade:
    st.session_state.selected_decade = decade_selection

# **Home Page**
if st.session_state.selected_decade == "Home":
    st.title("Pune's Architectural Evolution (1940s - 1990s)")

    # Display the logo in a smaller, centered format with container width
    st.markdown("<div class='centered-text'>", unsafe_allow_html=True)
    st.image("assets/logo.png", caption="Pune Architectural Archive", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
    Welcome to the Pune Architectural Archive, an interactive journey through the city's evolving built environment from the 1940s to the 1990s.
    
    Over these decades, Pune transformed from a modest educational hub into a burgeoning metropolis. 
    Each era brought its own architectural language, blending traditional craftsmanship with modern technology, and reflecting broader socio-economic changes.
    
    **Features of this Archive:**
    - **Decade-by-Decade Exploration:** Traverse through time to see how architectural styles and city planning evolved.
    - **Image Galleries & Featured Projects:** Delve into illustrated examples of landmark buildings, including schools, public offices, residences, and commercial spaces.
    - **Interactive Map:** Discover the geographic distribution of significant architectural works using a 3D map visualization.
    """
    )

# **About Page**
elif st.session_state.selected_decade == "About":
    st.title("About This Project")
    st.markdown(
        """
    This project aims to document and showcase Pune's architectural heritage from the mid-20th century. 
    By collating images, descriptions, and historical context, it provides a rich, educational resource for researchers, students, and enthusiasts.
    
    **Project Goals:**
    - Create a digital archive of Pune's historical and modern buildings.
    - Highlight architectural trends and socio-cultural influences across decades.
    - Provide an interactive platform that invites exploration and deeper understanding.
    
    **Methodology & Sources:**
    - Extensive archival research of municipal records, architectural journals, and historical photographs.
    - Contributions from local historians, architects, and urban planners.
    - Use of geospatial data for plotting buildings and neighborhoods on a 3D interactive map.
    
    **Contributors:**
    - Kaustubh Devang - Research, Content Development, and Web Implementation
    
    **Contact & Feedback:**
    If you have suggestions, historical photographs, or corrections, please get in touch at: 
    [pune_architecture@example.com](mailto:kaustubhdevang16@gmail.com)
    """
    )

# **Decade Pages**
else:
    st.title(f"Pune in the {st.session_state.selected_decade}")
    decade_data = data[data["decade"] == st.session_state.selected_decade]

    # **Use Tabs for Organization**
    tab_overview, tab_gallery, tab_projects, tab_map = st.tabs(
        ["Overview", "Gallery", "Featured Projects", "Map"]
    )

    with tab_overview:
        st.header(f"Overview of the {st.session_state.selected_decade}")
        overview_text = decade_overviews.get(
            st.session_state.selected_decade, "Overview information not available."
        )
        st.markdown(overview_text)

    with tab_gallery:
        st.header("Visual Gallery")
        st.write("Explore a curated selection of buildings and landmarks from this era.")
        # Display images in a responsive grid
        cols = st.columns(3)
        for idx, row in decade_data.iterrows():
            try:
                image = Image.open(row["image_path"])
                cols[idx % 3].image(image, caption=row["title"], use_container_width=True)
            except FileNotFoundError:
                cols[idx % 3].warning(f"Image not found for {row['title']}")

    with tab_projects:
        st.header("Featured Projects")
        st.write(
            "Dive deeper into some of the most notable buildings and their backstories."
        )
        for idx, row in decade_data.iterrows():
            with st.expander(row["title"]):
                col1, col2 = st.columns([1, 2])
                with col1:
                    try:
                        st.image(row["image_path"], use_container_width=True)
                    except FileNotFoundError:
                        st.error("Image not available.")
                with col2:
                    st.markdown(
                        f"**Architect**: {row['architect'] if not pd.isnull(row['architect']) else 'Unknown'}"
                    )
                    if "year_built" in row and not pd.isnull(row["year_built"]):
                        st.markdown(f"**Year Built**: {int(row['year_built'])}")
                    if "style" in row and not pd.isnull(row["style"]):
                        st.markdown(f"**Architectural Style**: {row['style']}")
                    st.markdown(
                        row["description"]
                        if not pd.isnull(row["description"])
                        else "No additional details available."
                    )

    with tab_map:
        st.header("Interactive 3D Map")
        st.write("Locate the architectural projects across Pune's landscape.")
        if (
            "location" in decade_data.columns
            and not decade_data["location"].isnull().all()
        ):
            # **Extract latitude and longitude**
            def extract_lat_lon(location_str):
                try:
                    if pd.isnull(location_str):
                        return None, None
                    lat, lon = map(float, location_str.split(","))
                    return lat, lon
                except Exception:
                    return None, None

            # Apply the function
            decade_data = decade_data.copy()
            decade_data[["lat", "lon"]] = decade_data["location"].apply(
                lambda x: pd.Series(extract_lat_lon(x))
            )

            # Drop rows with missing lat/lon
            map_data = decade_data.dropna(subset=["lat", "lon"])
            map_data["height"] = 50  # Example height

            if not map_data.empty:
                # **Create the pydeck 3D Column Layer**
                column_layer = pdk.Layer(
                    "ColumnLayer",
                    data=map_data,
                    get_position="[lon, lat]",
                    get_elevation="height",
                    elevation_scale=1,
                    radius=50,
                    get_fill_color="[200, 30, 0, 160]",
                    pickable=True,
                    auto_highlight=True,
                )

                # **Add a Text Layer for Labels**
                text_layer = pdk.Layer(
                    "TextLayer",
                    data=map_data,
                    get_position="[lon, lat]",
                    get_text="title",
                    get_size=14,
                    get_color="[50, 50, 50]",
                    get_alignment_baseline="'bottom'",
                )

                # **Define the initial view state**
                midpoint = (map_data["lat"].mean(), map_data["lon"].mean())
                view_state = pdk.ViewState(
                    latitude=midpoint[0],
                    longitude=midpoint[1],
                    zoom=13,
                    pitch=45,  # Tilt the map for a 3D perspective
                    bearing=0,
                )

                # **Create the Deck object**
                deck = pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state=view_state,
                    layers=[column_layer, text_layer],
                    tooltip={"text": "{title}\nArchitect: {architect}"},
                )

                # **Render the Deck object in Streamlit**
                st.pydeck_chart(deck)
            else:
                st.info("No valid location data available to display on the map.")
        else:
            st.info("Location data is not available for this decade.")

# **Navigation**
st.markdown("---")
idx = decades.index(st.session_state.selected_decade)
col1, col2, col3 = st.columns([1, 1, 1])

# Previous Decade Navigation
if idx > 1:
    previous_decade = decades[idx - 1]
    if col1.button(f"← {previous_decade}"):
        st.session_state.selected_decade = previous_decade

# Next Decade Navigation
if idx < len(decades) - 2:
    next_decade = decades[idx + 1]
    if col3.button(f"{next_decade} →"):
        st.session_state.selected_decade = next_decade

# Home Button
if col2.button("Home"):
    st.session_state.selected_decade = "Home"

# **Footer**
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
© 2024 Pune Architectural Archive  
*Preserving the Past, Inspiring the Future*
"""
)
