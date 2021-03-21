import altair as alt
import main
import pandas as pd



source = main.data()

chart = alt.Chart(source).mark_bar().encode(
    x='id',
    y="loc"
    )
    # The highlight will be set on the result of a conditional statement

chart_1 = alt.Chart(source).mark_circle(size=60).encode(
    x='id',
    y='CC',
    color='file_name',
    #tooltip=['Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()

chart_2 = alt.Chart(source).mark_line().encode(
    x='id',
    y='CC'
)

chart.save('chart.html')
