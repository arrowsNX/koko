##first download the data

### Updated Streamlit App Code
`https://gcpywjigvvtjwqgmi9dnkd.streamlit.app/`

### Explanation of the Additions


 **Average Intensity Over X-axis Chart**:
   - A new subheader and line chart are added, which visualizes the average radio intensity over the X-axis.
   - We calculate the average intensity for each X position and create a DataFrame for the line chart.
   - The line chart is displayed using `st.line_chart`.

### Running the Updated Streamlit App

1. Save the above code in your `app.py` file.
2. Make sure you have the required libraries installed:
   ```bash
   pip install streamlit numpy matplotlib scipy pandas
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

