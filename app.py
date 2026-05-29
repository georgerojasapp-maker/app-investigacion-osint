import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="OSINT Tracker", page_icon="🕵️")

st.title("🕵️ OSINT TRACKER")
st.caption("Inteligencia de Fuentes Abiertas · Búsqueda por Imagen")
st.divider()

archivo = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

if archivo:
    imagen = Image.open(archivo)
    st.image(imagen, use_container_width=True)
    st.success(f"✅ Imagen cargada: {archivo.name}")

    if st.button("🚀 Iniciar Búsqueda OSINT"):
        with st.spinner("🔄 Buscando coincidencias..."):
            time.sleep(2)
        st.success("✅ Búsqueda completada (simulación MVP)")
        st.info("Módulos reales se integran en la Fase 2")
else:
    st.info("👆 Sube una imagen JPG o PNG para comenzar")
