import streamlit as st
import datetime

def fill_dict(previous_renting_txID,
              userID, user_public_key, #user_rating,
              item_category, itemID, item_position, item_family_code, item_description, status_coefficient,
              inventory_coordinates, inventory_capacity,
              start_renting, end_renting, duration,
              available):
    data = {
        "previous_renting_txID": previous_renting_txID,           # Info da blockchain
        "user": {
            "userID": userID,                                     # Info da user account
            "user_public_key": user_public_key,                   # Info da user account
            #"user_rating": user_rating
        },
        "item": {
            "item_credentials": {
                "item_category": item_category,         # Info da App -> categoria
                "itemID": itemID,                                 # Info da App (codice [come da sito] + codice progressivo univoco oggetto)
                "item_position": item_position,             # Info da App
                "item_family_code": item_family_code,                       # Info da App
                "item_description": item_description              # Info da Ap
            },
            "item_status": status_coefficient                     # Bisogna trovare un modo per calcolarlo
        },
        "inventory": {
            "inventory_coordinates": inventory_coordinates,       # Info da App
            "inventory_capacity": inventory_capacity              # Info da App
        },
        "time_interval": {
            "start_renting": start_renting,                       # Info da App
            "end_renting": end_renting,                           # Info da App
            "duration": duration                                  # Info da App -> calcolata automaticamente con end_renting - start_renting
        },
        "available": available                                    # True if datetime.now() < start_renting or datetime.now() > end_renting
    }
    return data


def main():
    st.title("Template per Timestamp")

    previous_renting_txID = st.sidebar.text_input("previous_renting_txID")

    userID = st.sidebar.text_input("userID")

    user_public_key = st.sidebar.text_input("user_public_key")

    #user_rating = st.sidebar.slider('Rate your ability to be a good costumer', 0.0, 5.0, 0.0)

    item_category = st.sidebar.selectbox("Che accessorio vuoi prenotare?", ("Tostapane Bianco, Lucido Estetica 50's Style",
                                                                                  "Frullatore Nero Estetica 50's Style",
                                                                                  "Impastatrice Nero Estetica 50's Style")
                                              )
    itemID = st.sidebar.text_input("itemID")

    item_position = st.sidebar.text_input("item_position")

    ## Qua c'è da inserire la compilazione condizionale in base al campo item_Category
    #item_family_code = st.sidebar.selectbox('Codice accessorio', ('TSF01WHEU', 'BLF01BLEU', 'SMF02BLEU'))
    if "Tostapane" in item_category:
        item_family_code = "TSF01WHEU"
    elif "Frullatore" in item_category:
        item_family_code = "BLF01BLEU"
    elif "Impastatrice" in item_category:
        item_family_code = "SMF02BLEU"

    #item_description = st.sidebar.text_input("item_description")
    if item_family_code == "TSF01WHEU":
        item_description = "Nelle sue dimensioni il tostapane due fette Smeg concentra ergonomia, funzionalità e armonia estetica. Colazione o lunch break, brunch o aperitivo: se ha colpito al cuore, ogni scusa è buona per usarlo."
    if item_family_code == "BLF01BLEU":
        item_description = "I frullatori Smeg miscelano perfettamente ingredienti di consistenza differente per un utilizzo che accompagni ogni momento della nostra giornata."
    if item_family_code == "SMF02BLEU":
        item_description = "L’impastatrice Smeg della linea Anni ’50 sarà amore a prima vista. Nelle sue forme sinuose e nei suoi colori briosi si riflette tutto lo spirito creativo e la passione per la cucina, ma anche per le cose belle e il design."

    status_coefficient = st.sidebar.slider("In che condizioni era l'accessorio quando l'hai trovato? (Preso malissimo (0) -- Condizioni ottime (10))", 0, 10, 1)

    inventory_coordinates = st.sidebar.text_input("inventory_coordinates")

    inventory_capacity = st.sidebar.slider('How full is the inventory? (0 means empty, 100 means full)', 0, 100, 0)

    start_renting = st.sidebar.date_input("When will you rent the item?", datetime.date(2023, 1, 1))

    end_renting = st.sidebar.date_input("When will are going to bring back the item?", datetime.date(2023, 12, 1))

    duration = end_renting-start_renting

    if datetime.date.today() < start_renting or datetime.date.today() > end_renting:
        available = True
    else:
        available = False

    result = fill_dict(previous_renting_txID,
                       userID,
                       user_public_key,
                       #user_rating,
                       item_category,
                       itemID,
                       item_position,
                       item_family_code,
                       item_description,
                       status_coefficient,
                       inventory_coordinates,
                       inventory_capacity,
                       start_renting,
                       end_renting,
                       duration,
                       available
                       )

    st.write("Message", result)

if __name__ == '__main__':
    main()