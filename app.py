import streamlit as st

# Title of the application
st.title("Prototype de Suivi des Patientes")

# Main menu
menu = ["Accueil", "Dossier Patient", "Nouvelle Consultation"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Accueil":
    st.header("Liste des Patients")
    st.text_input("Rechercher un patient", "")
    st.write("Exemple de liste fictive :")
    st.table({
        "Nom": ["Dupont", "Martin", "Durand"],
        "Âge": [45, 54, 62],
        "Statut ménopausique": ["Oui", "Non", "Oui"]
    })

elif choice == "Dossier Patient":
    st.header("Dossier Patient")
    st.write("Informations détaillées sur le patient sélectionné.")
    st.text_area("Antécédents médicaux", "Exemple : Cancer, traitement hormonal...")
    st.text_area("Historique des consultations", "Exemple : Consultation du 01/01/2024 - Motif : douleurs.")

elif choice == "Nouvelle Consultation":
    st.header("Nouvelle Consultation")
    st.text_input("Motif de consultation")
    st.text_area("Examen clinique")
    st.selectbox("Échelle EVA", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    st.text_area("Conclusion et conduite à tenir")
    st.button("Sauvegarder")
