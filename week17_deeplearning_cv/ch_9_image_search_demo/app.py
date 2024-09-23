import streamlit as st
ifrom pinecone import Pinecone
from model import EmbeddingExtractor
from PIL import Image

st.title("Shoes Image Search")


@st.cache_resource
def load_model():
    return EmbeddingExtractor(weight_path="./data/resnet18_finetune.pth")


@st.cache_resource
def init_pinecone_index():
    pc = Pinecone(api_key=st.secrets["PINECONE_KEY"])
    index = pc.Index("shoes")
    return index


with st.spinner("Loading model..."):
    model = load_model()
index = init_pinecone_index()


def search(label, embedding, k=5):
    result = index.query(
        vector=embedding,
        top_k=k,
        filter={
            "label": label
        },
        include_metadata=True
    )
    return [x["metadata"]["image_path"].replace("./shoes/", st.secrets["S3_URL"]) for x in result["matches"]]


uploaded_file = st.file_uploader(
    label="upload",
    label_visibility="collapsed",
    type=["jpg", "jpeg", "png"]
)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.subheader("Query Image")
    st.image(image, width=150)
    with st.spinner("Search similar images..."):
        label, embedding = model.extract_features(image)
        image_paths = search(label, embedding, k=10)
        st.subheader("Similar Images")
        st.image(image_paths)
