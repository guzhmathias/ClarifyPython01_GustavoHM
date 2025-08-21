import plotly.graph_objects as go

# Dados do grafico

valores_x = [0,1,2,3,4,5]
valores_y = [0,1,4,9,16,25]

# Criar um gráfico de linha
fig = go.Figure(
    data = go.Scatter(
        x=valores_x,
        y = valores_y,
        mode = 'lines+markers',
        name = 'y = x²'
        ) # Gráfico de dispersão
    )

#Adicionando título e rotulo dos eixos
fig.update_layout(

    title = 'Grafico de f = x²',
    xaxis_title = "Eixo x",
    yaxis_title = "Eixo f(x)"
    )

fig.show()