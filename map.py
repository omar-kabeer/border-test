import streamlit as st
import pandas as pd
import folium
import pydeck as pdk
from streamlit_folium import st_folium, folium_static
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)

# App declaration
def main():
    df = pd.read_csv("data/borders info.csv")
    df = df.dropna()

    # page options
    pages = {
        "Home": [],
        "Border Access Points": [],
    }

    # Display dropdown menu in the sidebar for page selection
    page_selection = st.sidebar.selectbox("Select Page", list(pages.keys()))

    # Display selected page content
    if page_selection == "Home":
        tab1, tab2, tab3 = st.tabs(["Overview", "About", "Data"])
        with tab1:
            # Header contents
            st.title('Electronic Land Border Access Point (eLBAP)')
            st.subheader("Rapidly Identify and Access Electronically, National Border Access Points in Nigeria")
            st.markdown(
                "Welcome to the Electronic Land Border Access Point (eLBAP) App. This application aims to provide a fast and efficient way to identify and access national border access points in Nigeria through electronic means. With this site, you can easily search for border points based on the State, Local Government or coordinates."
            )
            st.image('resources/imgs/Nigeria showing states and LGAs with international borders.jpg')
            st.markdown("### Benin")
            st.markdown("Nigeria shares a border with Benin to the west. The border stretches for approximately 809 kilometers (503 miles).")
            st.markdown("### Niger")
            st.markdown("Nigeria shares a border with Niger to the north. The border between Nigeria and Niger is about 1,497 kilometers (930 miles) long.")
            st.markdown("### Chad")
            st.markdown("Nigeria shares a border with Chad to the northeast. The border between Nigeria and Chad is approximately 87 kilometers (54 miles) in length.")
            st.markdown("### Cameroon")
            st.markdown("Nigeria shares a border with Cameroon to the east. The border stretches for approximately 1,690 kilometers (1,050 miles).")
            st.markdown("These are the four countries that share a border with Nigeria."
            )
        with tab2:
                st.header("Nigerian Bordering Countries, States and Local Governments")
                st.write("#### The eLBAP App focuses on border access points with the following neighboring countries:")
                st.subheader("Benin Republic")
                with st.expander("##### Lagos State"):
                    st.write("###### Local Governments")
                    st.write("  - Badagry")
                with st.expander("##### Ogun State"):
                    st.write("###### Local Governments")
                    
                    st.write("  - Ipokia")
                    st.write("  - Yewa North")
                with st.expander("##### Oyo State"):
                    st.write("###### Local Governments")
                    st.write("  - Atisbo")
                    st.write("  - Iwajowa")
                    st.write("  - Saki West")
                with st.expander("##### Kwara State"):
                    st.write("###### Local Governments")
                    st.write("  - Baruten")
                with st.expander("##### Niger State"):
                    st.write("###### Local Governments")
                    st.write("  - Borgu")
                with st.expander("##### Kebbi State"):
                    st.write("###### Local Governments")
                    st.write("  - Bagudo")

                st.subheader("Cameroun")
                with st.expander("##### Adamawa State"):
                    st.write("###### Local Governments")
                    st.write("- Mubi North")
                    st.write("- Mubi South")
                    st.write("- Maiha")
                    st.write("- Fufore")
                    st.write("- Jada")
                    st.write("- Ganye")
                    st.write("- Toungo")
                with st.expander("##### Borno State"):
                    st.write("###### Local Governments")
                    
                    st.write("  - Gwoza")
                    st.write("  - Kala/Balge")
                with st.expander("##### Cross River State"):
                    st.write("###### Local Governments")
                    st.write("  - Obanliku")
                    st.write("  - Boki")
                    st.write("  - Etung")
                    st.write("  - Akampka")
                    st.write("  - Akpabuyo")
                with st.expander("##### Taraba State"):
                    st.write("###### Local Governments")
                    st.write("  - Gashaka")
                    st.write("  - Sardauna")
                    st.write("  - Kurmi")
                    st.write("  - Ussa")
                    st.write("  - Takum")
                    
                with st.expander("##### Benue State"):
                    st.write("###### Local Governments")
                    st.write("  - Kwande")

                    
                st.subheader("Chad")
                
                with st.expander("##### Borno State"):
                    st.write("###### Local Governments")
                    
                    st.write("  - Abadam")
                    st.write("  - Kukawa")
                    
                st.subheader("Niger")
                with st.expander("##### Borno State"):
                    st.write("###### Local Governments")
                    st.write("- Abadam")
                    st.write("- Mobbar")
                    
                with st.expander("##### Jigawa State"):
                    st.write("###### Local Governments")
                    
                    st.write("  - Maigatari")
                    st.write("  - Sule Tankarkar")
                with st.expander("##### Katsina State"):
                    st.write("###### Local Governments")
                    st.write("  - Baure")
                    st.write("  - Jibia")
                    st.write("  - Kaita")
                    st.write("  - Maiadua")
                    st.write("  - Mashi")
                    st.write("  - Zango")
                    
                with st.expander("##### Kebbi State"):
                    st.write("###### Local Governments")
                    st.write("  - Arewa Dandi")
                    st.write("  - Dandi")
                    
                    
                with st.expander("##### Sokoto State"):
                    st.write("###### Local Governments")
                    st.write("  - Gada")
                    st.write("  - Gudu")
                    st.write("  - Illela")
                    st.write("  - Isa")
                    st.write("  - Sabon Birni")
                    st.write("  - Tangaza")
                    
                with st.expander("##### Yobe State"):
                    st.write("###### Local Governments")
                    st.write("  - Geidam")
                    st.write("  - Machina")
                    st.write("  - Yunusari")
                    st.write("  - Yusufari")
                    
                with st.expander("##### Zamfara State"):
                    st.write("###### Local Governments")
                    st.write("  - Zurmi")                   
                
        with tab3:
            # Tab for state and local government information
            st.markdown("## This page contains information about available data used for this site")

            st.write(df)  # Same as st.write(df)

    if page_selection == "Border Access Points":
        st.title('Border Access Points')
        st.markdown(
            "This page allows you to search for and view information about border access points in Nigeria. The information includes the location of the border point, the type of border point, and the contact information for the border point."
        )
        
        m = folium.Map(location = [df.Latitude.mean(), df.Longitude.mean()],
                       zoom_start = 5.2, control_scale = True)
        for i, row in df.iterrows():
            iframe = folium.IFrame('Bodering Country: ' + str(row['Bordering Country']) + '<br><br>' + 'State: ' + str(row['State']) + '<br><br>' + 'Local Government: ' + str(row['Local Government']) + '<br><br>' + 'Border Name: ' + str(row["Border Name"]) + '<br><br>' + 'Longitude: ' + str(row["Longitude"]) + '<br><br>' + 'Latitude: ' + str(row["Latitude"]))
            popup = folium.Popup(iframe, min_width = 375, max_width = 375)
            folium.Marker(location=[row['Latitude'], row['Longitude']],
                          popup = popup, c = row["Border Name"]).add_to(m)
        st_data = st_folium(m, width=900)
        


if __name__ == "__main__":
    main()
