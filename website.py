import streamlit as st
import pandas as pd
from PIL import Image
import pydeck as pdk  # For enhanced maps


st.set_page_config(
    page_title="Pune's Architectural Evolution",
    page_icon=":city_sunrise:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    body {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(to right, #f7f7f7, #e3e3e3);
    }
    .centered-text {
        text-align: center;
        margin-bottom: 20px;
    }
    .sidebar .sidebar-content {
        background: #F5F5F5;
    }
    .gallery-image:hover {
        transform: scale(1.05);
        transition: transform 0.3s ease;
    }
    .highlight-box {
        background-color: #fcfcfc;
        border-left: 4px solid #FFA500;
        padding: 15px;
        margin: 20px 0;
        border-radius: 4px;
    }
    .highlight-box h4 {
        margin-top: 0;
        font-weight: 700;
    }
    .highlight-box ul {
        margin-bottom: 0;
        padding-left: 20px;
    }
    .highlight-box ul li {
        margin-bottom: 5px;
    }
    .main-title {
        text-align: center;
        font-size: 3em;
        font-weight: 700;
        margin-top: 20px;
        color: #333333;
    }
    .decade-title {
        font-size: 2em;
        color: #333333;
        margin-top: 20px;
    }
    .footer-text {
        font-size: 0.9em;
        color: #666666;
        text-align: center;
        margin-top: 30px;
    }
    .footer-text a {
        color: #666666;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# **Set Mapbox API Key**
pdk.settings.mapbox_api_key = "YOUR_MAPBOX_API_KEY"

# **Load Data**
@st.cache_data
def load_data():
    data = pd.read_csv("data/architecture_data.csv")
    return data


# Initialize session state for decade selection
if "selected_decade" not in st.session_state:
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

# **Define Decade Highlights**
decade_highlights = {
    "1940s": [
        "Transitioning from colonial influences to vernacular adaptations",
        "Introduction of reinforced concrete and newer building materials",
        "Foundational public and educational institutions",
    ],
    "1950s": [
        "Rising modernist principles influencing cityscapes",
        "Blending traditional aesthetics with new construction techniques",
        "Emergence of key municipal and residential projects",
    ],
    "1960s": [
        "Strong focus on functionality and open spaces",
        "Expansion of government complexes and research institutes",
        "Initial steps towards zoning and planned urban growth",
    ],
    "1970s": [
        "Growing emphasis on sustainable and climate-responsive designs",
        "Increased use of local materials and eco-friendly practices",
        "Housing cooperatives and community-centric developments",
    ],
    "1980s-1990s": [
        "Eclectic fusion of international and indigenous design philosophies",
        "Introduction of IT parks and corporate architecture",
        "Postmodern elements and innovative building façades",
    ],
}

# **Decades List**
decades = ["Home", "1940s", "1950s", "1960s", "1970s", "1980s-1990s", "About"]

# **Sidebar Navigation**
st.sidebar.title("Explore Pune's Past")
st.sidebar.markdown("Navigate through six decades of architectural transformation:")
decade_selection = st.sidebar.selectbox(
    "Select a Decade or Section",
    decades,
    index=decades.index(st.session_state.selected_decade),
)

# Update session state when selection changes
if decade_selection != st.session_state.selected_decade:
    st.session_state.selected_decade = decade_selection

# **Home Page**
if st.session_state.selected_decade == "Home":
    st.markdown(
        "<h1 class='main-title'>Pune's Architectural Evolution (1940s - 1990s)</h1>",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='centered-text'>", unsafe_allow_html=True)
    st.image(
        "assets/logo.png",
        caption="Pune Architectural Archive",
        use_container_width=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        Welcome to the **Pune Architectural Archive**, an interactive journey through the city's evolving built environment from the 1940s to the 1990s.
        
        Over these decades, Pune transformed from a modest educational hub into a burgeoning metropolis. Each era introduced fresh design philosophies, construction materials, and planning principles, mirroring broader social, economic, and cultural shifts.
        """
    )

    st.markdown(
        """
        **Features of this Archive:**
        - **Decade-by-Decade Exploration:** Traverse through time and witness changing architectural styles and urban planning milestones.
        - **Immersive Visual Galleries:** Explore landmark buildings, from public institutions and educational campuses to residential complexes and commercial hubs.
        - **Interactive 3D Map:** Pinpoint the geographic distribution of Pune's architectural gems using an advanced map visualization tool.
        """
    )

    st.info(
        "Use the sidebar to start exploring different decades or learn more in the 'About' section."
    )

# **About Page**
elif st.session_state.selected_decade == "About":
    st.title("About This Project")
    st.markdown(
        """
        This digital archive is a tribute to Pune's rich architectural heritage and its dynamic transformation over the mid-20th century. By compiling images, archival research, and expert insights, we hope to provide a valuable educational resource and a source of inspiration.
        """
    )

    st.markdown(
        """
        **Project Goals:**
        - Construct a comprehensive digital repository of Pune's historical buildings.
        - Highlight the interplay between architectural trends, socio-cultural influences, and evolving urban policies.
        - Offer an interactive, user-friendly platform that encourages exploration and deeper appreciation.
        
        **Methodology & Sources:**
        - In-depth review of municipal archives, architectural journals, and historical documentation.
        - Contributions from local historians, architects, and urban planners.
        - Integration of geospatial data for mapping and visualization.
        
        **Key Contributor:**
        - Kaustubh Devang – Research, Content Development, Web Implementation
        
        **Contact & Feedback:**
        We welcome contributions, suggestions, and corrections. Please reach out at:
        [kaustubhdevang16@gmail.com](mailto:kaustubhdevang16@gmail.com)
        """
    )

# **Decade Pages**
else:
    st.markdown(
        f"<h1 class='decade-title'>Pune in the {st.session_state.selected_decade}</h1>",
        unsafe_allow_html=True,
    )
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

        highlights = decade_highlights.get(st.session_state.selected_decade, [])
        if highlights:
            st.markdown(
                f"""
                <div class="highlight-box">
                    <h4>Key Highlights of this Era:</h4>
                    <ul>
                        {''.join(f'<li>{item}</li>' for item in highlights)}
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with tab_gallery:
        st.header("Visual Gallery")
        st.write(
            "Explore a selection of buildings and landmarks that exemplify this decade's architectural style. Hover over images for a subtle effect!"
        )

        cols = st.columns(3)
        idx_col = 0
        for idx, row in decade_data.iterrows():
            try:
                image = Image.open(row["image_path"])
                with cols[idx_col]:
                    st.markdown(f"<div class='gallery-image'>", unsafe_allow_html=True)
                    st.image(image, caption=row["title"], use_container_width=True)
                    st.markdown("</div>", unsafe_allow_html=True)

                idx_col = (idx_col + 1) % 3
            except FileNotFoundError:
                cols[idx_col].warning(f"Image not found for {row['title']}")
                idx_col = (idx_col + 1) % 3

    with tab_projects:
        st.header("Featured Projects")
        st.write(
            "Delve deeper into notable buildings of this decade. Click on a project to learn about its background, architectural significance, and the visionary minds behind it."
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
        st.write(
            "Pinpoint the geographical spread of these architectural projects. Zoom, pan, and tilt the map for a detailed spatial understanding."
        )
        if (
            "location" in decade_data.columns
            and not decade_data["location"].isnull().all()
        ):

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

                text_layer = pdk.Layer(
                    "TextLayer",
                    data=map_data,
                    get_position="[lon, lat]",
                    get_text="title",
                    get_size=14,
                    get_color="[50, 50, 50]",
                    get_alignment_baseline="'bottom'",
                )

                midpoint = (map_data["lat"].mean(), map_data["lon"].mean())
                view_state = pdk.ViewState(
                    latitude=midpoint[0],
                    longitude=midpoint[1],
                    zoom=13,
                    pitch=45,
                    bearing=0,
                )

                deck = pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state=view_state,
                    layers=[column_layer, text_layer],
                    tooltip={"text": "{title}\nArchitect: {architect}"},
                )

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
    if col1.button(
        f"← {previous_decade}", key=f"prev_{st.session_state.selected_decade}"
    ):
        st.session_state.selected_decade = previous_decade
        st.rerun()

# Home Button
if col2.button("Home", key=f"home_{st.session_state.selected_decade}"):
    st.session_state.selected_decade = "Home"
    st.rerun()

# Next Decade Navigation
if idx < len(decades) - 2:
    next_decade = decades[idx + 1]
    if col3.button(f"{next_decade} →", key=f"next_{st.session_state.selected_decade}"):
        st.session_state.selected_decade = next_decade
        st.rerun()


# **Footer**
st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    © 2024 Pune Architectural Archive  
    *Preserving the Past, Inspiring the Future*
    """
)

st.markdown(
    """
    <div class="footer-text">
        <p>Connect with us:</p>
        <p>
            <a href="mailto:kaustubhdevang16@gmail.com">Email</a> | 
            <a href="https://www.linkedin.com/">LinkedIn</a> | 
            <a href="https://www.twitter.com/">Twitter</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
