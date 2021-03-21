import altair as alt

def chart_cq_prod(DataFrame):
    chart = alt.Chart(DataFrame).mark_point().encode(
        x='file_name',
        y='CC',
        color='loc',
    ).interactive()
    chart.save('chart_cq_prod.html')

def chart_general(DataFrame):
    alt.Chart(source).mark_line().encode(
        x='key',
        y='price',
        color='symbol',
        strokeDash='symbol',
    )
