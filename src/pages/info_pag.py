import streamlit as st

st.title('Water Potability')
st.text('What are some metrics we must consider when drinking water?')



st.subheader('PH Value')
st.text('''
    PH is an important parameter in evaluating the acid–base balance of water. It is 
    also the indicator of acidic or alkaline condition of water status. Who has 
    recommended maximum permissible limit of pH from 6.5 to 8.5. The current 
    investigation ranges were 6.52–6.83 which are in the range of WHO standards.
''')
st.image('https://www.qmul.ac.uk/chesswatch/media/chesswatch/ph-range-chalk-rivers.jpg')
st.subheader('Hardness')
st.text('''
    Hardness is mainly caused by calcium and magnesium salts. These salts 
    are dissolved from geologic deposits through which water travels. The length of 
    time water is in contact with hardness producing material helps determine how 
    much hardness there is in raw water. Hardness was originally defined as the 
    capacity of water to precipitate soap caused by Calcium and Magnesium.
''')
st.image('https://waterfilterguru.com/wp-content/uploads/2021/02/water-hardness-scale.jpg')
st.subheader('Solids (Total dissolved solids- TDS)')
st.text('''
    Water has the ability to dissolve a wide range of inorganic and some 
    organic minerals or salts such as potassium, calcium, sodium, bicarbonates, 
    chlorides, magnesium, sulfates etc. These minerals produced un-wanted taste and 
    diluted color in appearance of water. This is the important parameter for the 
    use of water. The water with high TDS value indicates that water is highly 
    mineralized. Desirable limit for TDS is 500 mg/l and maximum limit is 1000 mg/l 
    which prescribed for drinking purpose.
''')
st.image('https://qph.cf2.quoracdn.net/main-qimg-8aecb67a79cdc35687964ced93f4245d-lq')
st.subheader('Chloramines')
st.text('''
Chlorine and chloramine are the major disinfectants used in public water systems. 
Chloramines are most commonly formed when ammonia is added to chlorine to treat 
drinking water. Chlorine levels up to 4 milligrams per liter (mg/L or 4 parts 
per million (ppm)) are considered safe in drinking water.
''')
st.subheader('Sulfate')
st.text('''
    Sulfates are naturally occurring substances that are found in minerals, soil, 
    and rocks. They are present in ambient air, groundwater, plants, and food. 
    The principal commercial use of sulfate is in the chemical industry. Sulfate 
    concentration in seawater is about 2,700 milligrams per liter (mg/L). It 
    ranges from 3 to 30 mg/L in most freshwater supplies, although much higher 
    concentrations (1000 mg/L) are found in some geographic locations.
''')

st.subheader('Conductivity')
st.text('''
    Pure water is not a good conductor of electric current rather’s 
    a good insulator. Increase in ions concentration enhances the electrical 
    conductivity of water. Generally, the amount of dissolved solids in water 
    determines the electrical conductivity. Electrical conductivity (EC) actually
    measures the ionic process of a solution that enables it to transmit current. 
    According to WHO standards, EC value should not exceeded 400 μS/cm.
 ''')
st.image('https://www.fondriest.com/environmental-measurements/wp-content/uploads/2014/02/conductivity_averages.jpg')
st.subheader('Organic Carbon')
st.text('''
Total Organic Carbon (TOC) in source waters comes from decaying natural 
organic matter (NOM) as well as synthetic sources. TOC is a measure of 
the total amount of carbon in organic compounds in pure water. According 
to US EPA < 2 mg/L as TOC in treated / drinking water,and < 4 mg/Lit in source 
water which is use for treatment.
''')
st.image('https://proteus-instruments.com/img/DOC-Table-1-v2.jpg')
st.subheader('Trihalomethanes')
st.text('''
THMs are chemicals which may be found in water treated with chlorine. The 
concentration of THMs in drinking water varies according to the level of organic 
material in the water, the amount of chlorine required to treat the water, and 
the temperature of the water that is being treated. THM levels up to 80 ppm is 
considered safe in drinking water.
''')
st.image('https://www.researchgate.net/profile/Juan-Gonzalez-Velasco/publication/225129589/figure/tbl2/AS:667612409241603@1536182610545/Measured-trihalomethane-levels-mg-L-in-treated-water-n78.png')
st.subheader('Turbidity')
st.text('''
The turbidity of water depends on the quantity of solid matter present in the 
suspended state. It is a measure of light emitting properties of water and the 
test is used to indicate the quality of waste discharge with respect to colloidal 
matter. The mean turbidity value obtained for Wondo Genet Campus (0.98 NTU) is lower 
than the WHO recommended value of 5.00 NTU.
''')
st.image('https://www.deloachindustries.com/hs-fs/hubfs/Turbidity-NTU-of-the-water-samples-tested.jpeg?width=378&name=Turbidity-NTU-of-the-water-samples-tested.jpeg')
st.subheader('Summary')
st.text('Taking in all of these factors, this is what will determine if water is drinkable or not')