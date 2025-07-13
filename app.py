import streamlit as st
import pandas as pd
import plotly.express as px

# Mind Map as text
mind_map_text = """
Central Theme: Elemental Analogies to String Theories
├── Fire 🔥 (Transformation & Energy)
│   ├── Type I: Transformative energy like open strings splitting/joining 🔥🔗
│   ├── Type IIA: Balanced heat flow like non-chiral supersymmetry 🔥🔄
│   ├── Type IIB: Chiral flames like asymmetric supersymmetry & holography 🔥🌀
│   ├── Heterotic SO(32): Hybrid vigor like left-right fusion 🔥⚡
│   └── Heterotic E8×E8: Unifying blaze like exceptional groups 🔥🌟
├── Water 💧 (Fluidity & Adaptability)
│   ├── Type I: Fluid interactions like unoriented open strings 💧🔗
│   ├── Type IIA: Adaptability like T-duality & compactification 💧🔄
│   ├── Type IIB: Mirroring surfaces like self-duality & AdS/CFT 💧🌀
│   ├── Heterotic SO(32): Grounding stability like anomaly-free structure 💧⚡
│   └── Heterotic E8×E8: Pervasive unity like grand unification 💧🌟
├── Air 🌬️ (Intangibility & Movement)
│   ├── Type I: Intangible movements like unoriented projections 🌬️🔗
│   ├── Type IIA: Balanced flow like (1,1) supersymmetry 🌬️🔄
│   ├── Type IIB: Chiral winds like (2,0) asymmetry & SL(2,Z) 🌬️🌀
│   ├── Heterotic SO(32): Bidirectional currents like hybrid movers 🌬️⚡
│   └── Heterotic E8×E8: Expansive reach like exceptional algebra 🌬️🌟
├── Earth 🌍 (Solidity & Grounding)
│   ├── Type I: Reactive grounding like open-closed stability 🌍🔗
│   ├── Type IIA: Solid balance like non-chiral vacua 🌍🔄
│   ├── Type IIB: Layered chirality like odd branes & dualities 🌍🌀
│   ├── Heterotic SO(32): Hybrid soil like bosonic-super fusion 🌍⚡
│   └── Heterotic E8×E8: Unified strata like Standard Model embeddings 🌍🌟
└── Ether ✨ (Boundlessness & Unity)
    ├── Type I: Boundless reactions like orientifold connections ✨🔗
    ├── Type IIA: Smooth expanse like M-theory lift ✨🔄
    ├── Type IIB: Holographic void like AdS/CFT & self-duality ✨🌀
    ├── Heterotic SO(32): Hidden stability like S-dual ties ✨⚡
    └── Heterotic E8×E8: Cosmic unity like linking universes ✨🌟
"""

# Table data
data = {
    'Element': ['Fire 🔥', 'Water 💧', 'Air 🌬️', 'Earth 🌍', 'Ether ✨'],
    'Type I': [
        'Transformative energy mirrors open strings splitting/joining dynamically 🔥🔗',
        'Fluid interactions reflect open strings flowing without orientation 💧🔗',
        'Intangible movements capture unoriented projections & gauge dynamics 🌬️🔗',
        'Reactive grounding reflects open-closed string stability 🌍🔗',
        'Boundless reactions capture orientifold connections ✨🔗'
    ],
    'Type IIA': [
        'Balanced heat flow parallels non-chiral supersymmetry & smooth transitions 🔥🔄',
        'Adaptability echoes T-duality & circle compactification 💧🔄',
        'Balanced flow aligns with (1,1) supersymmetry & even branes 🌬️🔄',
        'Solid balance evokes non-chiral vacua & supergravity limits 🌍🔄',
        'Smooth expanse echoes M-theory lift & dimensional flows ✨🔄'
    ],
    'Type IIB': [
        'Chiral flames evoke asymmetric supersymmetry & holographic dualities 🔥🌀',
        'Mirroring surfaces parallel self-duality & AdS/CFT holography 💧🌀',
        'Chiral winds match (2,0) asymmetry & SL(2,Z) symmetries 🌬️🌀',
        'Layered chirality mirrors odd branes & duality groups 🌍🌀',
        'Holographic void parallels AdS/CFT & self-dual nature ✨🌀'
    ],
    'Heterotic SO(32)': [
        'Hybrid vigor matches left-right mover fusion for stable gauges 🔥⚡',
        'Grounding stability mimics anomaly-free hybrid structure 💧⚡',
        'Bidirectional currents echo left-right hybrid movers 🌬️⚡',
        'Hybrid soil matches bosonic-super fusion for phenomenology 🌍⚡',
        'Hidden stability mimics S-dual ties to Type I ✨⚡'
    ],
    'Heterotic E8×E8': [
        'Unifying blaze aligns with exceptional groups embedding forces 🔥🌟',
        'Pervasive unity resembles grand unification in hidden sectors 💧🌟',
        'Expansive reach parallels exceptional algebra spanning symmetries 🌬️🌟',
        'Unified strata align with Standard Model embeddings 🌍🌟',
        'Cosmic unity resembles exceptional groups linking universes ✨🌟'
    ]
}
df = pd.DataFrame(data)

