# app.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import streamlit as st
import pandas as pd

# 1. Import libraries and load data
st.title("Perseus Molecular Cloud Radio Intensity Analysis")
st.write("This app analyzes radio intensity data from the Perseus molecular cloud.")

# About Me Section
st.header("About Me")
st.write("""
I am Koloina, a researcher interested in the habitability of exoplanets and radio astronomy.
This app filters and analyzes radio intensity data from the Perseus molecular cloud to help understand its structure and characteristics.
""")

# Upload data file
uploaded_file = st.file_uploader("Choose a .dat file", type='dat')

if uploaded_file is not None:
    # Load the data
    data = np.loadtxt(uploaded_file)

    # 2. Data exploration
    min_intensity = np.min(data)
    max_intensity = np.max(data)
    avg_intensity = np.mean(data)

    # Display intensity values
    st.write(f"**Minimum intensity:** {min_intensity}")
    st.write(f"**Maximum intensity:** {max_intensity}")
    st.write(f"**Average intensity:** {avg_intensity}")

    # Creating a histogram of the radio intensity
    fig_hist = plt.figure()
    plt.hist(data.ravel(), bins=50, color='blue', alpha=0.7)
    plt.title('Histogram of Radio Intensity')
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')
    plt.ylim(170, 240)
    st.pyplot(fig_hist)  # Display histogram in Streamlit

    # 3. Data visualization
    # Creating a grayscale image of the radio intensity distribution
    fig_img = plt.figure()
    plt.imshow(data, cmap='gray', origin="lower")
    plt.colorbar(label='Intensity')
    plt.title('Radio Intensity Distribution in the Perseus Molecular Cloud')
    plt.xlabel('X')
    plt.ylabel('Y')
    st.pyplot(fig_img)  # Display image in Streamlit

    # 4. Image processing technique
    sigma = st.slider("Select Gaussian smoothing sigma value:", min_value=0.1, max_value=5.0, value=1.25, step=0.1)
    
    # Applying Gaussian smoothing
    smoothed_data = gaussian_filter(data, sigma=sigma)

    # Visualizing the smoothed data
    fig_smoothed = plt.figure()
    plt.imshow(smoothed_data, cmap='gray', origin='lower')
    plt.colorbar(label='Intensity')
    plt.title(r'Gaussian Smoothed Radio Intensity Distribution, $\sigma={:.2f}$'.format(sigma))
    plt.xlabel('X')
    plt.ylabel('Y')
    st.pyplot(fig_smoothed)  # Display smoothed image in Streamlit

    # New Chart: Average Intensity Over X-axis
    avg_intensity_over_x = np.mean(data, axis=0)  # Average intensity along the Y-axis
    x_values = np.arange(data.shape[1])  # X-axis values

    # Creating a line chart
    st.subheader("Average Intensity Over X-axis")
    avg_intensity_df = pd.DataFrame({'X Position': x_values, 'Average Intensity': avg_intensity_over_x})
    st.line_chart(avg_intensity_df.set_index('X Position'))

else:
    st.warning("Please upload a .dat file to continue.")

