import streamlit as st
import bluetooth

def send_data_to_device(device_address, message):
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((device_address, 1))
        sock.send(message)
        sock.close()
        st.success("Données envoyées avec succès !")
    except Exception as e:
        st.error(f"Erreur lors de l'envoi des données : {e}")

# Interface utilisateur avec Streamlit
st.title("Communication Bluetooth avec Streamlit")

# Liste des appareils Bluetooth à proximité
device_list = bluetooth.discover_devices(lookup_names=True)

# Demander à l'utilisateur de choisir un appareil dans la liste
selected_device = st.selectbox("Sélectionnez un appareil Bluetooth", device_list)

# Demander à l'utilisateur le message à envoyer
message = st.text_input("Entrez le message à envoyer")

# Bouton pour envoyer le message au périphérique sélectionné
if st.button("Envoyer"):
    if selected_device and message:
        send_data_to_device(selected_device[0], message)
    else:
        st.warning("Veuillez sélectionner un appareil et saisir le message.")