# Radar chart data
theories = ['Type I', 'Type IIA', 'Type IIB', 'Heterotic SO(32)', 'Heterotic E8×E8']
elements_data = {
    'Fire 🔥': [5, 4, 5, 4, 5],
    'Water 💧': [4, 5, 5, 3, 4],
    'Air 🌬️': [3, 4, 5, 4, 4],
    'Earth 🌍': [4, 3, 4, 5, 5],
    'Ether ✨': [3, 4, 5, 4, 5]
}

st.title("Visualizations of Elemental Analogies to String Theories")

st.header("Mind Map (Text-Based)")
st.code(mind_map_text, language="plaintext")

st.header("Table Visualization")
# Allow selecting columns (theories) - combinations
selected_theories = st.multiselect("Select Theories to Display", theories, default=theories)
if selected_theories:
    table_cols = ['Element'] + selected_theories
    st.dataframe(df[table_cols])
else:
    st.write("Select at least one theory.")

st.header("Radar Chart Visualization")
# Allow selecting elements to plot - combinations
selected_elements = st.multiselect("Select Elements for Radar Chart", list(elements_data.keys()), default=list(elements_data.keys()))

if selected_elements:
    # Prepare data for plotly: long format
    radar_df = pd.DataFrame({
        'Theory': theories * len(selected_elements),
        'Intensity': [elements_data[el][i] for el in selected_elements for i in range(len(theories))],
        'Element': [el for el in selected_elements for _ in theories]
    })

    # Allow reordering theories (permutation)
    order_str = st.text_input("Enter theory order separated by commas (for permutation)", ", ".join(theories))
    permuted_theories = [th.strip() for th in order_str.split(",") if th.strip() in theories]
    if len(permuted_theories) == len(theories) and set(permuted_theories) == set(theories):
        # Reorder the data based on permuted theories
        theory_index = {th: theories.index(th) for th in theories}
        radar_df['Intensity'] = [elements_data[el][theory_index[th] ] for el in radar_df['Element'] for th in permuted_theories if False]  # Wait, need to reorder properly
        # Actually, to reorder, map the intensities according to new order
        # First, for each element, get the intensities in original order, then permute
        perm_index = {old_th: idx for idx, old_th in enumerate(theories)}
        new_intensities = []
        for el in selected_elements:
            orig_int = elements_data[el]
            new_int = [orig_int[perm_index[th]] for th in permuted_theories]
            new_intensities.extend(new_int)
        radar_df['Intensity'] = new_intensities
        radar_df['Theory'] = permuted_theories * len(selected_elements)
        radar_df['Theory'] = pd.Categorical(radar_df['Theory'], categories=permuted_theories, ordered=True)
        radar_df = radar_df.sort_values('Theory')

        fig = px.line_polar(radar_df, r='Intensity', theta='Theory', color='Element', line_close=True,
                            range_r=[1, 5], title="Radar Chart of Analogy Intensity")
        st.plotly_chart(fig)
    else:
        st.write("Invalid order; using default. Must include all unique theories separated by commas.")
        # Use default
        fig = px.line_polar(radar_df, r='Intensity', theta='Theory', color='Element', line_close=True,
                            range_r=[1, 5], title="Radar Chart of Analogy Intensity")
        st.plotly_chart(fig)
else:
    st.write("Select at least one element.")

st.header("Deployment Instructions")
st.write("1. Create a public GitHub repository (e.g., `elemental-string-theories-viz`).")
st.write("2. Save this code as `app.py` in the repository's root.")
st.write("3. Add a `requirements.txt` file with:")
st.code("""streamlit
pandas
plotly""")
st.write("4. Go to [Streamlit Cloud](https://share.streamlit.io/), sign in with GitHub, and deploy the app by connecting to your repo.")
st.write("5. The app will be publicly accessible at a URL like `https://<your-app-name>.streamlit.app/`.")
