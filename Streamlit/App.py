import pandas as pd
import streamlit as st



def loadData():
    data = pd.read_csv("BeatlesDataset.csv")
    return data

def nameSearch(searched):
    data = loadData()

    name = searched

    result = data[data['Title'].str.contains(name, case=False)]
    return result
def writerSearch(searched):
    data = loadData()
 
    
    composer = searched
    result = data[data['Songwriter'].str.contains(composer, case=False)]
    return result

def main():
    tab1, tab2, tab3 = st.tabs(["Home", "Pesquisa por Nome","Pesquisa por Compositor"])

    with tab1:
        st.header("Bem vindo à base de dados dos Beatles")
        st.image(image='/Streamlit/Image.webp')
        st.markdown('Projeto feito para estudar a ferramenta Streamlit em conjunto com a biblioteca Pandas')
        st.markdown('Feito por Gustavo Gomes')

    with tab2:
        st.header("Pesquisa por nome")
        st.subheader("Aqui você consegue pesquisar as músicas da sua banda favorita pelo nome delas")
        
        col1, col2 = st.columns(2)
        with col1:
            searchname = st.text_input(label="Insira o nome da música aqui")

        with col2:
            dataresult = nameSearch(searchname)
            st.markdown(f"{len(dataresult.index - 1)} resultados encontrados")
        
        
        st.dataframe(dataresult, height= 1000, use_container_width=True)
    with tab3:
        st.header("Pesquisa por Artista")
        st.subheader("Aqui você encontra as músicas compostas pelo seu compositor favorito dos Beatles")

        col1, col2 = st.columns(2)
        with col1:
            searchart = st.radio('Selecione pelos sobrenomes', ['Starkey', 'McCartney', 'Lennon', 'Harrison'], horizontal=True)

        with col2:
            dataresult = writerSearch(searchart)
            st.markdown(f"\n {len(dataresult.index-1)} resultados encontrados",)
        
        st.dataframe(dataresult, height=1000, use_container_width=True)
        


if __name__ == "__main__":
    main()
